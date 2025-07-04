from repository.UserRepository import UserRepository
from service.ConnectBD import ConnectBD

class UserService:
    def __init__(self, connectBD: ConnectBD):
        self.user_repository = UserRepository(connectBD)

    def create_user(self, name, email, passkey):
        return self.user_repository.insert(name, email, passkey)

    def delete_by_name(self, name):
        return self.user_repository.delete_by_name(name)

    def find_all(self):
        return self.user_repository.find_all()