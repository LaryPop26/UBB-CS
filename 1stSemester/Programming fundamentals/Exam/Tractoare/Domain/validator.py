from datetime import datetime
from Domain.tractor import Tractor

class ValidationError(Exception):
    def __init__(self,msg):
        self.msg = msg

class Validator:
    @staticmethod
    def validare(tractor: Tractor):
        """

        :param tractor:
        :return:
        """
        errors = ""
        if tractor.id_t < 0:
            errors += "Id ul trebuie sa fie pozitiv\n"
        if tractor.denumire == "":
            errors += "Denumirea nu poate lipsi\n"
        if tractor.pret < 0:
            errors += "Pretul trebuie sa fie pozitiv\n"
        if tractor.model == "":
            errors += "Model nu poate lipsi\n"
        try:
            datetime.strptime(tractor.data,"%d:%m:%Y")
        except ValueError:
            errors += "Data nu este in formatul zz:mm:yyyy\n"
        
        if len(errors) > 0:
            raise ValidationError(errors)
