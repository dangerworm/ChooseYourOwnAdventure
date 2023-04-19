import json

from flask import Flask, request, Response
from game import Game
from game_response import GameResponse

app = Flask(__name__)
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
        game_response = GameResponse('Welcome back, adventurer!', None)

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

    if game.player == None:
        game_response = GameResponse(None, 'You must set up a character before playing.',
                                     {
                                         "questions": [
                                             "What is your name?"
                                         ]
                                     })
    elif data['command'] == 'look':
        game_response = GameResponse(
            game.player.id, game.player.location.description, None)
    elif data['command'] == 'go':
        game.player.location = game.locations[data.arguments.location]
        game_response = GameResponse(
            game.player.id, game.player.location.name, None)
    else:
        game_response = GameResponse(
            game.player.id, 'What do you want to do?', None)

    response = Response(json.dumps(game_response, default=vars),
                        status=200, mimetype='application/json')

    return response


if __name__ == '__main__':
    app.run(debug=True)
