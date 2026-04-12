# Input: raw_images, please make sure that your folders adhere to SpeciesNet labeling guidelines found on their repo
# Purpose: runs MegaDetector (the first layer of SpeciesNet) on raw images to crop them
# Output: cropped_images ready to be used further

import os
from PIL import Image
from speciesnet import SpeciesNet

model = SpeciesNet()

raw_root_fp = 'training_data/raw_images'
crop_root_fp = 'training_data/cropped_images'

for species in os.listdir(raw_root_fp):
    species_raw_path = os.path.join(raw_root_fp, species)
    species_crop_path = os.path.join(crop_root_fp, species)
    os.makedirs(species_crop_path, exist_ok=True)

    for filename in os.listdir(species_raw_path):
        image_path = os.path.join(species_raw_path, filename)
        result = model.detect(image_path)

        if result['detections']:
            img = Image.open(image_path)
            width, height = img.size
            bbox = result['detections'][0]['bbox']

            left = bbox['x'] * width
            top = bbox['y'] * height
            right = left + bbox['width'] * width
            bottom = top + bbox['height'] * height

            crop = img.crop((left, top, right, bottom))
            crop.save(os.path.join(species_crop_path, filename))