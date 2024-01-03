

from player_actions.action import Action

class Investigate(Action):
    """
    Static class so does not require __init__ or any attributes to be passed in.
    """

    def can_act(game, target):
        """
        Function to check whether the location has any items or creatures the player can
        investigate.
        """

        investigate_target_names, _ = Action.get_nearby_items(game, target, includeCreatures = True)
        
        valid = True
        message = ''

        if target not in investigate_target_names:
            valid = False
            message = f'There is no {target} to investigate.'

        elif target == None:
            valid = False
            message = 'You did not specify anything to investigate.'
        
        return valid, message
        

    def act (game, target):
        """
        Function to investigate a creature or item (a 'target') 
        Takes 2 arguments:
        1) game
        2) target  
        """

        investigate_targets = []

        # Get the game object(s) that match the free text word for the target creature
        investigate_targets = [creature for creature in game.player.location.creatures if creature.name.lower() == target.lower()]
        investigate_targets += [item for item in game.player.location.items if item.name.lower() == target.lower()]

        thing_to_investigate = investigate_targets[0]

        observations = [str(thing_to_investigate), thing_to_investigate.investigation(game.items)]
        
        message = f'You investigate the {target}. {" ".join(observations)}'
        return message
