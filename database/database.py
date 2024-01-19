import sqlite3
from sql_queries import create_table

class Database:
    def __int__(self):
        self.connect = sqlite3.connect("db.sqlite3")
        self.cursor = self.connect.cursor()

    def sql_create_tables(self):
        if self.connect:
            print("Successfully connected")
        self.connect.execute(create_table.CREATE_USER_TABLE)

        self.connect.commit()