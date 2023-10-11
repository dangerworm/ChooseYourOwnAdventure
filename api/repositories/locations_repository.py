
from repositories.base_repository import BaseRepository
from classes.location import Location

class LocationsRepository(BaseRepository):
    def __init__(self) -> None:
      super().__init__()
    
    def get_all(self):
      query = "select id, time_based_descriptions, observations, exits, x, y from setup.locations"
      list_records = super().get_all(query)
      return self.create_objects(list_records)
    
  
    def create_objects(self,list_records):
      dict_records = {}

      number_of_records = len(list_records)
      for record_number in range(number_of_records):
        record = list_records[record_number]
        object = Location(*record)
        dict_records[object.id] = object
      
      return dict_records