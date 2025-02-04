from domain.entitate import Emisiune

class RepoEmisiuni:
    def __init__(self, filename):
        self.__filename = filename

    def load_from_file(self):
        """

        :return:
        """
        lista = []
        with open(self.__filename, "r") as file:
            lines = file.readlines()
            for line in lines:
                nume, tip, durata, descriere = [i.strip() for i in line.split(',')]
                emisiune = Emisiune(nume, tip, durata, descriere)
                lista.append(emisiune)
        return lista

    def save_to_file(self, lista):
        """

        :return:
        """
        with open(self.__filename, "w") as file:
            for em in lista:
                string = em.nume + ',' + em.tip + ',' + str(em.durata) + ',' + em.descriere+'\n'
                file.write(string)

    def stergere(self, nume, tip):
        erori = []
        lista = self.load_from_file()
        lungime = len(lista)
        lista = [el for el in lista if el.nume != nume and el.tip != tip]
        if len(lista) == lungime:
            erori.append('Nu exista emisiune cu aceste date')
        if len(erori) > 0:
            raise ValueError('\n'.join(erori))

        self.save_to_file(lista)

    def modificare(self, nume, tip, durata, descriere):
        erori = []
        ok = 0
        lista = self.load_from_file()
        for el in lista:
            if el.nume == nume and el.tip == tip:
                el.durata = durata
                el.descriere = descriere
                ok = 1
        if ok == 0:
            erori.append('Nu exista emisiune cu aceste date')

        if len(erori) > 0:
            raise ValueError('\n'.join(erori))

        self.save_to_file(lista)