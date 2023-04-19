class Location:
    def __init__(self, id, name, connections, description, items, observations):
        self.id = id
        self.name = name
        self.connections = connections
        self.description = description
        self.items = items
        self.observations = observations

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name
