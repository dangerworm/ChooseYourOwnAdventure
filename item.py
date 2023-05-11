class Item:
    def __init__(self, id, name, description, observations, effects, contains, value, hit_points, attack_points, uses_count):
        self.id = id
        self.name = name
        self.description = description
        self.observations = observations
        self.effects = effects
        self.contains = contains
        self.value = value
        self.hit_points = hit_points
        self.attack_points = attack_points
        self.uses_count = uses_count

    def on_take(self):
        print(f"You have picked up {self.name}")

    def on_drop(self):
        print(f"You have dropped {self.name}")

    def __str__(self):
        return f"{self.name}: {self.description}"
