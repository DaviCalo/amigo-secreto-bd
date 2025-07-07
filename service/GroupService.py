from model.GroupModel import Group
from repository.GroupRepository import GroupRepository
from service.ConnectBD import ConnectBD


class GroupService:
    def __init__(self, connectBD: ConnectBD):
        self.group_repository = GroupRepository(connectBD)

    def create_group(self, group: Group):
        return self.group_repository.insert(group)

    def find_all(self):
        return self.group_repository.find_all()