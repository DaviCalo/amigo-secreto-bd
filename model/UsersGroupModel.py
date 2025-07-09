class UserGroup:
    def __init__(self, user_group_id, user_id, recipient_user_id, group_id, grift_select_id):
        self._user_group_id = user_group_id
        self._user_id = user_id
        self._recipient_user_id = recipient_user_id
        self._group_id = group_id
        self._grift_select_id = grift_select_id

    @property
    def user_group_id(self):
        return self._user_group_id

    @user_group_id.setter
    def user_group_id(self, user_group_id):
        self._user_group_id = user_group_id

    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        self._user_id = user_id

    @property
    def recipient_user_id(self):
        return self._recipient_user_id

    @recipient_user_id.setter
    def recipient_user_id(self, recipient_user_id):
        self._recipient_user_id = recipient_user_id

    @property
    def group_id(self):
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        self._group_id = group_id

    @property
    def grift_select_id(self):
        return self._grift_select_id

    @grift_select_id.setter
    def grift_select_id(self, grift_select_id):
        self._grift_select_id = grift_select_id

    def __str__(self):
        return (f"UsersGroup ID: {self.user_group_id}\n"
                f"  User id: {self.user_id}\n"
                f"  Recipient user id: {self.recipient_user_id}\n"
                f"  Group id: {self.group_id}\n"
                f"  Grift Select id: {self.grift_select_id}\n")