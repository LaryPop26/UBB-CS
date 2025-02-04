class Locatie:
    def __init__(self, id_locatie, denumire, tip, pret_pe_zi):
        self.__id = id_locatie
        self.__denumire = denumire
        self.__tip = tip
        self.__pret_pe_zi = pret_pe_zi

    @property
    def id_locatie(self):
        return self.__id

    @property
    def denumire(self):
        return self.__denumire

    @property
    def tip(self):
        return self.__tip

    @property
    def pret_pe_zi(self):
        return self.__pret_pe_zi

    def __str__(self):
        return ("Locatie " + str(self.id_locatie) + " | Denumire " + str(self.denumire)
                + " | Tip " + str(self.tip) + " | Pret Pe Zi " + str(self.pret_pe_zi))
