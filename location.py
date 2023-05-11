

class Location:
    def __init__(self, id, time_based_descriptions, items, observations, x, y):
        self.id = id
        self.time_based_descriptions = time_based_descriptions
        self.items = items
        self.observations = observations
        self.x = x
        self.y = y

    def __str__(self):
        return self.name

    def __repr__(self):
        output = 'You are in ' + self.name + '.\n'
        output += self.description + '.\n'
        output += 'You see ' + ', '.join([str(item) for item in self.items]) + '.\n'
