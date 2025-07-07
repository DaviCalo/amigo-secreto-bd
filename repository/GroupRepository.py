import traceback

import psycopg2

from model.GroupModel import Group
from service.ConnectBD import ConnectBD

class GroupRepository:
    def __init__(self, connectBD: ConnectBD):
        self.connectBD = connectBD

    def insert(self, group: Group):
        connection, cursor = None, None
        is_success = False

        try:
            connection, cursor = self.connectBD.open_connect()
            cursor.execute(
                "INSERT INTO groups (name, description, status_group, maximum_value, minimum_value, draw_date, meet_date, location, created_user_id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)",
                (group.name, group.description, group.status_group, group.maximum_value, group.minimum_value, group.draw_date, group.meet_date, group.location, group.created_user_id)
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


    def find_all(self):
        connection, cursor = None, None
        groups = []

        try:
            connection, cursor = self.connectBD.open_connect()
            cursor.execute("SELECT name, description, status_group, maximum_value, minimum_value, draw_date, meet_date, location, created_user_id, group_id FROM groups")
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
            if connection and cursor:
                self.connectBD.close_connection()

        return groups


    def update_by_id(self, group: Group):
        connection, cursor = None, None
        is_success = False

        try:
            connection, cursor = self.connectBD.open_connect()
            cursor.execute(
                "UPDATE groups SET name = %s, description = %s, status_group = %s, maximum_value = %s, minimum_value = %s, draw_date = %s, meet_date = %s, location = %s WHERE group_id = %s;",
                (group.group_id, group.description, group.status_group, group.maximum_value, group.minimum_value, group.draw_date, group.meet_date, group.location, group.group_id)
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