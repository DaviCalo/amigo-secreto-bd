from repository.GroupRepository import GroupRepository
from service.ConnectBD import ConnectBD


class GroupService:
    def __init__(self, connectBD: ConnectBD):
        self.group_repository = GroupRepository(connectBD)

    def create_group(self, name, description, status_group, maximum_value, minimum_value, draw_date, meet_date, location, created_user_id):
        return self.group_repository.insert(name, description, status_group, maximum_value, minimum_value, draw_date, meet_date, location, created_user_id)

    def find_all(self):
        return self.group_repository.find_all()