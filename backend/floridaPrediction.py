import pickle
import numpy as np
from speciesnet.classifier import SpeciesNetClassifier
from speciesnet.utils import load_rgb_image
from parser import *

CONFIDENCE_THRESHOLD = 0.7

class floridaClassifier:

    def __init__(self, model_path, fallback_pkl):
        # load SpeciesNet for feature exraction
        self.classifier = SpeciesNetClassifier(model_path)
        self.extracted_features = {}

        # hook into the pooling layer to capture the 1280-dim embedding
        for name, module in self.classifier.model.named_modules():
            if 'avg_pool/Mean_Squeeze' in name:
                module.register_forward_hook(self._save_features)
                break

        with open(fallback_pkl, 'rb') as f:
            saved_data = pickle.load(f)

        self.fallback_classifier = saved_data['classifier']
        self.label_encoder = saved_data['encoder']

    def _save_features(self, module, input, output):
        self.extracted_features['vector'] = output.cpu().detach().numpy()

    def predict(self, filepath, bboxes=None):
        # load and preprocess the image
        image = load_rgb_image(filepath)
        if image is None:
            return {'filepath': filepath, 'failure': 'could not load image'}

        preprocessed = self.classifier.preprocess(image, bboxes=bboxes)
        if preprocessed is None:
            return {'filepath': filepath, 'failure': 'preprocessing failed'}

        # run the forward pass just to trigger the feature hook
        self.classifier.predict(filepath, preprocessed)

        # grab the captured feature vector
        feature_vector = self.extracted_features.get('vector')
        if feature_vector is None:
            return {'filepath': filepath, 'failure': 'feature extraction failed'}

        # run the fallback classifier on the extracted features
        probabilities = self.fallback_classifier.predict_proba(feature_vector)
        best_index = np.argmax(probabilities)
        confidence = probabilities[0][best_index]
        species = self.label_encoder.inverse_transform([best_index])[0]
        species = species.partition(';')[2]

        return {
            'filepath': filepath,
            'species': species,
            'confidence': float(confidence),
            'source': 'fallback'
        }