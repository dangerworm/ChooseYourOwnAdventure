
"""
Purpose:
To manage the set up of a location that the player has entered, e.g.:
- check for history of location (ensure dead enemies still dead, loot still looted, etc.)
"""

#Import repositories
from repositories.locations_repository import LocationsRepository
from repositories.items_repository import ItemsRepository
from repositories.creature_types_repository import CreatureTypesRepository


class LocationSetupWorkflow:
  def __init__(self) -> None:
    self.location_repository = LocationsRepository()
    self.items_repository = ItemsRepository()
    self.creature_types_repository = CreatureTypesRepository()

  def build_location(self, location_id, time_of_day):
    location = self.location_repository.get_by_id(location_id)
    
    #TODO:
    #check player history and pick up items and creatures that have been left behind in this location
    #e.g. dead / alive, loot left

    #build creature types (based on spawn creatures function)
    #build items (based on spawn creatures function)

    return location