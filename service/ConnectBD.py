import psycopg2
from psycopg2 import sql
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

class ConnectBD:
    def __init__(self, user, password, host, port, database):
        self._user = user
        self._password = password
        self._host = host
        self._port = port
        self._database = database
        self._connection = None
        self._cursor = None

    def open_connect(self):
        self._connection = psycopg2.connect(user=self._user, password=self._password,
                                           host=self._host, port=self._port, database=self._database)
        self._cursor = self._connection.cursor()
        return self._connection, self._cursor

    def close_connection(self):
        self._connection.close()
        self._cursor.close()

    def create_connect(self):
        self._connection = psycopg2.connect(user=self._user, password=self._password,
                                           host=self._host, port=self._port)
        return self._connection