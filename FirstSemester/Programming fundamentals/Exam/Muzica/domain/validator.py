class Validator:
    @staticmethod
    def validate(durata, gen):
        errors = []
        if durata.isdigit() != True or float(durata) != int(durata) or int(durata) < 0:
            errors.append("Durata invalida")
        if gen not in ["rock",'jazz','pop','altele']:
            errors.append("Gen invalid")
        if len(errors) > 0:
            raise Exception(errors)
