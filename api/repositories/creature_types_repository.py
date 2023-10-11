import psycopg2

from repositories.base_repository import BaseRepository
from classes.creature_type import CreatureType

class EffectsRepository(BaseRepository):
    def __init__(self) -> None:
        super().__init__()

    def get_all(self):
      query = "select id, name, description, characteristics, observations, weaknesses, resistances, immunities from setup.item"
      list_records = super().get_all(query)
      return self.create_objects(list_records)

  
    def create_objects(self,list_records):
      dict_records = {}

      number_of_records = len(list_records)
      for record_number in range(number_of_records):
        record = list_records[record_number]
        object = CreatureType(*record)
        dict_records[object.id] = object
      
      return dict_records
    