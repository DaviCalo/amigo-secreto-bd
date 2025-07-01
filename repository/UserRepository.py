import traceback
import psycopg2
from service.ConnectBD import ConnectBD

class UserRepository:
    def __init__(self, connectBDClass: ConnectBD):
        self.connectBD = connectBDClass

    def insert(self, name, email, passkey):
        connection = self.connectBD.open_connect()
        cursor = None
        is_success = False

        try:
            cursor = connection.cursor()
            cursor.execute(
                "INSERT INTO users (name, email, passkey) VALUES ('{}', '{}', '{}')".format(name, email, passkey)
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

    def delete_by_name(self, name):
        connection = self.connectBD.open_connect()
        cursor = None
        is_success = False

        try:
            cursor = connection.cursor()
            cursor.execute(
                "DELETE FROM users WHERE nome = {} LIMIT 1".format(name)
            )
            connection.commit()

            if cursor.rowcount > 0:
                is_success = True

        except (Exception, psycopg2.Error) as error:
            traceback.print_exc()

        finally:
            if connection:
                cursor.close()
                self.connectBD.close_connection()

        return is_success

    def find_all(self):
        connection = None
        cursor = None
        users = []

        try:
            connection = self.connectBD.open_connect()
            cursor = connection.cursor()

            sql_select_all_query = "SELECT id, name, email, passkey FROM users"
            cursor.execute(sql_select_all_query)
            rows = cursor.fetchall()

            for row in rows:
                user = {
                    "id": row[0],
                    "name": row[1],
                    "email": row[2],
                    "passkey": row[3]
                }
                users.append(user)

        except (Exception, psycopg2.Error) as error:
            print(f"Error fetching all users: {error}")
            traceback.print_exc()

        finally:
            if cursor:
                cursor.close()
            if connection:
                self.connectBD.close_connection()

        return users