from model.LetterModel import Letter
from repository.LetterRepository import LetterRepository
from service.DB.ConnectBD import ConnectBD


class LetterService:
    def __init__(self, connectBD: ConnectBD):
        self.letter_repository = LetterRepository(connectBD)

    def create_letter(self, letter: Letter):
        return self.letter_repository.insert(letter)

    def find_all(self):
        return self.letter_repository.find_all()

    def delete_by_id(self, letter_id: int):
        return self.letter_repository.delete_by_id(letter_id)