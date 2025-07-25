class WishList:
    def __init__(self, wish_list_id, user_group_id, gift_id):
        self._wish_list_id = wish_list_id
        self._user_group_id = user_group_id
        self._gift_id = gift_id

    @property
    def wish_list_id(self):
        return self._wish_list_id

    @wish_list_id.setter
    def wish_list_id(self, wish_list_id):
        self._wish_list_id = wish_list_id

    @property
    def user_group_id(self):
        return self._user_group_id

    @user_group_id.setter
    def user_group_id(self, user_group_id):
        self._user_group_id = user_group_id

    @property
    def gift_id(self):
        return self._gift_id

    @gift_id.setter
    def gift_id(self, gift_id):
        self._gift_id = gift_id

    def __str__(self):
        return (f"Gift ID: {self.wish_list_id}\n"
                    f"  User group id: {self.user_group_id}\n"
                    f"  Gift id: {self.gift_id}\n")