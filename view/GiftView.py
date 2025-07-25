import traceback

from model.GiftModel import Gift
from service.DB.ConnectBD import ConnectBD
from service.GiftService import GiftService
from utils.Prints import gift_view, invalid_option


class GiftView:
    def __init__(self, connectBD: ConnectBD):
        self.gift_service = GiftService(connectBD)

    def main_gift_view(self):
        try:
            gift_view()
            optional = int(input())
            if optional == 1:
                self.create_gift()
            elif optional == 2:
                self.find_all()
            elif optional == 0:
                return
            else:
                raise ValueError
        except ValueError:
            invalid_option()
        self.main_gift_view()

    def create_gift(self):
        gift_name = input("Digite o nome do presente")

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
            print(f"Foram encontrados {len(gifts)} presentes no total")
            for gifts in gifts:
                print(gifts)
        else:
            print(f"Não foi encontrado nenhum presente no banco")