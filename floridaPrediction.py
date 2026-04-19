import pickle
import torch
import numpy as np
from speciesnet.classifier import SpeciesNetClassifier
from speciesnet.utils import load_rgb_image

class FloridaSpeciesNet:

    CONFIDENCE_THRESHOLD = 0.7

    def __init__(self, model_path, fallback_pkl):
        self.classifier = SpeciesNetClassifier(model_path)
        self.features = {}
        for name, module in self.classifier.model.named_modules():
            if 'avg_pool/Mean_Squeeze' in name:
                module.register_forward_hook(self._hook_fn)
                break
        with open(fallback_pkl, 'rb') as f:
            saved = pickle.load(f)
        self.fallback = saved['classifier']
        self.encoder = saved['encoder']

    def _hook_fn(self, module, input, output):
        self.features['vector'] = output.cpu().detach().numpy()

    def predict(self, filepath, bboxes=None):
        img = load_rgb_image(filepath)
        if img is None:
            return {'filepath': filepath, 'failure': 'could not load image'}
        preprocessed = self.classifier.preprocess(img, bboxes=bboxes)
        if preprocessed is None:
            return {'filepath': filepath, 'failure': 'preprocessing failed'}

        speciesnet_result = self.classifier.predict(filepath, preprocessed)
        top_score = speciesnet_result['classifications']['scores'][0]
        top_label = speciesnet_result['classifications']['classes'][0]

        if top_score >= self.CONFIDENCE_THRESHOLD and not "blank" in top_label:
            return {
                'filepath': filepath,
                'species': top_label,
                'confidence': top_score,
                'source': 'speciesnet'
            }

        vector = self.features.get('vector')
        if vector is None:
            return {
                'filepath': filepath,
                'species': top_label,
                'confidence': top_score,
                'source': 'speciesnet_uncertain'
            }

        probabilities = self.fallback.predict_proba(vector)
        top_idx = np.argmax(probabilities)
        fallback_confidence = probabilities[0][top_idx]
        fallback_species = self.encoder.inverse_transform([top_idx])[0]

        return {
            'filepath': filepath,
            'species': fallback_species,
            'confidence': fallback_confidence,
            'speciesnet_suggestion': top_label,
            'speciesnet_confidence': top_score,
            'source': 'fallback'
        }