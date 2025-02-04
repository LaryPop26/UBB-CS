class Melodie:
    def __init__(self, titlu, artist, gen, durata):
        self.__titlu = titlu
        self.__artist = artist
        self.__gen = gen
        self.__durata = durata

    @property
    def titlu(self):
        return self.__titlu

    @property
    def artist(self):
        return self.__artist

    @property
    def gen(self):
        return self.__gen

    @property
    def durata(self):
        return self.__durata

    @gen.setter
    def gen(self, value):
        self.__gen = value

    @durata.setter
    def durata(self, value):
        self.__durata = value

    def __str__(self):
        return f"{self.__titlu},{self.__artist},{self.__gen},{self.__durata}"
