from random import choice

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
            return target, [weapon.lower() for weapon in arguments['weapons']]
        else:
            return target, ['fist']


    def can_act(game, target, weapons):
        """
        Function to check whether the play has any equipment (weapons etc.) that 
        can be used to attack a target, and whether the target is in the same
        location, to be attacked.
        
        """
        
        attack_target_names = [creature.name.lower() for creature in game.player.location.creatures]
        attack_target_names += [item.name.lower() for item in game.player.location.items]
        
        item_names = [item.name.lower() for item in game.player.items]
        item_names += [item.name.lower() for item in game.player.location.items]
        
        all_items_in_item_names = True

        for item in weapons:
            if item != 'fist' and item not in item_names:
                all_items_in_item_names = False

        valid = True
        message = ''

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
        is_creature = False

        attack_targets = [creature for creature in game.player.location.creatures if creature.name.lower() == target.lower() and creature.hit_points > 0]
        if len(attack_targets) > 0:
            is_creature = True

        attack_targets += [item for item in game.player.location.items if item.name.lower() == target.lower()]
        
        if len(attack_targets) == 0:
            attack_targets = [creature for creature in game.player.location.creatures if creature.name.lower() == target.lower()]

        attack_weapons = [item for item in game.player.items if item.name.lower() in weapons]
        attack_weapons += [item for item in game.player.location.items if item.name.lower() in weapons]

        if weapons[0] == 'fist':
            attack_weapons = [type('',(object,),{'attack_points': 1})()]

        was_dead = attack_targets[0].hit_points <= 0

        for weapon in attack_weapons:
            attack_targets[0].hit_points -= weapon.attack_points

        hp = attack_targets[0].hit_points
        start_hp = attack_targets[0].starting_hit_points

        first_hits = []
        weakened = []
        injured = []
        bloodied = []
        death = ''
        killed = ''

        if is_creature:
            # Creature adjectives
            first_hits = ['angry ', 'annoyed ', 'aggravated ']
            weakened = ['weakened ', 'surprised ', 'scraped ']
            injured = ['injured ', 'aggrieved ', 'gored ']
            bloodied = ['bloodied ', 'battered ', 'mutilated ']
            death = 'death'
            killed = 'killed'
        else:
            # Item adjectives
            first_hits = ['hard ', 'sturdy ', 'solid ']
            weakened = ['cracked ', 'dented ', 'damaged ']
            injured = ['broken ', 'holed ', 'heavily damaged ']
            bloodied = ['smashed ', 'battered ', 'demolished ']
            death = 'destruction'
            killed = 'destroyed'

        adjective = ''
        extra_text = ''

        if was_dead:
            adjective =  'dead '
        elif hp <= 0:
            extra_text = f' and {killed} it.'
        elif hp < round(start_hp * 0.25, 0):
            adjective = choice(bloodied)
            extra_text = f', {death} is near...'
        elif hp < round(start_hp * 0.5, 0):
            adjective = choice(injured)
            extra_text = ', it is looking worse for wear!'
        elif hp < round(start_hp * 0.75, 0):
            adjective = choice(weakened)
        else:
            adjective = choice(first_hits)

        return f'You attacked the {adjective}{target} with your {", ".join(weapons)}{extra_text}'
