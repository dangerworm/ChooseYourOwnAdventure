

#Import repositories
from repositories.locations_repository import LocationsRepository
from repositories.items_repository import ItemsRepository
from repositories.creature_types_repository import CreatureTypesRepository

#Import time of day
from utils.constants import MORNING

from classes.game import Game

class GameSetupWorkflow:
  def __init__(self) -> None:
    self.location_repository = LocationsRepository()
    self.items_repository = ItemsRepository()
    self.creature_types_repository = CreatureTypesRepository()

    def create_new_game(self):
      items = self.items_repository.get_all()
      creature_types = self.creature_types_repository.get_all()
      locations = self.location_repository.get_all()
      
      game = Game(items, creature_types, locations)

      return game