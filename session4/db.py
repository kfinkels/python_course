import sqlite3


class PetStoreDB:

    @classmethod
    def fetch_all(cls, query):
        with sqlite3.connect('pet_store.sqlite') as conn:
            cursor = conn.cursor()
            cursor.execute(query)
            data = cursor.fetchall()
            return [{'id': item[0], 'name': item[1], 'type': item[2], 'created': item[3]}
                    for item in data]

    @classmethod
    def insert(cls, query):
        with sqlite3.connect('pet_store.sqlite') as conn:
            cursor = conn.cursor()
            cursor.execute(query)
            conn.commit()

    @classmethod
    def init_db(cls):
        with sqlite3.connect('pet_store.sqlite') as conn:
            cursor = conn.cursor()
            cursor.execute(
                '''CREATE TABLE IF NOT EXISTS PETS (
                ID INT PRIMARY KEY NOT NULL,
                NAME TEXT NOT NULL,
                ANIMAL_TYPE TEXT NOT NULL,
                CREATED TEXT NOT NULL);
                '''
            )
            cursor.execute(
                '''INSERT OR IGNORE INTO PETS (
                ID,NAME,ANIMAL_TYPE,CREATED) 
                VALUES (1, 'Humi', 'dog', '01-01-2019');
                '''
            )
            conn.commit()

    @classmethod
    def get_pets(cls, limit, animal_type=None):
        where = f'WHERE ANIMAL_TYPE="{animal_type}"' if animal_type else ''
        query = f'SELECT * FROM PETS {where} limit {limit}'
        return cls.fetch_all(query)
