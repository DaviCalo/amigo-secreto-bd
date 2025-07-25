import traceback

from model.UserModel import User
from service.DB.ConnectBD import ConnectBD
from service.UserService import UserService
from utils.Prints import user_view, invalid_option


class UserView:
    def __init__(self, connectBD: ConnectBD):
        self.user_service = UserService(connectBD)


    def main_user_view(self):
        try:
            user_view()
            optional = int(input())
            if optional == 1:
                self.create_user()
            elif optional == 2:
                self.delete_by_name()
            elif optional == 3:
                self.find_all()
            elif optional == 4:
                self.find_by_id()
            elif optional == 5:
                self.update_by_id()
            elif optional == 0:
                return
            else:
                raise ValueError
        except ValueError:
            invalid_option()
        self.main_user_view()


    def create_user(self):
        name_user = input("Digite o nome do usuário:")
        email_user = input("Digite o email do usuário:")
        passkey_user = input("Digite a senha do usuário:")
        user = None

        try:
            user = User(
                user_id=None,
                name=name_user,
                email=email_user,
                passkey=passkey_user
            )

            user = self.user_service.create_user(user)
        except Exception as e:
            traceback.print_exc()

        if user:
            print(f"Usuário criado com sucesso!")
            print(f"Seu Id de usuário é {user.user_id}")
        else:
            print(f"Usuário {name_user} não criado")


    def delete_by_name(self):
        name_user = input("Digite o nome do usuário a ser deletedo:")
        is_success = None

        try:
            is_success = self.user_service.delete_by_name(name_user)

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
        except Exception as e:
            traceback.print_exc()

        if users:
            for user in users:
                print(user)
            print(f"Foram encontrados {len(users)} usuários")
        else:
            print(f"Não foram encontrados nenhum usuário no banco")


    def find_by_id(self):
        user_id = int(input("Digite o id do usuário para encontrar:"))
        user = None

        try:
            user = self.user_service.find_by_id(user_id)
        except Exception as e:
            traceback.print_exc()

        if user:
            print(user)
        else:
            print(f"Não foram encontrados nenhum usuário no banco")

    def update_by_id(self):
        id_user = int(input("Digite o id do usuario que deseja atualizar:"))
        name_user = input("Digite o novo nome do usuário:")
        email_user = input("Digite o novo email do usuário:")
        passkey_user = input("Digite a novo senha do usuário:")
        is_success = None

        try:
            user = User(
                user_id=id_user,
                name=name_user,
                email=email_user,
                passkey=passkey_user
            )

            is_success = self.user_service.update_by_id(user)

        except Exception as e:
            traceback.print_exc()

        if is_success:
            print(f"Usuário {name_user} atualizado com sucesso")
        else:
            print(f"Usuário {name_user} não atualizado")
