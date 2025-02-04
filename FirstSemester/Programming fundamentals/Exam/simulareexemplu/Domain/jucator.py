
class Jucator:
    def __init__(self, nume, tara, nr_meciuri, nr_victorii, nr_puncte):
        self.__nume = nume
        self.__tara = tara
        self.__nr_meciuri = nr_meciuri
        self.__nr_victorii = nr_victorii
        self.__nr_puncte = nr_puncte

    @property
    def nume(self):
        return self.__nume

    @property
    def tara(self):
        return self.__tara

    @property
    def nr_meciuri(self):
        return self.__nr_meciuri

    @property
    def nr_victorii(self):
        return self.__nr_victorii

    @property
    def nr_puncte(self):
        return self.__nr_puncte

    @nume.setter
    def nume(self, nume):
        self.__nume = nume

    @tara.setter
    def tara(self, tara):
        self.__tara = tara

    @nr_meciuri.setter
    def nr_meciuri(self, nr_meciuri):
        self.__nr_meciuri = nr_meciuri

    @nr_victorii.setter
    def nr_victorii(self, nr_victorii):
        self.__nr_victorii = nr_victorii

    @nr_puncte.setter
    def nr_puncte(self, nr_puncte):
        self.__nr_puncte = nr_puncte

    def __eq__(self, other):
        if type(other) != type(self):
            return False
        return self.nume == other.nume and self.tara == other.tara

    def __str__(self):
        return ("Nume: " + self.__nume + " | Tara: " + self.__tara + " | Numar meciuri: " + str(self.__nr_meciuri)
                + " | Numar victorii: " + str(self.__nr_victorii) + " | Numar punncte: " + str(self.__nr_puncte))
