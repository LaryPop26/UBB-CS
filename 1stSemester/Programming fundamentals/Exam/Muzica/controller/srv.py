import random

from domain.entitate import Melodie

class Controller:
    def __init__(self, repo, validator):
        self.__repo = repo
        self.__validator = validator

    def adauga(self,titlu,artist, gen,durata):
        melodie = Melodie(titlu,artist,gen,durata)
        # nu e facut self.__validator.validate(melodie)
        self.__repo.adauga(melodie)

    def modificare(self,titlu,artist, gen,durata):
        """

        :param self:
        :param titlu:
        :param artist:
        :param gen:
        :param durata:
        :return:
        """
        self.__validator.validare(durata, gen)
        self.__repo.modificare(titlu, artist, gen, durata)

    def add_random(self,n,l1,l2):
        """

        :param n:
        :param l1:
        :param l2:
        :return:
        """
        l3 = ['pop','jazz','rock','altele']
        i = 1
        lista = self.__repo.load()
        ok = 1
        while i <= n:
            titlu = random.choice(l1)
            artist = random.choice(l2)
            durata = random.randint(90,250)
            gen = random.choice(l3)
            melodie = Melodie(titlu, artist, gen, durata)
            for el in lista:
                if el.titlu == titlu and el.artist == artist:
                    ok = 0
            if ok == 1:
                lista.append(melodie)
                i+=1
        self.__repo.save()

    def add_random2(self,nr):
        # nu merge aici
        gen = ['pop','jazz','rock','altele']
        vocale = ['a','e','i','o','u']
        consoane = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']
        titlu_lst = []
        artist_lst = []
        titlu = ''
        artist = ''
        ok = 0
        for i in range(nr):
            cate_lit = random.randint(8,12)
            index = random.randint(1,cate_lit)
            for j in range(cate_lit):
                if ok == 0:
                    titlu_lst.append(random.choice(vocale))
                    artist_lst.append(random.choice(vocale))
                    ok = 1
                else:
                    titlu_lst.append(random.choice(consoane))
                    artist_lst.append(random.choice(consoane))
                    ok = 0
            titlu_lst[index] = " "
            artist_lst[index] = " "
            for el in titlu_lst:
                titlu = titlu + el
            for el in artist_lst:
                artist = artist + el
            gen = random.choice(gen)
            durata = str(random.randint(90,250))
            self.add(titlu,artist,gen,durata)
            titlu_lst = []
            artist_lst = []
            titlu = ''
            artist = ''
            ok = 0

    def export(self, output):
        """

        :param output:
        :return:
        """
        lista = self.__repo.load()

        lista = sorted(lista, key=lambda el: (el.titlu,el.artist))

        with open(output, 'w') as f:
            for mel in lista:
                string = mel.titlu + ',' + mel.artist + ',' + mel.gen + ',' + str(mel.durata)+'\n'
                f.write(string)
