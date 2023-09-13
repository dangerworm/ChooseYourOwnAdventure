
class Action:
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
        
    def get_available_targets(game, target):
        
        target_names = [creature.name.lower() for creature in game.player.location.creatures]
        target_names += [item.name.lower() for item in game.player.location.items]

        is_creature = False
        action_targets = [creature for creature in game.player.location.creatures if creature.name.lower() == target.lower() and creature.hit_points > 0]
        if len(action_targets) > 0:
            is_creature = True

        return target_names, is_creature