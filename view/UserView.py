import traceback

from service.ConnectBD import ConnectBD
from service.UserService import UserService
from utils.Mainprint import user_view

class UserView:
    def __init__(self, connectBD: ConnectBD):
        self.user_service = UserService(connectBD)

    def main_user_view(self):
        user_view()
        optional = int(input())
        if optional == 1:
            self.create_user()
        if optional == 2:
            self.delete_by_name()
        if optional == 3:
            self.find_all()
        if optional == 0:
            return
        self.main_user_view()

    def create_user(self):
        name_user = input("Digite o nome do usuário:")
        email_user = input("Digite o email do usuário:")
        passkey_user = input("Digite a senha do usuário:")
        is_success = None
        try:
            is_success = self.user_service.create_user(name_user, email_user, passkey_user)
        except Exception as e:
            traceback.print_exc()
        if is_success:
            print(f"Usuário {name_user} criado com sucesso")
        else:
            print(f"Usuário {name_user} não criado")

    def delete_by_name(self):
        name_user = input("Digite o nome do usuário a ser deletedo:")
        is_success = None
        try:
            create = self.user_service.delete_by_name(name_user)
        except Exception as e:
            traceback.print_exc()
        if is_success:
            print(f"Usuário {name_user} deletado com sucesso")
        else:
            print(f"Usuário {name_user} não foi encontrado")

    def find_all(self):
        users = []
        try:
            users = self.user_service.find_all()
            if users:
                print(users)

        except Exception as e:
            traceback.print_exc()

        if users:
            print(f"Foram encontrados {len(users)} usuários")
        else:
            print(f"Não foram encontrados nenhum usuário no banco")