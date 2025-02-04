from Domain.booking import BookingInquiry

class ServiceError(Exception):
    def __init__(self, msg):
        self.msg = msg

class LocatieSrv:
    def __init__(self, repo, validator):
        self.__repo = repo
        self.__validator = validator

    def cauta_locatii_dupa_tip(self, tip_partial: str):
        """
        Cauta toate obiectele ce au stringuri ce contin tipul dat
        :param tip_partial: tip cautat
        :return: lista cu toate obiectele valide
        """
        self.__validator.validate_tip(tip_partial)
        return [locatie for locatie in self.get_all() if tip_partial.lower() in locatie.tip.lower()]

    def rezervare(self, id_locatie: int, buget: int):
        """
        Gaseste nr de zile pe care userul si le permite
        :param id_locatie: id ul locatiei pt care se cauta
        :param buget: bugetul maxim
        :return: obiect de tip BookingInquiry ce indeplineste consitia
        """
        self.__validator.validate_nr(id_locatie)
        self.__validator.validate_nr(buget)
        locatie = self.__repo.cauta_dupa_id(id_locatie)
        if locatie is None:
            raise ServiceError("Id ul nu exista!")
        return BookingInquiry(locatie, buget)

    def get_all(self):
        return self.__repo.get_all()
