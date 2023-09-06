from classes.creature import Creature
from utils.constants import DIRECTIONS

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

    def determine_creature_alive_or_dead(self, creature):
        if creature.hit_points <= 0:
            return f'dead {creature.description}'
        else:
            return creature.description

    def location_summary(self, time_of_day):
        output = self.time_based_descriptions[time_of_day] + '.\n'
        output += 'There are exits to the '
        output += ', '.join([DIRECTIONS[exit] for exit in self.exits]) + '.\n'
        
        if len(self.items) > 0:
            output += self.observations_and_items()
        
        if len(self.creatures) > 0:
            output += self.visible_creatures()

        return output

    def observations_and_items(self):
        observations = [str(observation) for observation in self.observations]
        items = [str(item) for item in self.items]

        output = ''
        if len(observations) > 0:
            output += ", ".join(observations) + '\n'

        if len(items) > 0:
            output += f'You see {", ".join(items)} \n'

        return output

    def visible_creatures(self):
        creatures = ['a ' + self.determine_creature_alive_or_dead(creature) for creature in self.creatures]
        
        if len(creatures) > 0:
            return f'You see {", ".join(creatures)}\n'
        else:
            return ''

    def spawn_creatures(self, game):
        creature_type_spawned_ids = []

        for creature_probability in self.creature_time_probabilities:
            if creature_probability.should_spawn_creature(game.time_of_day):
                creature_type_spawned_ids.append(creature_probability.creature_type_id)
                    
        creature_types = [creature_type for creature_type in game.creature_types if creature_type.id in creature_type_spawned_ids]

        self.creatures = [Creature.generate(creature_type) for creature_type in creature_types]
    
    