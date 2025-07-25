import traceback
import psycopg2

from model.LetterModel import Letter
from service.DB.ConnectBD import ConnectBD

class LetterRepository:
    def __init__(self, connectBD: ConnectBD):
        self.connectBD = connectBD

    def insert(self, letter: Letter):
        connection, cursor = None, None
        is_success = False

        try:
            connection, cursor = self.connectBD.open_connect()
            cursor.execute(
                "INSERT INTO letters (message, user_group_id) VALUES (%s, %s)",
                (letter.message, letter.user_group_id)
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

    def delete_by_id(self, letter_id: int):
        connection, cursor = None, None
        is_success = False

        try:
            connection, cursor = self.connectBD.open_connect()
            cursor.execute(
                "DELETE FROM letter WHERE letter_id = %s LIMIT 1",
                letter_id
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
        letters = []

        try:
            connection, cursor = self.connectBD.open_connect()
            cursor.execute("SELECT letter_id, message, user_group_id FROM letters")
            rows = cursor.fetchall()

            for row in rows:
                letter = Letter(row[0], row[1], row[2])
                letters.append(letter)

        except (Exception, psycopg2.Error) as error:
            print(f"Error fetching all letters: {error}")
            traceback.print_exc()

        finally:
            if connection and cursor:
                self.connectBD.close_connection()

        return letters