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
  