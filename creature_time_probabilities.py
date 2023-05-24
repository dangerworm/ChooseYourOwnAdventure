import random

class CreatureTimeProbabilities():
    #attributes
    def __init__(self, id, creature_type_id, creature_time_probabilities) -> None:
        self.id = id
        self.creature_type_id = creature_type_id
        self.creature_time_probabilities = creature_time_probabilities

    #methods
    def should_spawn_creature(self, time_of_day):
        probability = random.random()
        return probability < self.creature_time_probabilities[time_of_day]
