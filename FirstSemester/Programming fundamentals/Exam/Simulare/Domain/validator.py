class ValidatorError(Exception):
    def __init__(self, msg):
        self.msg = msg

class Validator:
    @staticmethod
    def validate_nr(nr):
        if nr < 0:
            raise ValidatorError("Campul nu poate fi negativ")

    @staticmethod
    def validate_tip(tip_locatie):
        if tip_locatie == "":
            raise ValidatorError("Tip nu poate fi gol")
