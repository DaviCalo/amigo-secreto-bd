from repository.UserRepository import UserRepository
from service.ConnectBD import ConnectBD

class UserService:
    def __init__(self, user_Repository: UserRepository):
        self.user_Repository = user_Repository

    def create_user(self, name, email, passkey):
        return self.user_Repository.insert(name, email, passkey)