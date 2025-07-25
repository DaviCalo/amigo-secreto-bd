from service.DB.ConnectBD import ConnectBD
from utils.Prints import origin_view, invalid_option, exit_program
from view.GroupView import GroupView
from view.UserGroupView import UserGroupView
from view.UserView import UserView
from view.WishListView import WishListView
from view.GiftView import GiftView
from view.LetterView import LetterView

class MainView:
    def __init__(self, connectBD: ConnectBD):
        self.user_view = UserView(connectBD)
        self.group_view = GroupView(connectBD)
        self.user_group_view = UserGroupView(connectBD)
        self.wish_list_view = WishListView(connectBD)
        self.gift_view = GiftView(connectBD)
        self.letter_view = LetterView(connectBD)

    def run(self):
        try:
            origin_view()
            option = int(input())
            if option == 1:
                self.user_view.main_user_view()
            elif option == 2:
                self.wish_list_view.main_wish_list_view()
            elif option == 3:
                self.gift_view.main_gift_view()
            elif option == 4:
                self.group_view.main_group_view()
            elif option == 5:
                self.user_group_view.main_user_group_view()
            elif option == 6:
                self.letter_view.main_letter_view()
            elif option == 0:
                exit_program()
                return
            else:
                raise ValueError
        except ValueError:
            invalid_option()
        self.run()
