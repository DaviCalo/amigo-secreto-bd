import traceback

from model.GiftModel import Gift
from service.DB.ConnectBD import ConnectBD
from service.GiftService import GiftService
from utils.Prints import gift_view

class GiftView:
    def __init__(self, connectBD: ConnectBD):
        self.gift_service = GiftService(connectBD)

    def main_gift_view(self):
        gift_view()
        optional = int(input())
        if optional == 1:
            self.create_gift()
        if optional == 2:
            self.find_all()
        if optional == 0:
            return
        self.main_gift_view()

    def create_gift(self):
        name = input("Digite o nome do presente")

        is_success = None
        try:
            gift = Gift(
                gift_id=None,
                name=gift_name
            )

            is_success = self.gift_service.create_gift(gift)

        except Exception as e:
            traceback.print_exc()

        if is_success:
            print(f"Presente {gift_name} adicionado com sucesso")
        else:
            print(f"Presente {gift_name} não foi criado")


    def find_all(self):
        gifts = []
        try:
            gifts = self.gift_service.find_all()
        except Exception as e:
            traceback.print_exc()

        if gifts:
            for gifts in gifts:
                print(gifts)
            print(f"Foram encontrados {len(gifts)} presentes no total")
            print(f"Presentes: {gifts}")
        else:
            print(f"Não foi encontrado nenhum presente no banco")