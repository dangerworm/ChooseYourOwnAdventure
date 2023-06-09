import json

from flask import Flask, request, Response
from flask_cors import CORS
from player_actions.commands import run_command
from game import Game
from classes.game_response import GameResponse

from constants import MORNING, AFTERNOON, EVENING, NIGHT

app = Flask(__name__)
CORS(app)

game = Game()


@app.route('/', methods=['GET'])
def welcome():
    game_response = {}

    if game.player == None:
        game_response = GameResponse(None, 'Welcome, adventurer! Please set up a character.',
                                     {
                                         "questions": [
                                             "What is your name?"
                                         ]
                                     })
    else:
        game_response = GameResponse(game.player.id, 'Welcome back, adventurer!', None)

    response = Response(json.dumps(game_response, default=vars),
                        status=200, mimetype='application/json')

    return response


@app.route('/command', methods=['POST'])
def command():
    data = request.get_json()
    game_response = {}

    if data['command'] == 'create_player':
        name = data['arguments']['name']
        game.setup_player(name, 'n')

        game_response = GameResponse(
                game.player.id, game.player.location.location_summary(MORNING), None)

        return Response(json.dumps(game_response, default=vars),
                        status=200, mimetype='application/json')


    if game.player == None:
        game_response = GameResponse(None, 'You must set up a character before playing.',
                                     {
                                         "questions": [
                                             "What is your name?"
                                         ]
                                     })
    elif data['command'] != '':
        game_response = run_command(game, data['command'], data['arguments'])

    elif data['command'] == 'look':
        game_response = GameResponse(
            game.player.id, game.player.location.description, None)

    elif data['command'] == 'go':
        # Get the location name from the arguments in data
        location_name = data['arguments']['location']
        
        # Find all locations with location_name in their name
        locations = [location for location in game.locations if location_name.lower() in location.name.lower()]

        if len(locations) == 1:
            game.player.location = locations[0]
            game_response = GameResponse(
                game.player.id, game.player.location.description, None)

    else:
        game_response = GameResponse(
            game.player.id, 'What do you want to do?', None)

    response = Response(json.dumps(game_response, default=vars),
                        status=200, mimetype='application/json')

    return response


if __name__ == '__main__':
    app.run(debug=True, port=5050)
