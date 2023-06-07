

class Attack():
    """
    Static class so does not require __init__ or any attributes to be passed in.
    """


    def parse(game, arguments):
        target_exists = 'target' in arguments and len(arguments['target']) > 0        
        if target_exists:
            target = arguments['target']
        else:
            target = None

        weapons_exists = 'weapons' in arguments and len(arguments['weapons']) > 0

        if weapons_exists:
            return target, arguments['weapons']
        else:
            return target, ['fist']


    def can_act(game, target, weapons):
        """
        Function to check whether the play has any equipment (weapons etc.) that 
        can be used to attack a target, and whether the target is in the same
        location, to be attacked.
        
        """
        
        attack_target_names = [creature.name for creature in game.player.location.creatures]
        attack_target_names += [item.name for item in game.player.location.items]
        
        item_names = [item.name for item in game.player.items]
        item_names += [item.name for item in game.player.location.items]
        
        all_items_in_item_names = True

        for item in weapons:
            if item != 'fist' and item not in item_names:
                all_items_in_item_names = False

        valid = True

        if target not in attack_target_names:
            valid = False
            message = f'There is no {target} to attack.'

        elif target == None:
            valid = False
            message = 'You did not specify a target to attack.'
        
        elif not all_items_in_item_names:
            valid = False
            if len(item_names) == 1:
                message = 'You do not have that item.'
            else:
                message = 'You do not have those items.'
        
        return valid, message
        

    def act (game, target, weapons):
        """
        Function to attack a target (e.g. enemy, object such as a door, etc.). 
        Takes 2 arguments:
        1) game
        2) target  
        """
        
        #get the game object that matches the free text word for the target creature
        attack_targets = [creature for creature in game.player.location.creatures if creature.name == target and creature.hit_points > 0]
        attack_targets += [item for item in game.player.location.items if item.name == target]
        
        if len(attack_targets) == 0:
            attack_targets = [creature for creature in game.player.location.creatures if creature.name == target]

        attack_weapons = [item for item in game.player.items if item.name in weapons]
        attack_weapons += [item for item in game.player.location.items if item.name in weapons]

        if weapons[0] == 'fist':
            attack_weapons = [type('',(object,),{'attack_points': 1})()]

        for weapon in attack_weapons:
            attack_targets[0].hit_points -= weapon.attack_points

        message = f'You attacked the {target} with your {", ".join(weapons)}'

        if attack_targets[0].hit_points < 0:
            message += ' and killed it.' 
        
        return message