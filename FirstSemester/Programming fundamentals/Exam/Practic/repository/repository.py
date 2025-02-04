from domain.entitate import Automobil

class RepoAutomobil:
    def __init__(self, filename):
        """
        Constructor
        :param filename: numele fisierului in care se tin datele
        """
        self.__filename = filename
        self.__lista_a = []
        self.__load()

    def __load(self) -> None:
        """
        incarca datele din fisier
        """
        with open(self.__filename) as f:
            lines = f.readlines()
            for line in lines:
                if line.strip() != '\n':
                    id_t, marca, pret, model, data = [i.strip() for i in line.split(',')]
                    self.__lista_a.append(Automobil(int(id_t), marca, int(pret), model, data))

    def save(self, lista) -> None:
        """
        Incarca datele in fisier
        """
        with open(self.__filename, 'w') as f:
            for a in lista:
                line = f"{a.id_a},{a.marca},{a.pret},{a.model},{a.data}\n"
                f.write(line)

    def adaugare(self, automobil: Automobil):
        """
        Adauga o entitate la lista
        :param automobil: entitate de adaugat
        :return: lista modificata prin adaugare
        """
        self.__lista_a.append(automobil)
        self.save(self.__lista_a)

    def stergere(self, cifra: int):
        """
        Sterge o entitate de tip automobil daca in pretul sau se gaseste cifra data
        :param cifra: cifra cautata in pret
        :return: lista modificata
        """
        cifra = str(cifra)
        self.__lista_a = [a for a in self.__lista_a if cifra not in str(a.pret)]
        self.save(self.__lista_a)

    def reload(self):
        """
        restabileste lista dupa undo
        :return:
        """
        self.__lista_a = []
        self.__load()

    def get_all(self):
        return self.__lista_a

    def size(self):
        return len(self.__lista_a)
