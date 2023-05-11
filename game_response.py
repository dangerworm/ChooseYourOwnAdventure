import json

class GameResponse:
    def __init__(self, player_id, message, data):
        self.player_id = player_id
        self.message = message
        self.data = data
