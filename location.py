from constants import DIRECTIONS
from creature import Creature

class Location:
    def __init__(self, id, time_based_descriptions, observations, exits, items, x, y, creature_time_probabilities):
        self.id = id
        self.time_based_descriptions = time_based_descriptions
        self.observations = observations
        self.exits = exits
        self.items = items
        self.x = x
        self.y = y
        self.creature_time_probabilities = creature_time_probabilities
        self.creatures = []

    def location_summary(self, time_of_day):
        output = self.time_based_descriptions[time_of_day] + '.\n'
        output += 'There are exits to the '
        output += ', '.join([DIRECTIONS[path] for path in self.exits]) + '.\n'
        if len(self.creatures) == 0:
            return output
        output += 'You see '
        output += ', '.join([creature.description for creature in self.creatures]) + '.\n'
        return output

    def observations_and_items(self, list_of_items):
        output = '/n'.join([str(observation) for observation in self.observations]) + '\n'
        output += 'You see ' + ', '.join([str(item) for item in list_of_items]) + '.\n'
        return output

    def spawn_creatures(self, game):
        creature_type_spawned_ids = []

        for creature_probability in self.creature_time_probabilities:
            if creature_probability.should_spawn_creature(game.time_of_day):
                creature_type_spawned_ids.append(creature_probability.creature_type_id)
                    
        creature_types = [creature_type for creature_type in game.creature_types if creature_type.id in creature_type_spawned_ids]

        print(creature_types)
    
        self.creatures = [Creature.generate(creature_type) for creature_type in creature_types]