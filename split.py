# Input: Output from previous stage, in cropped_images
# Output: Input will be randomly spread across the 3 folders found in 'splits'


import os
import shutil
import random

crop_root = 'training_data/cropped_images'
splits_root = 'training_data/splits'

for species in os.listdir(crop_root):
    images = os.listdir(os.path.join(crop_root, species))
    random.shuffle(images)

    n = len(images)
    train_end = int(0.7 * n)
    val_end = int(0.85 * n)

    splits = {
        'train': images[:train_end],
        'val': images[train_end:val_end],
        'test': images[val_end:]
    }

    for split_name, split_images in splits.items():
        dest = os.path.join(splits_root, split_name, species)
        os.makedirs(dest, exist_ok=True)
        for img in split_images:
            shutil.copy(
                os.path.join(crop_root, species, img),
                os.path.join(dest, img)
            )