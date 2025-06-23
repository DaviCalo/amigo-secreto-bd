import os
from service.connect_BD import ConnectBD

class Main:
    def __init__(self, DB_USER, DB_PASSWORD, DB_HOST, DB_PORT, DB_DATABASE):
        self.connect_BD = ConnectBD(
                DB_USER,
                DB_PASSWORD,
                DB_HOST,
                DB_PORT,
                DB_DATABASE
        )

    def run(self):
        print('esta rodando')

if __name__ == '__main__':
    DB_USER = os.getenv('DB_USER_PG')
    DB_PASSWORD = os.getenv('DB_PASSWORD_PG')
    DB_HOST = os.getenv('DB_HOST_PG')
    DB_PORT = os.getenv('DB_PORT_PG')
    DB_DATABASE = os.getenv('DB_DATABASE_PG')
    main = Main(DB_USER, DB_PASSWORD, DB_HOST, DB_PORT, DB_DATABASE)
    main.run()