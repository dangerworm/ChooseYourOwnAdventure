# ChooseYourOwnAdventure

# STEP ONE!
Check the terminal is in the right environment if you are using an environment (Matt!)

# Quick start
if you have an environment, activate that environment

Open Docker and DBeaver

open two terminals
in one of these type:

`./startup-api.sh`

This will fail first time due to the speed. Don't panic. Run it again. 

press enter

In the other terminal type:

`./startup-client.sh`


press enter

# How to build the docker container
in the terminal type the following:

`docker-compose build --no-cache postgres`

then, type:

`docker-compose up -d postgres`

then open dbeaver


## How to run
To run this game, go into the `api` folder and run 

`python -m flask --app app --debug run --port 5050`

Then go into the `client` folder and run 

`npm start`

