from model.GroupModel import Group
from repository.GroupRepository import GroupRepository
from service.DB.ConnectBD import ConnectBD

class GroupService:
    def __init__(self, connectBD: ConnectBD):
        self.group_repository = GroupRepository(connectBD)

    def create_group(self, group: Group):
        return self.group_repository.insert(group)

    def find_all(self):
        return self.group_repository.find_all()

    def update_by_id(self, group: Group):
        return self.group_repository.update_by_id(group)

    def delete_by_id(self, group_id: int):
        return self.group_repository.delete_by_id(group_id)