import traceback

from model.LetterModel import Letter
from service.DB.ConnectBD import ConnectBD
from service.LetterService import LetterService
from utils.Prints import letter_view

class LetterView:
    def __init__(self, connectBD: ConnectBD):
        self.letter_service = LetterService(connectBD)


    def main_letter_view(self):
        letter_view()
        optional = int(input())
        if optional == 1:
            self.create_letter()
        if optional == 2:
            self.find_all()


    def create_letter(self):
        letter_id = input("Digite o ID da carta:")
        message = input("Digite a mensagem a ser registrada:")
        user_group_id = input("Digite o ID do grupo destinatário:")
        is_success = None

        try:
            letter = Letter(
                id=letter_id,
                message=message,
                user_group_id=user_group_id
            )

            is_success = self.letter_service.create_letter(letter)
        except Exception as e:
            traceback.print_exc()

        if is_success:
            print(f"Carta com o ID: {letter_id} adicionada ao sistema com sucesso")
        else:
            print(f"Carta de ID: {letter_id} não adicionada. Tente novamente")


    def find_all(self):
        letters = []
        try:
            letters = self.letter_service.find_all()
        except Exception as e:
            traceback.print_exc()

        if letters:
            for letter in letters:
                print(letter)
            print(f"Foram encontradas {len(letters)} cartas:")
            print(f"Cartas: {letters}")
        else:
            print(f"Atualmente, não há nenhuma carta no banco")