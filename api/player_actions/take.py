from player_actions.action import Action
from random import choice

class Take(Action):
    """
    Static class so does not require __init__ or any attributes to be passed in.
    """
        
    def can_act(game, item_name):
        """
        Function to check whether the location in which the player is, has any items (weapons etc.) that 
        can be picked up. Doesn't pick them up, just checks if there any that can be picked up.
        """
        
        item_names = [item.name.lower() for item in game.player.location.items]

        valid = True
        message = ''

        if not item_name in item_names:
            valid = False
            message = 'You cannot see that item.'
        
        return valid, message
        

    def act (game, item):
        """
        Function to pick up an item. 
        Takes 2 arguments:
        1) game
        2) item  
        """
        
        #get the game object that matches the free text word for the target item
        desired_item = [location_item for location_item in game.player.location.items if location_item.name.lower() == item][0]
        
        game.player.items.append(desired_item)

        return f'You pick up the {desired_item}.'
