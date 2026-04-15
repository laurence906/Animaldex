import os
from featureExtractor import *
import numpy as np


MODEL_PATH = 'speciesnet-v4.0.2a-weights'
extractor = FloridaFeatureExtractor(MODEL_PATH)

def extract_all_features(extractor, splits_root, output_root):
    for split in ['train', 'val', 'test']:
        split_path = os.path.join(splits_root, split)
        for species in os.listdir(split_path):
            species_path = os.path.join(split_path, species)
            filenames = os.listdir(species_path)
            total = len(filenames)
            vectors, labels = [], []

            for i, filename in enumerate(filenames):
                filepath = os.path.join(species_path, filename)
                print(f"{split} | {species[:30]} | {i+1}/{total}", end='\r')
                vector = extractor.extract(filepath)
                if vector is not None:
                    vectors.append(vector.squeeze())
                    labels.append(species)

            output_dir = os.path.join(output_root, split)
            os.makedirs(output_dir, exist_ok=True)
            np.save(os.path.join(output_dir, f'{species}_vectors.npy'), np.array(vectors))
            np.save(os.path.join(output_dir, f'{species}_labels.npy'), np.array(labels))
            print(f"\nDone: {len(vectors)} vectors for {species[:30]} ({split})")

extract_all_features(
    extractor,
    'training_data/splits',
    'training_data/features'
)