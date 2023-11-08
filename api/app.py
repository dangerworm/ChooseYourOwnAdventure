import json
from workflows.game_setup_workflow import GameSetupWorkflow
from player_actions.command_parser import CommandParser

from flask import Flask, request, Response
from flask_cors import CORS, cross_origin
from player_actions.commands import run_command
from classes.game_response import GameResponse

from utils.constants import MORNING, AFTERNOON, EVENING, NIGHT

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

game_setup_workflow = GameSetupWorkflow()
game = game_setup_workflow.create_new_game()

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
    data = request.get_json(force=True)
    input = data['data']

    game_response = {}

    if input[:13] == 'create_player':
        name = input[14:]
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
        return Response(json.dumps(game_response, default=vars),
                        status=200, mimetype='application/json')
        
    parser = CommandParser()
    command, arguments = parser.get_command_and_arguments_from_input(input)

    if command != '':
        game_response = run_command(game, command, arguments)

    else:
        game_response = GameResponse(
            game.player.id, 'What do you want to do?', None)

    response = Response(json.dumps(game_response, default=vars),
                        status=200, mimetype='application/json')

    return response


if __name__ == '__main__':
    app.run(debug=True, port=5050)
