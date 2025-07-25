import traceback

from model.LetterModel import Letter
from service.DB.ConnectBD import ConnectBD
from service.LetterService import LetterService
from utils.Prints import letter_view, invalid_option

class LetterView:
    def __init__(self, connectBD: ConnectBD):
        self.letter_service = LetterService(connectBD)


    def main_letter_view(self):
        try:
            letter_view()
            optional = int(input())
            if optional == 1:
                self.create_letter()
            elif optional == 2:
                self.find_all()
            elif optional == 0:
                return
            else:
                raise ValueError
        except ValueError:
            invalid_option()
        self.main_letter_view()


    def create_letter(self):
        message = input("Digite a mensagem a ser registrada:")
        user_group_id = input("Digite o ID do usuario_grupo que vai mandar a carta:")
        is_success = None

        try:
            letter = Letter(
                letter_id=None,
                message=message,
                user_group_id=user_group_id
            )

            is_success = self.letter_service.create_letter(letter)
        except Exception as e:
            traceback.print_exc()

        if is_success:
            print(f"Carta adicionada ao sistema com sucesso")
        else:
            print(f"Carta não adicionada. Tente novamente")


    def find_all(self):
        letters = []
        try:
            letters = self.letter_service.find_all()
        except Exception as e:
            traceback.print_exc()

        if letters:
            print(f"Foram encontradas {len(letters)} cartas:")
            for letter in letters:
                print(letter)
        else:
            print(f"Atualmente, não há nenhuma carta no banco")