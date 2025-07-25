import traceback

from model.GroupModel import Group
from model.UsersGroupModel import UserGroup
from service.DB.ConnectBD import ConnectBD
from service.UserGroupService import UserGroupService
from utils.Prints import user_group_view, invalid_option


class UserGroupView:
    def __init__(self, connectBD: ConnectBD):
        self.user_group_service = UserGroupService(connectBD)

    def main_user_group_view(self):
        try:
            user_group_view()
            optional = int(input())
            if optional == 1:
                self.create_user_group()
            elif optional == 2:
                self.delete_by_id()
            elif optional == 3:
                self.find_all()
            elif optional == 4:
                self.rate_users()
            elif optional == 0:
                return
            else:
                raise ValueError
        except ValueError:
            invalid_option()
        self.main_user_group_view()

    def create_user_group(self):
        user_id = input("Digite o id do usuario que vai participar do grupo:")
        group_id = input("Digite o id do grupo:")

        is_success = None
        try:
            user_group = UserGroup(
                user_group_id=None,
                user_id=user_id,
                recipient_user_id=None,
                group_id=group_id,
                grift_select_id=None
            )

            is_success = self.user_group_service.create_user_group(user_group)

        except Exception as e:
            traceback.print_exc()

        if is_success:
            print(f"Usuario adicionado ao grupo")
        else:
            print(f"Error ao adicionar usuario ao grupo")


    def find_all(self):
        user_groups = []
        try:
            user_groups = self.user_group_service.find_all()
        except Exception as e:
            traceback.print_exc()

        if user_groups:
            for user_group in user_groups:
                print(user_group)
            print(f"Foram encontrados {len(user_groups)} grupos")
        else:
            print(f"Não foi encontrado nenhum grupo no banco")


    def delete_by_id(self):
        id_group = int(input("Digite o id do user grupo que deseja deletar:"))
        is_success = None

        try:
            is_success = self.user_group_service.delete_by_id(id_group)
        except Exception as e:
            traceback.print_exc()

        if is_success:
            print(f"Grupo deletado com sucesso")
        else:
            print(f"Erro ao deletar o grupo")


    def rate_users(self):
        id_user_group = int(input("Digite o id do grupo que deseja sotear:"))
        is_success = None

        try:
            is_success = self.user_group_service.rate_users(id_user_group)
        except Exception as e:
            traceback.print_exc()

        if is_success:
            print(f"Usuarios do grupo sorteados")
        else:
            print(f"Erro ao sotear usuarios do grupo")