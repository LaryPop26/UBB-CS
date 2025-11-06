class Emisiune:
    def __init__(self, nume, tip, durata, descriere):
        self.__nume = nume
        self.__tip = tip
        self.__durata = durata
        self.__descriere = descriere

    @property
    def nume(self):
        return self.__nume

    @property
    def tip(self):
        return self.__tip

    @property
    def durata(self):
        return self.__durata

    @property
    def descriere(self):
        return self.__descriere

    @durata.setter
    def durata(self, durata):
        self.__durata = durata

    @descriere.setter
    def descriere(self, descriere):
        self.__descriere = descriere

    def __str__(self):
        return f"{self.__nume},{self.__tip},{self.__durata},{self.__descriere}\n"
