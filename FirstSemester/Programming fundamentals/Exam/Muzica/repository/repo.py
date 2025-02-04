from domain.entitate import Melodie

class Repo:
    def __init__(self, filename):
        self.__filename = filename

    def load(self):
        """

        :return:
        """
        lista = []
        with open(self.__filename,'r') as file:
            lines = file.readlines()
            for line in lines:
                titlu, artist, gen, durata = [i.strip() for i in line.split()]
                melodie = Melodie(titlu, artist, gen, str(durata))
                lista.append(melodie)
        return lista

    def save(self, lista):
        """

        :return:
        """
        with open(self.__filename,'w') as file:
            for mel in lista:
                string = mel.titlu + ',' + mel.artist + ',' + mel.gen + ',' + str(mel.durata)
                file.write(string)

    def adauga(self, melodie):
        """

        :param melodie:
        :return:
        """
        lista = self.load()
        lista.append(melodie)
        self.save(lista)

    def modificare(self,titlu, artist, gen, durata):
        """

        :param titlu:
        :param artist:
        :param gen:
        :param durata:
        :return:
        """
        ok = 0
        lista = self.load()
        for el in lista:
            if el.titlu == titlu and el.artist == artist:
                el.durata = durata
                el.gen = gen
                ok = 1
        if ok == 0:
            raise Exception('Melodia nu exista')
        self.save(lista)
