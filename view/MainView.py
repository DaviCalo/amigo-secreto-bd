from repository.UserRepository import UserRepository
from service.ConnectBD import ConnectBD
from service.UserService import UserService
from utils.Mainprint import origin_view
from view.UserView import UserView

class MainView:
    def __init__(self, connectBD: ConnectBD):
        self.connect_BD = connectBD
        self.user_repository = UserRepository(self.connect_BD)
        self.user_service = UserService(self.user_repository)
        self.user_view = UserView(self.user_service)

    def run(self):
        origin_view()
        option = int(input())
        if option == 1:
            self.user_view.main_user_view()
        if option == 0:
            return
        self.run()
