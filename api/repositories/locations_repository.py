
from repositories.base_repository import BaseRepository
from classes.location import Location

class LocationsRepository(BaseRepository):
    def __init__(self) -> None:
      super().__init__()
    
    def get_all(self):
      query = "select id, time_based_descriptions, observations, exits, x, y from setup.locations"
      list_records = super().get_all(query)
      entities = self.create_entities(list_records)
      
      query = "select location_id, creature_type_id from public.location_creature_types"
      list_records = super().get_all(query)
      dict_location_to_creature_type_id = super().create_id_dictionary(list_records)
    
      query = "select location_id, item_id from public.location_items"
      list_records = super().get_all(query)
      dict_location_to_item_id = super().create_id_dictionary(list_records)

      for location_id in entities.keys():
        entities[location_id].creature_types = dict_location_to_creature_type_id[location_id]
        entities[location_id].items = dict_location_to_item_id[location_id]
      
      return entities
    
    def get_by_id(self, id):
      query = "select id, time_based_descriptions, observations, exits, x, y from setup.locations WHERE id = {0}"
      record = super().get_by_id(query, id)
      entity = self.create_entity(record)

      #list_records here contains creature types in the location
      query = "select creature_type_id from public.location_creature_types where location_id = {0}"
      list_records = super().get_all(query, id)
      entity.creature_types = super().create_id_list(list_records)
      
      #list_records here contains items in the location
      query = "select item_id from public.location_items where location_id = {0}"
      list_records = super().get_all(query, id)
      entity.items = super().create_id_list(list_records)

      return entity #populated location

    def create_entities(self, list_records):
      dict_records = {}

      number_of_records = len(list_records)
      for record_number in range(number_of_records):
        record = list_records[record_number]
        object = self.create_entity(record)
        dict_records[object.id] = object
      
      return dict_records

    def create_entity(self, record):
      """
      Method to return the instance of a specific location
      """
      object = Location(*record)
      return object
