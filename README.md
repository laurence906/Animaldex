# Animal-Recognition-Pokedex  
**AnimalDex** is a web app designed to encourage users to explore, engage with, and learn about the nature around them.

## Project Idea & Functionality
AnimalDex utilizes [**Google's SpeciesNet**](https://github.com/google/cameratrapai), an AI model built for animal recognition on camera traps, to recognize the animals within photographs uploaded by users. Upon recognition, users are provided some brief information about the creature seen in their photograph.

## Setup & Other Info
- Make sure to have node and Mongo Compass installed. 
- Start a virtual environment using Python 3.12 in the backend folder and install from requirements.txt
- Set up a .env file in backend folder, and paste a format similar to this:\
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''\
MONGO_URI=mongodb://localhost:27017\
DB_NAME=animaldex\
SECRET_KEY=[yourkeyhere]\
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
- Navigate to the frontend folder and run "npm install".

**Once all set up, to run app (using bash):**
- Open terminal, cd to backend, start venv (venv/Scripts/activate), and run "python app.py".
- Open second terminal, cd to frontend, run "npm run dev".
