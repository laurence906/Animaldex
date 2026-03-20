# Animal-Recognition-Pokedex  
**AnimalDex** is a web app designed to encourage users to explore, engage with, and learn about the nature around them.

## Project Idea & Functionality
AnimalDex utilizes [**Google's SpeciesNet**](https://github.com/google/cameratrapai), an AI model built for animal recognition on camera traps, to recognize the animals within photographs uploaded by users. Upon recognition, users are provided some brief information about the creature seen in their photograph.

## Setup & Other Info
If running on Windows, run on Command Prompt, NOT Windows Powershell.
Running flask/backend server:
    In Animaldex/, run .venv/Scripts/flask.exe run --no-debugger
Running frontend server:
    In Animaldex/frontent/my-react-app, run npm run dev