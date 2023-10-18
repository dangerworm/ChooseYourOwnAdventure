
class ItemTypeEntity():

  def __init__(self, id, name, description, observations, value, weight, 
  hit_points, starting_hit_points, attack_points, uses_count):
    
    self.id = id
    self.name = name
    self.description = description
    self.observations = observations
    self.value = value
    self.weight = weight
    self.hit_points = hit_points
    self.starting_hit_points = starting_hit_points
    self.attack_points = attack_points
    self.uses_count = uses_count
    self.contained_items = []
    self.effects = []