# Animal-Recognition-Pokedex  
**AnimalDex** is a web app designed to encourage users to explore, engage with, and learn about the nature around them.

## Project Idea & Functionality
AnimalDex utilizes [**Google's SpeciesNet**](https://github.com/google/cameratrapai), an AI model built for animal recognition on camera traps, to recognize the animals within photographs uploaded by users. Upon recognition, users are provided some brief information about the creature seen in their photograph.

## Setup & Other Info
This branch holds the backend ML Model logic. This varies from test images used for verification, to dictionary parsing and SpeciesNet API calls. If interested, you would only want to run the tests.py or speciesnet_test.py files; they are the only ones with actual behavior. speciesnet_api.py contains the prototype of the backend API used throughout the project. If you run into any issues running the code here, first make sure you have updated your environment according to requirements.txt, and then make sure the code you are running is calling a valid filepath.
