import psycopg2

class BaseRepository():
  def __init__(self) -> None:
    self.connection = psycopg2.connect(
        host='localhost', 
        port=5440, 
        dbname='postgres', 
        user='postgres', 
        password='postgres'
    )


  def get_all(self, query):
      """
      Method to get the data from the table named table_name in the database.
      """
      with self.connection.cursor() as cursor:
        cursor.execute(query)
        records = cursor.fetchall()
        return records
      
  def get_by_id(self, query, id):
      """
      Method to get specific records from a table based on the id.
      """
      with self.connection.cursor() as cursor:
        cursor.execute(query, id)
        records = cursor.fetchall()
        return records
  
  def create_id_dictionary(self, list_records):
      """
      method to take in a list of lists, and convert this to a dictionary.
      key = entity_id
      values = list of IDs
      """

      dict_entity_to_id = {}
      number_of_records = len(list_records)
      for record_number in range(number_of_records):
        record = list_records[record_number]
        entity_id, id = record[:2]

        if not entity_id in dict_entity_to_id.keys():
          dict_entity_to_id[entity_id] = []

        dict_entity_to_id[entity_id].append(id)
    
      return dict_entity_to_id
  
  def create_id_count_dictionary(self, list_records):
      """
      method to take in a list of lists, and convert this to a dictionary.
      key = entity_id
      values = list of IDs
      """

      dict_entity_to_id_with_count = {}
      number_of_records = len(list_records)
      for record_number in range(number_of_records):
        record = list_records[record_number]
        entity_id, id, count = record[:3]

        if not entity_id in dict_entity_to_id_with_count.keys():
          dict_entity_to_id_with_count[entity_id] = {}

        dict_entity_to_id_with_count[entity_id][id] = count
    
      return dict_entity_to_id_with_count
  
  def create_id_list(self, list_records):
     """
     Method to create a list of all id's rather than a list of lists
     """
     return [record[0] for record in list_records]