import traceback

import psycopg2

from dto.WishListWithGifts import WishListWithGifts
from model.WishListModel import WishList
from service.DB.ConnectBD import ConnectBD

class WishListRepository:
    def __init__(self, connectBD: ConnectBD):
        self.connectBD = connectBD

    def insert(self, wish_list: WishList):
        connection, cursor = None, None
        is_success = False

        try:
            connection, cursor = self.connectBD.open_connect()
            cursor.execute(
                "INSERT INTO wish_list (user_group_id, gift_id) VALUES (%s, %s)",
                (wish_list.user_group_id, wish_list.gift_id)
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
        WishLists = []

        try:
            connection, cursor = self.connectBD.open_connect()
            cursor.execute("SELECT wish_list_id, user_group_id, gift_id FROM wish_list")
            rows = cursor.fetchall()

            for row in rows:
                WishListRow = WishList(
                    wish_list_id=row[0], user_group_id=row[1], gift_id=row[2]
                )
                WishLists.append(WishListRow)

        except (Exception, psycopg2.Error) as error:
            print(f"Error fetching all users: {error}")
            traceback.print_exc()

        finally:
            if connection and cursor:
                self.connectBD.close_connection()

        return WishLists


    def delete_by_id(self, wish_list_id: int):
        connection, cursor = None, None
        is_success = False

        try:
            connection, cursor = self.connectBD.open_connect()
            cursor.execute(
                "DELETE FROM wish_list WHERE wish_list_id = %s",
                (wish_list_id,)
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

    def find_by_id(self, wish_list_id: str):
        connection, cursor = None, None
        WishListRow = None

        try:
            connection, cursor = self.connectBD.open_connect()
            cursor.execute(
                "SELECT wish_list_id, user_group_id, gift_id FROM wish_list WHERE wish_list_id = %s",
                (wish_list_id,)
           )
            row = cursor.fetchone()

            if row:
                WishListRow = WishList(
                    wish_list_id=row[0], user_group_id=row[1], gift_id=row[2]
                )

        except (Exception, psycopg2.Error) as error:
            print(f"Error fetching all groups: {error}")
            traceback.print_exc()

        finally:
            if connection and cursor:
                self.connectBD.close_connection()

        return WishListRow

    def find_by_user_group_id(self, user_group_id: int):
        connection, cursor = None, None
        isExist = False

        try:
            connection, cursor = self.connectBD.open_connect()
            cursor.execute(
                "SELECT * FROM wish_list WHERE user_group_id = %s",
                (user_group_id,)
            )
            row = cursor.fetchone()

            if row:
                isExist = True

        except (Exception, psycopg2.Error) as error:
            print(f"Error fetching all groups: {error}")
            traceback.print_exc()

        finally:
            if connection and cursor:
                self.connectBD.close_connection()

        return isExist

    def find_all_gifts_by_user_group(self, user_group_id: int) -> list[WishListWithGifts] | None:
        connection, cursor = None, None
        WishLists = []

        try:
            connection, cursor = self.connectBD.open_connect()
            cursor.execute(
                "SELECT wl.wish_list_id, wl.user_group_id, wl.gift_id, g.gift_name FROM wish_list AS wl, gifts AS g WHERE wl.user_group_id = %s AND g.gift_id = wl.gift_id",
                (user_group_id,)
           )
            rows = cursor.fetchall()

            for row in rows:
                WishListRow = WishListWithGifts(
                    wish_list_id=row[0], user_group_id=row[1], gift_id=row[2], name_gift=row[3]
                )
                WishLists.append(WishListRow)

        except (Exception, psycopg2.Error) as error:
            print(f"Error fetching all groups: {error}")
            traceback.print_exc()

        finally:
            if connection and cursor:
                self.connectBD.close_connection()

        return WishLists