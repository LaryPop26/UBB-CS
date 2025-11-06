from Domain.tractor import Tractor

class RepoTractor:
    def __init__(self, filename: str):
        """
        Constructor pt repository cu date din fisier
        :param filename: numele fisierului din care se iau date
        """
        self.__filename = filename
        self.__lista_t = []
        self.__load()

    def __load(self) -> None:
        """
        incarca datele din fisier
        """
        with open(self.__filename) as f:
            lines = f.readlines()
            for line in lines:
                if line.strip() != '\n':
                    id_t, denumire, pret, model, data = [i.strip() for i in line.split(',')]
                    self.__lista_t.append(Tractor(int(id_t), denumire, int(pret), model, data))

    def save(self, lista) -> None:
        """
        Incarca datele in fisier
        """
        with open(self.__filename, 'w') as f:
            for t in lista:
                line = f"{t.id_t},{t.denumire},{t.pret},{t.model},{t.data}\n"
                f.write(line)

    def reload(self):
        self.__lista_t = []
        self.__load()

    def adaugare(self, tractor: Tractor) -> None:
        """
        Adauga o noua entitate de tip Tractor in lista
        :param tractor: entitate de tip Tractor
        :return: lista se modifica prin adaugare
        """
        self.__lista_t.append(tractor)
        self.save(self.__lista_t)

    def stergere(self, cifra: int) -> None:
        """
        Sterge o entitate de tip Tractor din lista daca pretul contine cifra data
        :param cifra: cifra cautata in pret
        :return: lista se modifica prin eliminarea el valide
        """
        for t in self.__lista_t:
            nr = t.pret
            ok = 0
            while nr > 0 and ok == 0:
                if cifra == nr % 10:
                    ok = 1
                    self.__lista_t.remove(t)
                nr = nr // 10

    def get_all(self):
        return self.__lista_t

    def size(self):
        return len(self.__lista_t)
