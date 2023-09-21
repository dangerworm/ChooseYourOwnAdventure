# ChooseYourOwnAdventure
## How to run
To run this game, go into the `api` folder and run 

`python -m flask --app app --debug run --port 5050`

Then go into the `client` folder and run 

`npm start`

# How to build the docker container
in the terminal type the following:

`docker-compose build --no-cache postgres`

then, type:

`docker-compose up -d postgres`

then open dbeaver