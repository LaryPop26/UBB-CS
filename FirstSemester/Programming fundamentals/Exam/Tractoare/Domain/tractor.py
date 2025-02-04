class Tractor:
    def __init__(self, id_t: int, denumire: str, pret: int, model: str, data: str):
        """
        Constructor pt entitatatea Tractor
        :param id_t: id ul din lista
        :param denumire: denumire tractor
        :param pret: pret tractor
        :param model: model tractor
        :param data: data expirarii reviziei
        """
        self.__id_t = id_t
        self.__denumire = denumire
        self.__pret = pret
        self.__model = model
        self.__data = data

    @property
    def id_t(self):
        return self.__id_t

    @property
    def denumire(self):
        return self.__denumire

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
        return self.__id_t == other.__id_t

    def __str__(self):
        return ("Id: " + str(self.__id_t)
                + " | Denumire: " + self.__denumire
                + " | Pret: " + str(self.__pret)
                + " | Model: " + self.__model
                + " | Data revizie: " + self.__data
                )

def test_domain():
    t = Tractor(1, "da", 123, "curent", "23.12.2025")
    assert t.denumire == "da"
    assert t.pret == 123
    assert t.model == "curent"
    assert t.data == "23.12.2025"

test_domain()
