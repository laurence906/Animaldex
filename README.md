# Animal-Recognition-Pokedex  
**AnimalDex** is a web app designed to encourage users to explore, engage with, and learn about the nature around them.

## Project Idea & Functionality
AnimalDex utilizes [**Google's SpeciesNet**](https://github.com/google/cameratrapai), an AI model built for animal recognition on camera traps, to recognize the animals within photographs uploaded by users. Upon recognition, users are provided some brief information about the creature seen in their photograph.

## Setup & Other Info
Usage: 
    Delete all .gitkeep files from training_data and its subfolders.
    Add properly named subfolders of training data in ./training_data/cropped_images
    Run crop.py and split.py in succession.

This branch is not intended to be functional, it is simply the branch that contains the scripts that were used for fine-tuning the model. It also incldues the updated weights that were generated after fine-tuning. The fine-tuning was done on a set of images well over 100GB in size, so it is not included in this branch for obvious reasons. All data that was used in the fine-tuning of the model will be credited below.

[UCF's Florida Wildlife Camera Trap Dataset](https://www.crcv.ucf.edu/research/projects/florida-wildlife-camera-trap-dataset/)
