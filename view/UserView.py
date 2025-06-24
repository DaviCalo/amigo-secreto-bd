import os
import traceback

from repository.UserRepository import UserRepository
from service.ConnectBD import ConnectBD
from service.UserService import UserService
from utils.Mainprint import user_view


class UserView:
    def __init__(self, user_service: UserService):
        self.user_service = user_service

    def main_user_view(self):
        user_view()
        optional = int(input())
        if optional == 1:
            self.create_user()

    def create_user(self):
        print("Digite o nome do usuário")
        name_user = input()
        print("Digite o email do usuário")
        email_user = input()
        print("Digite a senha do usuário")
        passkey_user = input()

        create = None

        try:
            create = self.user_service.create_user(name_user, email_user, passkey_user)
        except Exception as e:
            traceback.print_exc()

        if create:
            print(f"Usuário {name_user} criado com sucesso")
        else:
            print(f"Usuário {name_user} não criado")