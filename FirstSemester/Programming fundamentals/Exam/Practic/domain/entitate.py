class Automobil:
    def __init__(self, id_a, marca, pret, model, data):
        """
        Constructor
        :param id_a: id automobil
        :param marca: marca automobil
        :param pret: pret automobil
        :param model: model automobil
        :param data: data inspectie tehnica automobil
        """
        self.__id_a = id_a
        self.__marca = marca
        self.__pret = pret
        self.__model = model
        self.__data = data

    @property
    def id_a(self):
        return self.__id_a

    @property
    def marca(self):
        return self.__marca

    @property
    def pret(self):
        return self.__pret

    @property
    def model(self):
        return self.__model

    @property
    def data(self):
        return self.__data

    def __eq__(self, other):
        return self.__id_a == other.id_a

    def __str__(self):
        return ("Id: " + str(self.__id_a) +
                " | Marca: " + self.__marca +
                " | Pret: " + str(self.__pret) +
                "  Model: " + self.__model +
                " | Data: " + self.__data)
