# Chatter
Chatter is a chat bot

## How it works
Chatter is a chatbot that accepts input and returns an output.

Example:

      ____ _             _     _
     / ___| |__   __ _ _| |_ _| |_  ___ _ __
    | |   | '_ \ / _` |_   _|_   _|/ _ \ '__|
    | |___| | | | (_| | | |   | | |  __/ |
     \____|_| |_|\__,_| |_|   |_|  \___|_|

    Welcome to Jesse's Docker Chatter CLI!

Type your input below. Type 'exit' to quit.

You: Tell me a joke about a cybersecurity engineer playing table tennis
AI: Why did the cybersecurity engineer always win at table tennis?

Because he knew how to handle all the “backspins”!

You: Tell me a better joke
AI: Sure, here’s one for you:

Why don't scientists trust atoms?

Because they make up everything!


## Setup Instructions

### Open AI Account/API Key
First, go to platform.openai.com and sign up for a free account.
After signing up for an account, you can obtain an API key
Create an .env file (name it ".env"). Add the api key value to the newly created .env file.
Format should be:
'OPENAIAPIKEY=abcdefghi1234567'

### Run from Docker
docker run -it --rm --env-file ./.env jdschiewe/chatter


## Other Details

### Build New Docker Image and Push to DockerHub
If you want to run from Docker:
docker build -t jdschiewe/chatter .
docker push jdschiewe/chatter:latest

### Update Python Dependencies
To update Python dependencies (requirements.txt):
pip freeze > requirements.txt


### Run Automated Tests
python -m unittest test_docker_chatter.py
python -m unittest test_chatform.py
