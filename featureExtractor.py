import torch
import numpy as np
from speciesnet.classifier import SpeciesNetClassifier
from speciesnet.utils import load_rgb_image

class FloridaFeatureExtractor:
    def __init__(self, model_path):
        self.classifier = SpeciesNetClassifier(model_path)
        self.features = {}
        self._register_hook()

    def _register_hook(self):
        for name, module in self.classifier.model.named_modules():
            if 'avg_pool/Mean_Squeeze' in name:
                module.register_forward_hook(self._hook_fn)
                print(f"Hook registered on: {name}")
                break

    def _hook_fn(self, module, input, output):
        self.features['vector'] = output.cpu().detach().numpy()

    def extract(self, filepath, bboxes=None):
        img = load_rgb_image(filepath)
        if img is None:
            return None
        preprocessed = self.classifier.preprocess(img, bboxes=bboxes)
        if preprocessed is None:
            return None
        arr = preprocessed.arr / 255
        batch = np.stack([arr], axis=0).astype(np.float32)
        tensor = torch.from_numpy(batch).to(self.classifier.device)
        with torch.no_grad():
            self.classifier.model(tensor)
        return self.features.get('vector')