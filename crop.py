# Input: raw_images, please make sure that your folders adhere to SpeciesNet labeling guidelines found on their repo
# Purpose: runs MegaDetector (the first layer of SpeciesNet) on raw images to crop them
# Output: cropped_images ready to be used further

import os
from PIL import Image
from speciesnet.classifier import SpeciesNetClassifier
from speciesnet.utils import load_rgb_image

MODEL_PATH = 'speciesnet-v4.0.2a-weights'
classifier = SpeciesNetClassifier(MODEL_PATH)

raw_root_fp = 'training_data/raw_images'
crop_root_fp = 'training_data/cropped_images'

for species in os.listdir(raw_root_fp):
    species_raw_path = os.path.join(raw_root_fp, species)
    species_crop_path = os.path.join(crop_root_fp, species)
    os.makedirs(species_crop_path, exist_ok=True)

    for filename in os.listdir(species_raw_path):
        image_path = os.path.join(species_raw_path, filename)
        img = load_rgb_image(image_path)
        if img is None:
            print(f"Could not load: {filename}")
            continue

        preprocessed = classifier.preprocess(img)
        if preprocessed is not None:
            crop = Image.fromarray(preprocessed.arr)
            crop.save(os.path.join(species_crop_path, filename))
            print(f"Cropped: {filename}")
        else:
            print(f"No detection: {filename}")