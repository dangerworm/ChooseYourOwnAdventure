from player_actions.action import Action
from random import choice

class Attack(Action):
    """
    Static class so does not require __init__ or any attributes to be passed in.
    """

    def can_act(game, target, weapons):
        """
        Function to check whether the player has any equipment (weapons etc.) that 
        can be used to attack a target, and whether the target is in the same
        location, to be attacked.
        
        """
        
        attack_target_names, is_creature = Action.get_available_targets(game, target)
        
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
        
        return valid, message, is_creature
        

    def act (game, target, is_creature, weapons):
        """
        Function to attack a target (e.g. enemy, object such as a door, etc.). 
        Takes 4 arguments:
        1) game
        2) target 
        3) is_creature (boolean) 
        4) weapons
        """

        attack_targets = []
        attack_weapons = []

        if target == 'game_player':
            attack_targets = [game.player]
        else:
            # Get the game object(s) that match the free text word for the target creature
            attack_targets = [creature for creature in game.player.location.creatures if creature.name.lower() == target.lower() and creature.hit_points > 0]
            attack_targets += [item for item in game.player.location.items if item.name.lower() == target.lower()]
            
            if len(attack_targets) == 0:
                attack_targets = [creature for creature in game.player.location.creatures if creature.name.lower() == target.lower()]

            attack_weapons = [item for item in game.player.items if item.name.lower() in weapons]
            attack_weapons += [item for item in game.player.location.items if item.name.lower() in weapons]

        if weapons[0] == 'fist':
            attack_weapons = [type('',(object,),{'attack_points': 1})()]

        thing_to_hit = attack_targets[0]

        was_dead = thing_to_hit.hit_points <= 0

        start_hp = thing_to_hit.hit_points
        
        for weapon in attack_weapons:
            thing_to_hit.hit_points -= weapon.attack_points

        hp = thing_to_hit.hit_points

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
        is_dead = was_dead

        if was_dead:
            adjective =  'dead '
        elif hp <= 0:
            extra_text = f' and {killed} it.'
            is_dead = True
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

        if target == 'game_player':
            hp_comment = ''
            if hp <= 0:
                hp_comment = 'You are dead'
            else:
                hp_comment = f'You now have {hp} health'
            message = f'It hit you back with its {", ".join(weapons)} and you lost {start_hp - hp} health. {hp_comment}'
            return thing_to_hit, is_dead, message
        else:
            message = f'You attacked the {adjective}{target} with your {", ".join(weapons)}{extra_text}'
            return thing_to_hit, is_dead, message
