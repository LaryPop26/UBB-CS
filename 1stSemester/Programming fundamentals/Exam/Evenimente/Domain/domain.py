class Eveniment:
    def __init__(self, data, ora, descriere):
        self.__data = data
        self.__ora = ora
        self.__descriere = descriere

    @property
    def data(self):
        return self.__data

    @property
    def ora(self):
        return self.__ora

    @property
    def descrire(self):
        return self.__descriere

    def __str__(self):
        return f"{self.descrire} - {self.ora} - {self.descrire}"
