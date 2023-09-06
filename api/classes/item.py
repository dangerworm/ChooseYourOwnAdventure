class Item:
    def __init__(self, id, name, description, observations, weight, effects, contains, value, hit_points, attack_points, uses_count):
        self.id = id
        self.name = name
        self.description = description
        self.observations = observations
        self.weight = weight
        self.effects = effects
        self.contains = contains
        self.value = value
        self.hit_points = hit_points
        self.starting_hit_points = hit_points
        self.attack_points = attack_points
        self.uses_count = uses_count

    def __str__(self):
        return f"{self.description}"

    def investigation(self, item_objects):
        list_of_items = [item for item in item_objects if item.id in self.contains]
        output = 'You see ' + ', '.join([str(item) for item in list_of_items]) + '.\n'
        return output
