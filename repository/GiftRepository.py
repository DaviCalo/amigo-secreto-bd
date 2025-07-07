import traceback
import psycopg2


class GiftRepository:
    def __init__(self, connectBD: ConnectBD):
        self.connectBD = connectBD

    def insert(self, name):
        connection = self.connectBD.open_connect()
        cursor = None
        is_success = False

        try:
            cursor = connection.cursor()
            cursor.execute(
                "INSERT INTO gifts (name) VALUES ('{}')".format(name)
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
                "DELETE FROM gift WHERE nome = {} LIMIT 1".format(name)
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
        gifts = []

        try:
            connection = self.connectBD.open_connect()
            cursor = connection.cursor()

            sql_select_all_query = "SELECT gift_id, name FROM gift"
            cursor.execute(sql_select_all_query)
            rows = cursor.fetchall()

            for row in rows:
                gift = {
                    "id": row[0],
                    "name": row[1],
                }
                gifts.append(gift)

        except (Exception, psycopg2.Error) as error:
            print(f"Error fetching all gifts: {error}")
            traceback.print_exc()

        finally:
            if cursor:
                cursor.close()
            if connection:
                self.connectBD.close_connection()

        return gifts