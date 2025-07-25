import traceback
import psycopg2

from model.UserModel import User
from service.DB.ConnectBD import ConnectBD

class UserRepository:
    def __init__(self, connectBD: ConnectBD):
        self.connectBD = connectBD

    def insert(self, user: User):
        connection, cursor = None, None
        is_success = False

        try:
            connection, cursor = self.connectBD.open_connect()
            cursor.execute(
                "INSERT INTO users (name, email, passkey) VALUES (%s, %s, %s);",
                (user.name, user.email, user.passkey,)
            )
            connection.commit()

            if cursor.rowcount == 1:
                is_success = True

        except (Exception, psycopg2.Error) as error:
            traceback.print_exc()

        finally:
            if connection and cursor:
                self.connectBD.close_connection()

        return is_success


    def delete_by_name(self, name: str):
        connection, cursor = None, None
        is_success = False

        try:
            connection, cursor = self.connectBD.open_connect()
            cursor.execute(
                "DELETE FROM users AS u WHERE u.name = %s",
                (name,)
            )
            connection.commit()

            if cursor.rowcount > 0:
                is_success = True

        except (Exception, psycopg2.Error) as error:
            traceback.print_exc()

        finally:
            if connection and cursor:
                self.connectBD.close_connection()

        return is_success


    def find_all(self):
        connection, cursor = None, None
        users = []

        try:
            connection, cursor = self.connectBD.open_connect()
            sql_select_all_query = "SELECT user_id, name, email, passkey FROM users;"
            cursor.execute(sql_select_all_query)
            rows = cursor.fetchall()

            for row in rows:
                user = User(row[0], row[1], row[2], row[3])
                users.append(user)

        except (Exception, psycopg2.Error) as error:
            print(f"Error fetching all users: {error}")
            traceback.print_exc()

        finally:
            if connection and cursor:
                self.connectBD.close_connection()

        return users


    def find_by_id(self, user_id: int):
        connection, cursor = None, None
        user = None

        try:
            connection, cursor  = self.connectBD.open_connect()
            cursor.execute(
                "SELECT user_id, name, email, passkey FROM users WHERE user_id = %s;",
                (user_id,)
            )
            row = cursor.fetchone()

            if row:
                user = User(row[0], row[1], row[2], row[3])

        except (Exception, psycopg2.Error) as error:
            print(f"Error fetching user: {error}")
            traceback.print_exc()

        finally:
            if connection and cursor:
                self.connectBD.close_connection()

        return user

    def find_by_name(self, name: str):
        connection, cursor = None, None
        user = None

        try:
            connection, cursor = self.connectBD.open_connect()
            cursor.execute(
                "SELECT user_id, name, email, passkey FROM users WHERE name = %s;",
                (name,)
            )
            row = cursor.fetchone()

            if row:
                user = User(row[0], row[1], row[2], row[3])

        except (Exception, psycopg2.Error) as error:
            print(f"Error fetching user: {error}")
            traceback.print_exc()

        finally:
            if connection and cursor:
                self.connectBD.close_connection()

        return user

    def update_by_id(self, user: User):
        connection, cursor = None, None
        is_success = False

        try:
            connection, cursor = self.connectBD.open_connect()
            cursor.execute(
                "UPDATE users SET name = %s, email = %s, passkey = %s WHERE user_id = %s;",
                (user.name, user.email, user.passkey, user.user_id,)
            )
            connection.commit()

            if cursor.rowcount > 0:
                is_success = True

        except (Exception, psycopg2.Error) as error:
            traceback.print_exc()

        finally:
            if connection and cursor:
                self.connectBD.close_connection()

        return is_success