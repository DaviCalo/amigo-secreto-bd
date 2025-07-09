from model.UserModel import User
from repository.UserRepository import UserRepository
from service.DB.ConnectBD import ConnectBD

class UserService:
    def __init__(self, connectBD: ConnectBD):
        self.user_repository = UserRepository(connectBD)

    def create_user(self, user: User):
        return self.user_repository.insert(user)

    def delete_by_name(self, name: str):
        return self.user_repository.delete_by_name(name)

    def find_all(self):
        return self.user_repository.find_all()

    def find_by_id(self, user_id: int):
        return self.user_repository.find_by_id(user_id)

    def update_by_id(self, user):
        return self.user_repository.update_by_id(user)