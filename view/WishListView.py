import traceback

from model.GiftModel import Gift
from model.GroupModel import Group
from model.WishListModel import WishList
from service.DB.ConnectBD import ConnectBD
from service.WishListService import WishListService
from utils.Prints import group_view, wish_list_view, invalid_option


class WishListView:
    def __init__(self, connectBD: ConnectBD):
        self.wish_list_service = WishListService(connectBD)

    def main_wish_list_view(self):
        try:
            wish_list_view()
            optional = int(input())
            if optional == 1:
                self.create_wish_list()
            elif optional == 2:
                self.delete_by_id()
            elif optional == 3:
                self.find_all_gifts_by_user_group()
            elif optional == 0:
                return
            else:
                raise ValueError
        except ValueError:
            invalid_option()
        self.main_wish_list_view()

    def create_wish_list(self):
        user_group_id = int(input("Digite o id de um user_group:"))
        gift_name = input("Digite o nome do presente que deseja receber:")

        is_success = None
        try:
            gift = Gift(
                gift_id=None,
                name=gift_name
            )

            wish_list = WishList(
                wish_list_id=None,
                user_group_id=user_group_id,
                gift_id=None
            )

            is_success = self.wish_list_service.create_wish_list(wish_list, gift)

        except Exception as e:
            traceback.print_exc()

        if is_success:
            print(f"Presente {gift_name} adicionado com sucesso")
        else:
            print(f"Presente {gift_name} não foi criado")


    def find_all(self):
        wish_list = []
        try:
            wish_list = self.wish_list_service.find_all()
        except Exception as e:
            traceback.print_exc()

        if wish_list:
            for wish_list in wish_list:
                print(wish_list)
            print(f"Foram encontradas {len(wish_list)} listas de desejos")
        else:
            print(f"Não foi encontrado nenhuma lista de desejos no banco")


    def delete_by_id(self):
        id_wish_list = int(input("Digite o id da lista de desejos que deseja remover o presente:"))
        is_success = None

        try:
            is_success = self.wish_list_service.delete_by_id(id_wish_list)
        except Exception as e:
            traceback.print_exc()

        if is_success:
            print(f"Presente deletado com sucesso da lista de desejos")
        else:
            print(f"Erro ao deletar o presente")

    def find_all_gifts_by_user_group(self):
        id_wish_list = int(input("Digite o id do user group que deseja ver os presentes:"))
        wish_list = []

        try:
            wish_list = self.wish_list_service.find_all_gifts_by_user_group(id_wish_list)
        except Exception as e:
            traceback.print_exc()

        if wish_list:
            for wish_list in wish_list:
                print(wish_list)

            print(f"Foram encontradas os presentes nessa lista")
        else:
            print(f"Não foi encontrado nenhuma lista de desejos no banco")