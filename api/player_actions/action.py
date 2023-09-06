
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