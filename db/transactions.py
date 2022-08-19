import sqlite3

from configs.constants import DB_PATH


class Transactions:
    def __init__(self, db_path=DB_PATH):
        self.db_path = db_path
        self.connection = sqlite3.Connection(DB_PATH)
        self.cursor = self.connection.cursor()

    @property
    def _connection(self):
        return sqlite3.connect(self.db_path)

    def execute(self, sql: str, parameters: tuple = None, fetchone=False, fetchall=False, commit=False):
        connection=self
