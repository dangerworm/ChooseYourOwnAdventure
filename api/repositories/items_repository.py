import psycopg2

from repositories.base_repository import BaseRepository
from classes.item import Item

class ItemsRepository(BaseRepository):
    def __init__(self) -> None:
        super().__init__()

    def get_all(self):
      query = "select id, name, description, observations, weight, effects, contains, value, hit_points, attack_points, uses_count from setup.item"
      list_records = super().get_all(query)
      entities = self.create_entities(list_records)

      query = "select item_id, contained_item_id from public.contained_items"
      list_records = super().get_all(query)
      dict_item_to_contained_item_id = super().create_id_dictionary(list_records)
    
      query = "select item_id, effect_id from public.item_effects"
      list_records = super().get_all(query)
      dict_item_to_effect_id = super().create_id_dictionary(list_records)

      for item_id in entities.keys():
        entities[item_id].contained_items = dict_item_to_contained_item_id[item_id]
        entities[item_id].effects = dict_item_to_effect_id[item_id]
      
      return entities

  
    def create_entities(self,list_records):
      dict_records = {}

      number_of_records = len(list_records)
      for record_number in range(number_of_records):
        record = list_records[record_number]
        object = Item(*record)
        dict_records[object.id] = object
      
      return dict_records
