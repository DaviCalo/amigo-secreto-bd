import traceback
import psycopg2

from model.GiftModel import Gift
from service.ConnectBD import ConnectBD

class GiftRepository:
    def __init__(self, connectBD: ConnectBD):
        self.connectBD = connectBD

    def insert(self, name):
        connection, cursor = None, None
        is_success = False

        try:
            connection, cursor = self.connectBD.open_connect()
            cursor.execute(
                "INSERT INTO gifts (name) VALUES ('{}')".format(name)
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

    def delete_by_name(self, name):
        connection, cursor = None, None
        is_success = False

        try:
            connection, cursor = self.connectBD.open_connect()
            cursor.execute(
                "DELETE FROM gift WHERE nome = {} LIMIT 1".format(name)
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
        gifts = []

        try:
            connection, cursor = self.connectBD.open_connect()
            cursor.execute("SELECT gift_id, name FROM gifts")
            rows = cursor.fetchall()

            for row in rows:
                gift = Gift(row[0], row[1])
                gifts.append(gift)

        except (Exception, psycopg2.Error) as error:
            print(f"Error fetching all gifts: {error}")
            traceback.print_exc()

        finally:
            if connection and cursor:
                self.connectBD.close_connection()

        return gifts