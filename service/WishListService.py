from model.GiftModel import Gift
from model.WishListModel import WishList
from repository.GiftRepository import GiftRepository
from repository.WishListRepository import WishListRepository
from service.DB.ConnectBD import ConnectBD

class WishListService:
    def __init__(self, connectBD: ConnectBD):
        self.wish_list_repository = WishListRepository(connectBD)
        self.gift_repository= GiftRepository(connectBD)

    def create_wish_list(self, wish_list: WishList, gift: Gift):
        is_gift = self.gift_repository.insert(gift)

        if is_gift:
            gift_id = self.gift_repository.find_by_name(gift.name).gift_id
            wish_list.gift_id = gift_id
            return self.wish_list_repository.insert(wish_list)
        else:
            return False

    def find_all(self):
        return self.wish_list_repository.find_all()

    def delete_by_id(self, wish_list_id: int):
        gift_id = self.find_by_id(wish_list_id).gift_id
        if gift_id:
            return self.gift_repository.delete_by_id(gift_id)
        else:
            return False

    def find_by_id(self, wish_list_id: int):
        return self.wish_list_repository.find_by_id(wish_list_id)

    def find_by_user_group_id(self, user_group_id: int):
        return self.wish_list_repository.find_by_user_group_id(user_group_id)

    def find_all_gifts_by_user_group(self, user_group_id: int):
        if self.find_by_user_group_id(user_group_id):
            return self.wish_list_repository.find_all_gifts_by_user_group(user_group_id)
        else:
            raise Exception("Não existe esse id")