import traceback

from model.GroupModel import Group
from service.ConnectBD import ConnectBD
from service.GroupService import GroupService
from utils.Prints import group_view


class GroupView:
    def __init__(self, connectBD: ConnectBD):
        self.group_service = GroupService(connectBD)

    def main_group_view(self):
        group_view()
        optional = int(input())
        if optional == 1:
            self.create_group()
        if optional == 2:
            pass
        if optional == 3:
            self.find_all()
        if optional == 0:
            return
        self.main_group_view()

    def create_group(self):
        name_group = input("Digite o nome do grupo:")
        description_group = input("Digite a descrição do grupo:")
        status_group = "CREATED"
        maximum_value_group = int(input("Digite o valor minimo dos presentes:"))
        minimum_value_group = int(input("Digite o valor maximo dos presentes:"))
        draw_date_group = input("Digite a data do sorteio:")
        meet_date_group = input("Digite a data do encontro:")
        location_group = input("Digite o local do encontro:")
        created_user_id_group = int(input("Digite o seu id:"))

        is_success = None
        try:
            group = Group(
                group_id=None,
                name=name_group,
                description=description_group,
                status_group=status_group,
                maximum_value=maximum_value_group,
                minimum_value=minimum_value_group,
                link=None,
                draw_date=draw_date_group,
                meet_date=meet_date_group,
                location=location_group,
                created_user_id=created_user_id_group
            )

            is_success = self.group_service.create_group(group)

        except Exception as e:
            traceback.print_exc()

        if is_success:
            print(f"Usuário {name_group} criado com sucesso")
        else:
            print(f"Usuário {name_group} não criado")

    def find_all(self):
        groups = []
        try:
            groups = self.group_service.find_all()
        except Exception as e:
            traceback.print_exc()

        if groups:
            for group in groups:
                print(group)
            print(f"Foram encontrados {len(groups)} usuários")
        else:
            print(f"Não foram encontrados nenhum usuário no banco")