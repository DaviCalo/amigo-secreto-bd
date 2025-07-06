import traceback

import psycopg2

from model.GroupModel import Group
from service.ConnectBD import ConnectBD

class GroupRepository:
    def __init__(self, connectBD: ConnectBD):
        self.connectBD = connectBD

    def insert(self, name, description, status_group, maximum_value, minimum_value, draw_date, meet_date, location, created_user_id):
        connection = self.connectBD.open_connect()
        cursor = None
        is_success = False

        try:
            cursor = connection.cursor()
            cursor.execute(
                "INSERT INTO groups (name, description, status_group, maximum_value, minimum_value, draw_date, meet_date, location, created_user_id) VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(name, description, status_group, maximum_value, minimum_value, draw_date, meet_date, location, created_user_id)
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

    def find_all(self):
        connection = None
        cursor = None
        groups = []

        try:
            connection = self.connectBD.open_connect()
            cursor = connection.cursor()

            sql_select_all_query = "SELECT name, description, status_group, maximum_value, minimum_value, draw_date, meet_date, location, created_user_id, group_id FROM groups"
            cursor.execute(sql_select_all_query)
            rows = cursor.fetchall()

            for row in rows:
                group = Group(
                    name=row[0],
                    description=row[1],
                    status_group=row[2],
                    maximum_value=row[3],
                    minimum_value=row[4],
                    draw_date=row[5],
                    meet_date=row[6],
                    location=row[7],
                    created_user_id=row[8],
                    group_id=row[9]
                )
                groups.append(group)

        except (Exception, psycopg2.Error) as error:
            print(f"Error fetching all users: {error}")
            traceback.print_exc()

        finally:
            if cursor:
                cursor.close()
            if connection:
                self.connectBD.close_connection()

        return groups