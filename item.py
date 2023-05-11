class Item:
    def __init__(self, id, name, description, value, effects, observations, items):
        self.id = id
        self.name = name
        self.description = description
        self.value = value
        self.effects = effects
        self.observations = observations
        self.items = items

    def on_take(self):
        print(f"You have picked up {self.name}")

    def on_drop(self):
        print(f"You have dropped {self.name}")

    def __str__(self):
        return f"{self.name}: {self.description}"
