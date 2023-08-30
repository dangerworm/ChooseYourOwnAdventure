import psycopg2

class EffectsRepository():
    def __init__(self) -> None:
        self.connection = psycopg2.connect(
            host='localhost', 
            port=5440, 
            dbname='postgres', 
            user='postgres', 
            password='postgres'
        )

        self.connection.autocommit=True

    def get_effects(self):
      with self.connection.cursor() as cursor:
        cursor.execute('select * from effects');
        effects = cursor.fetchall()
        return effects
    