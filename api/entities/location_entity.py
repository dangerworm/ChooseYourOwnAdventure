

class LocationEntity():
  """
  This is a 'Plain Old Object (POO ;) ) class, i.e. attribute only class. 
  It holds data and does nothing with it, i.e. has no methods to use the data with.
  """
  def __init__(self, id, time_based_descriptions, exits, observations, x, y):
    #attributes
    self.id = id
    self.time_based_descriptions = time_based_descriptions
    self.exits = exits
    self.observations = observations
    self.x = x
    self.y = y
    self.creature_types = []
    self.items = []

