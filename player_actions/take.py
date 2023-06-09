from random import choice

class Take():
    """
    Static class so does not require __init__ or any attributes to be passed in.
    """


    def parse(game, arguments):
        item_exists = 'target' in arguments and len(arguments['target']) > 0        
        if item_exists:
            return arguments['target']
        else:
            pass
        
    def can_act(game, item):
        """
        Function to check whether the location in which the player is, has any items (weapons etc.) that 
        can be picked up. Doesn't pick them up, just checks if there any that can be picked up.
        """
        
        item_names = [item.name.lower() for item in game.player.location.items]
        item_exists = item in item_names
        
        valid = True
        message = ''

        if not item_exists:
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

        return f'You pick up the {desired_item}.'
