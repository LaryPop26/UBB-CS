from datetime import datetime
from domain.entitate import Automobil

class ValidatorError(Exception):
    def __init__(self, msg):
        self.msg = msg

class Validator:
    @staticmethod
    def validate(automobil: Automobil):
        """
        validate date pentru automobil
        :param automobil: entitate cu campurile de verificat
        :return: -;
        :raises ValidatorError; daca cel putin un parametru nu e valid
        """
        errors = ""
        if automobil.id_a < 0:
            errors += 'Id ul trebuie sa fie pozitiv\n'

        if automobil.marca == "":
            errors += 'Marca nu poate lipsi\n'

        if automobil.pret < 0:
            errors += 'Pretul trebuie sa fie intreg pozitiv\n'

        if automobil.model == "":
            errors += 'Model nu poate lipsi\n'

        try:
            datetime.strptime(automobil.data, '%d:%m:%Y')
        except ValueError:
            errors += 'Data nu are formatul bun'

        if len(errors) > 0:
            raise ValidatorError(errors)
