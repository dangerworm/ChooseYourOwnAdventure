
from constants import DIRECTIONS

class Location:
    def __init__(self, id, time_based_descriptions, observations, exits, items, x, y):
        self.id = id
        self.time_based_descriptions = time_based_descriptions
        self.observations = observations
        self.exits = exits
        self.items = items
        self.x = x
        self.y = y

    def location_summary(self, time_of_day):
        output = self.time_based_descriptions[time_of_day] + '.\n'
        output += 'There are exits to the '
        output += ', '.join([DIRECTIONS[path] for path in self.exits])
        return output

    def observations_and_items(self):
        output = '/n'.join([str(observation) for observation in self.observations]) + '\n'
        output += 'You see ' + ', '.join([str(item) for item in self.items]) + '.\n'
        return output


    