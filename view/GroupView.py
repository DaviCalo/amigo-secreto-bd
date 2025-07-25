import traceback

from model.GroupModel import Group
from service.DB.ConnectBD import ConnectBD
from service.GroupService import GroupService
from utils.Prints import group_view, invalid_option


class GroupView:
    def __init__(self, connectBD: ConnectBD):
        self.group_service = GroupService(connectBD)

    def main_group_view(self):
        try:
            group_view()
            optional = int(input())
            if optional == 1:
                self.create_group()
            elif optional == 2:
                self.delete_by_id()
            elif optional == 3:
                self.find_all()
            elif optional == 4:
                self.update_by_id()
            elif optional == 0:
                return
            else:
                raise ValueError
        except ValueError:
            invalid_option()
        self.main_group_view()

    def create_group(self):
        name_group = input("Digite o nome do grupo:")
        description_group = input("Digite a descrição do grupo:")
        status_group = "CREATED"
        maximum_value_group = int(input("Digite o valor minimo dos presentes:"))
        minimum_value_group = int(input("Digite o valor maximo dos presentes:"))
        draw_date_group = input("Digite a data do sorteio (Ex: 2025-12-20):")
        meet_date_group = input("Digite a data do encontro (Ex: 2025-12-20):")
        location_group = input("Digite o local do encontro:")
        created_user_id_group = int(input("Digite o id do usuário criador do grupo:"))

        is_success = None
        try:
            group = Group(
                group_id=None,
                name=name_group,
                description=description_group,
                status_group=status_group,
                maximum_value=maximum_value_group,
                minimum_value=minimum_value_group,
                draw_date=draw_date_group,
                meet_date=meet_date_group,
                location=location_group,
                created_user_id=created_user_id_group
            )

            is_success = self.group_service.create_group(group)

        except Exception as e:
            traceback.print_exc()

        if is_success:
            print(f"Grupo {name_group} criado com sucesso")
        else:
            print(f"Grupo {name_group} não criado")


    def find_all(self):
        groups = []
        try:
            groups = self.group_service.find_all()
        except Exception as e:
            traceback.print_exc()

        if groups:
            for group in groups:
                print(group)
            print(f"Foram encontrados {len(groups)} grupos")
        else:
            print(f"Não foi encontrado nenhum grupo no banco")


    def update_by_id(self):
        id_group = int(input("Digite o id do grupo que deseja atualizar:"))
        name_group = input("Digite o nome do grupo:")
        description_group = input("Digite a descrição do grupo:")
        maximum_value_group = int(input("Digite o valor minimo dos presentes:"))
        minimum_value_group = int(input("Digite o valor maximo dos presentes:"))
        draw_date_group = input("Digite a data do sorteio:")
        meet_date_group = input("Digite a data do encontro:")
        location_group = input("Digite o local do encontro:")

        is_success = None

        group = Group(
            group_id=id_group,
            name=name_group,
            description=description_group,
            status_group=None,
            maximum_value=maximum_value_group,
            minimum_value=minimum_value_group,
            draw_date=draw_date_group,
            meet_date=meet_date_group,
            location=location_group,
            created_user_id=None
        )

        try:
            is_success = self.group_service.update_by_id(group)
        except Exception as e:
            traceback.print_exc()

        if is_success:
            print(f"Grupo atualizado com sucesso")
        else:
            print(f"Erro na atualização do grupo")


    def delete_by_id(self):
        id_group = int(input("Digite o id do grupo que deseja deletar:"))
        is_success = None

        try:
            is_success = self.group_service.delete_by_id(id_group)
        except Exception as e:
            traceback.print_exc()

        if is_success:
            print(f"Grupo deletado com sucesso")
        else:
            print(f"Erro ao deletar o grupo")