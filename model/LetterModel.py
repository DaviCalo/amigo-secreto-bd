class Letter:
    def __init__(self, letter_id, message, user_group_id):
        self._letter_id = letter_id
        self._message = message
        self._user_group_id = user_group_id

    @property
    def letter_id(self):
        return self._letter_id

    @letter_id.setter
    def letter_id(self, letter_id):
        self._letter_id = letter_id

    @property
    def message(self):
        return self._message

    @message.setter
    def message(self, message):
        self._message = message

    @property
    def user_group_id(self):
        return self._user_group_id

    @user_group_id.setter
    def user_group_id(self, user_group_id):
        self._user_group_id = user_group_id

    def __str__(self):
        return (f"Letter ID: {self.letter_id}\n"
                f"  Message: {self.message}\n"
                f"  User Group ID: {self.user_group_id}\n")