class BookingInquiry:
    def __init__(self, locatie, buget):
        self.__locatie = locatie
        self.__buget = buget

    @property
    def locatie(self):
        return self.__locatie

    @property
    def buget(self):
        return self.__buget

    def get_number_of_days(self):
        return self.__buget // self.__locatie.pret_pe_zi

    def __str__(self):
        return ("Locatie " + str(self.__locatie.denumire) + " | Tip " + self.__locatie.tip
                + " | Nr zile " + str(self.get_number_of_days()))
