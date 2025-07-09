import traceback

import psycopg2

from model.UsersGroupModel import UserGroup
from service.ConnectBD import ConnectBD


class UserGroupRepository:
    def __init__(self, connectBD: ConnectBD):
        self.connectBD = connectBD

    def insert(self, userGroup: UserGroup):
        connection, cursor = None, None
        is_success = False

        try:
            connection, cursor = self.connectBD.open_connect()
            cursor.execute(
                "INSERT INTO users_groups (user_id, recipient_user_id, group_id, grift_select_id) VALUES (%s, %s, %s, %s)",
                (userGroup.user_id, userGroup.recipient_user_id, userGroup.group_id, userGroup.grift_select_id)
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
        userGroups = []

        try:
            connection, cursor = self.connectBD.open_connect()
            cursor.execute("SELECT user_group_id, user_id, recipient_user_id, group_id, grift_select_id FROM users_groups")
            rows = cursor.fetchall()

            for row in rows:
                userGroup = UserGroup(
                    user_group_id = row[0], user_id = row[1], recipient_user_id = row[2], group_id = row[3], grift_select_id = row[4]
                )
                userGroups.append(userGroup)

        except (Exception, psycopg2.Error) as error:
            print(f"Error fetching all users: {error}")
            traceback.print_exc()

        finally:
            if connection and cursor:
                self.connectBD.close_connection()

        return userGroups


    def update_by_id(self, userGroup: UserGroup):
        connection, cursor = None, None
        is_success = False

        try:
            connection, cursor = self.connectBD.open_connect()
            cursor.execute(
                "UPDATE users_groups SET user_id = %s, recipient_user_id = %s, group_id = %s, grift_select_id = %s WHERE user_group_id = %s;",
                (userGroup.user_id, userGroup.recipient_user_id, userGroup.group_id, userGroup.grift_select_id, userGroup.user_group_id)
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

    def delete_by_id(self, users_groups_id: int):
        connection, cursor = None, None
        is_success = False

        try:
            connection, cursor = self.connectBD.open_connect()
            cursor.execute(
                "DELETE FROM users_groups WHERE user_group_id = %s",
                (users_groups_id,)
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

    def find_by_id(self, users_groups_id: int):
        connection, cursor = None, None
        userGroup = None

        try:
            connection, cursor = self.connectBD.open_connect()
            cursor.execute(
                "SELECT user_group_id, user_id, recipient_user_id, group_id, grift_select_id FROM users_groups WHERE user_group_id = %s",
                users_groups_id
           )
            row = cursor.fetchone()

            if row:
                userGroup = UserGroup(
                    user_group_id=row[0],
                    user_id=row[1],
                    recipient_user_id=row[2],
                    group_id=row[3],
                    grift_select_id=row[4]
                )

        except (Exception, psycopg2.Error) as error:
            print(f"Error fetching all users: {error}")
            traceback.print_exc()

        finally:
            if connection and cursor:
                self.connectBD.close_connection()

        return userGroup