
class CreatureTypeEntity():
  """
  This is a 'Plain Old Object (POO ;) ) class, i.e. attribute only class. 
  It holds data and does nothing with it, i.e. has no methods to use the data with.
  """
  def __init__(self, id, name, description, observations, time_probabilities, 
               hit_points_range, agility_range, charisma_range, endurance_range, 
               intelligence_range, mana_range, perception_range, strength_range, 
               immunities, resistances, weaknesses):
    #attributes
    self.id = id
    self.name = name
    self.description = description
    self.observations = observations
    self.time_probabilities = time_probabilities
    self.hit_points_range = hit_points_range
    self.agility_range = agility_range
    self.charisma_range = charisma_range
    self.endurance_range = endurance_range
    self.intelligence_range = intelligence_range
    self.mana_range = mana_range
    self.perception_range = perception_range
    self.strength_range = strength_range
    self.immunities = immunities
    self.resistances = resistances
    self.weaknesses = weaknesses
