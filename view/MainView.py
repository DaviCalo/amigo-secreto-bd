from repository.UserRepository import UserRepository
from service.ConnectBD import ConnectBD
from service.UserService import UserService
from utils.Prints import origin_view
from view.GroupView import GroupView
from view.UserView import UserView

class MainView:
    def __init__(self, connectBD: ConnectBD):
        self.user_view = UserView(connectBD)
        self.group_view = GroupView(connectBD)

    def run(self):
        origin_view()
        option = int(input())
        if option == 1:
            self.user_view.main_user_view()
        if option == 2:
            self.group_view.main_group_view()
        if option == 0:
            return
        self.run()
