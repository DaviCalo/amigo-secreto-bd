from service.DB.ConnectBD import ConnectBD
from utils.Prints import origin_view
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
        origin_view()
        option = int(input())
        if option == 1:
            self.user_view.main_user_view()
        if option == 2:
            self.group_view.main_group_view()
        if option == 3:
            self.user_group_view.main_user_group_view()
        if option == 4:
            self.wish_list_view.main_wish_list_view()
        if option == 5:
            self.gift_view.main_gift_view()
        if option == 6:
            self.letter_view.main_letter_view()
        if option == 0:
            return
        self.run()
