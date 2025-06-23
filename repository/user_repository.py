import traceback
import psycopg2
from service.connect_BD import ConnectBD

class UserRepository(object):
    def __init__(self, connectBDClass: ConnectBD):
        self.connectBD = connectBDClass

    def insert(self, name, email, passkey):
        connection = self.connectBD.open_connect()
        cursor = None
        is_success = False

        try:
            cursor = connection.cursor()
            cursor.execute(
                "INSERT INTO users (nome, login, senha) VALUES ('{}', '{}', '{}')".format(name, email, passkey)
            )
            connection.commit()

            if cursor.rowcount == 1:
                is_success = True

        except (Exception, psycopg2.Error) as error:
            traceback.print_exc()

        finally:
            if connection:
                cursor.close()
                self.connectBD.close_connection()
        return is_success