import traceback

import psycopg2

from model.UsersGroupModel import UserGroup
from service.DB.ConnectBD import ConnectBD


class UserGroupRepository:
    def __init__(self, connectBD: ConnectBD):
        self.connectBD = connectBD

    def insert(self, userGroup: UserGroup):
        connection, cursor = None, None
        is_success = False

        try:
            connection, cursor = self.connectBD.open_connect()
            cursor.execute(
                "INSERT INTO users_groups (user_id, group_id) VALUES (%s, %s)",
                (userGroup.user_id, userGroup.group_id)
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
            user_group_id = self.find_by_id(users_groups_id).group_id
            cursor.execute(
                "DELETE FROM users_groups WHERE user_group_id = %s",
                (users_groups_id,)
            )
            connection.commit()

            if cursor.rowcount > 0:
                is_success = True
                self.update_recipient_to_none(user_group_id)

        except (Exception, psycopg2.Error) as error:
            traceback.print_exc()

        finally:
            if connection and cursor:
                self.connectBD.close_connection()

        return is_success

    def find_by_id(self, users_groups_id: int) -> UserGroup:
        connection, cursor = None, None
        userGroup = None

        try:
            connection, cursor = self.connectBD.open_connect()
            cursor.execute(
                "SELECT user_group_id, user_id, recipient_user_id, group_id, grift_select_id FROM users_groups WHERE user_group_id = %s",
                (users_groups_id,)
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
            print(f"Error fetching all users_groups: {error}")
            traceback.print_exc()

        finally:
            if connection and cursor:
                self.connectBD.close_connection()

        return userGroup

    def find_all_by_group(self, id_user_group: int) -> list[UserGroup]:
        connection, cursor = None, None
        userGroups = []

        try:
            connection, cursor = self.connectBD.open_connect()
            cursor.execute(
                "SELECT user_group_id, user_id, recipient_user_id, group_id, grift_select_id FROM users_groups WHERE group_id = %s",
                (id_user_group,)
            )
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

    def update_recipient_user_by_user_group_id(self, id_user_group: int, id_recipient_user: int):
        connection, cursor = None, None
        is_success = False

        try:
            connection, cursor = self.connectBD.open_connect()
            cursor.execute(
                "UPDATE users_groups SET recipient_user_id = %s WHERE user_group_id = %s;",
                (id_recipient_user, id_user_group)
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


    def rate_users(self, id_user_group: int):
        userGroups: list[UserGroup] = self.find_all_by_group(id_user_group)

        if not isinstance(userGroups, (list, tuple)):
            userGroups = [userGroups]

        users_info = []
        for user_group_obj in userGroups:
            try:
                user_id = user_group_obj.user_id
                user_group_id = user_group_obj.user_group_id
                users_info.append((user_id, user_group_id))
            except AttributeError as e:
                print(f"Error accessing attributes on UserGroup object: {e}")
                print(f"Object: {user_group_obj}")

        num_users = len(users_info)

        if num_users == 0:
            return False

        for i, (current_user_id, current_user_group_id) in enumerate(users_info):
            next_user_index = (i + 1) % num_users
            recipient_user_id, _ = users_info[next_user_index]

            self.update_recipient_user_by_user_group_id(current_user_group_id, recipient_user_id)

        return True


    def update_recipient_to_none(self, id_group: int):
        connection, cursor = None, None
        is_success = False

        try:
            connection, cursor = self.connectBD.open_connect()
            cursor.execute(
                "UPDATE users_groups SET recipient_user_id = null WHERE group_id = %s;",
                (id_group,)
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

