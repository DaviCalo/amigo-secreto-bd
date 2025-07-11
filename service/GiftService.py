from model.GiftModel import Gift
from repository.GiftRepository import GiftRepository
from service.DB.ConnectBD import ConnectBD


class GiftService:
    def __init__(self, connectBD: ConnectBD):
        self.gift_repository = GiftRepository(connectBD)

    def create_gift(self, gift: Gift):
        return self.gift_repository.insert(gift)

    def find_all(self):
        return self.gift_repository.find_all()

    def find_by_name(self, gift: Gift):
        return self.gift_repository.find_by_name(gift)

    def delete_by_name(self, name: int):
        return self.gift_repository.delete_by_name(name)

    def delete_by_id(self, gift_id: int):
        return self.gift_repository.delete_by_id(gift_id)