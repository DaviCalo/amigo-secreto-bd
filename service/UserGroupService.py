from model.UsersGroupModel import UserGroup
from repository.UserGroupRepository import UserGroupRepository
from service.DB.ConnectBD import ConnectBD

class UserGroupService:
    def __init__(self, connectBD: ConnectBD):
        self.userGroup_repository = UserGroupRepository(connectBD)

    def create_user_group(self, userGroup: UserGroup):
        return self.userGroup_repository.insert(userGroup)

    def find_all(self):
        return self.userGroup_repository.find_all()

    def rate_users(self, id_user_group: int):
        return self.userGroup_repository.rate_users(id_user_group)

    def delete_by_id(self, user_group_id: int):
        return self.userGroup_repository.delete_by_id(user_group_id)