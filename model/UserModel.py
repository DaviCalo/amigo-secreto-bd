class User:
    def __init__(self, user_id, name, email, passkey):
        self._user_id = user_id
        self._name = name
        self._email = email
        self._passkey = passkey

    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        self._user_id = user_id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        self._email = email

    @property
    def passkey(self):
        return self._passkey

    @passkey.setter
    def passkey(self, passkey):
        self._passkey = passkey

    def __str__(self):
        return (f"User ID: {self.user_id}\n"
                f"  Name: {self.name}\n"
                f"  Email: {self.email}\n"
                f"  Passkey: {self.passkey}\n")