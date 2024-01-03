
from player_actions.action import Action

class Drop(Action):
    """
    Static class so does not require __init__ or any attributes to be passed in.
    """

    def can_act(game, item_name):
        """
        Function to check whether the player has any equipment (weapons etc.) that 
        can be dropped        
        """
        
        item_names = [item.name.lower() for item in game.player.items]

        valid = True
        message = ''

        if item_name not in item_names:
            valid = False
            message = f'You do not have {item_name} to drop.'

        elif item_name == None:
            valid = False
            message = 'You did not specify an item to drop.'
        
        return valid, message
    
    def act(game, item_name):
        """
        Function to drop an item (e.g. weapon, object etc.). 
        Takes 2 arguments:
        1) game
        2) item 
        """

        item = [item for item in game.player.items if item.name.lower() == item_name][0]
        
        game.player.items.remove(item)
        game.player.location.items.append(item)

        message = f'You have dropped the {item_name}'
        
        return message