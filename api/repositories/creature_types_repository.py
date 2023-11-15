from repositories.base_repository import BaseRepository
from classes.creature_type import CreatureType

class CreatureTypesRepository(BaseRepository):
    def __init__(self) -> None:
        super().__init__()

    def get_all(self):
      query = "select id, name, description, observations, time_probabilities, hit_points_range, agility_range, charisma_range, endurance_range, intelligence_range, mana_range, perception_range, strength_range from setup.creature_types"
      list_records = super().get_all(query)
      entities = self.create_entities(list_records)

      query = "select creature_type_id, damage_type_id from setup.creature_type_immunities"
      list_records = super().get_all(query)
      dict_creature_type_to_immunity_id = super().create_id_dictionary(list_records)
    
      query = "select creature_type_id, damage_type_id from setup.creature_type_resistances"
      list_records = super().get_all(query)
      dict_creature_type_to_resistance_id = super().create_id_dictionary(list_records)
    
      query = "select creature_type_id, damage_type_id from setup.creature_type_weaknesses"
      list_records = super().get_all(query)
      dict_creature_type_to_weakness_id = super().create_id_dictionary(list_records)

      for creature_type_id in dict_creature_type_to_immunity_id.keys():
        entities[creature_type_id].immunities = dict_creature_type_to_immunity_id[creature_type_id]

      for creature_type_id in dict_creature_type_to_resistance_id.keys():
        entities[creature_type_id].resistances = dict_creature_type_to_resistance_id[creature_type_id]
      
      for creature_type_id in dict_creature_type_to_weakness_id.keys():
        entities[creature_type_id].weaknesses = dict_creature_type_to_weakness_id[creature_type_id]

      return entities

    def create_entities(self,list_records):
      dict_records = {}

      number_of_records = len(list_records)
      for record_number in range(number_of_records):
        record = list_records[record_number]
        object = CreatureType(*record)
        dict_records[object.id] = object
      
      return dict_records
    