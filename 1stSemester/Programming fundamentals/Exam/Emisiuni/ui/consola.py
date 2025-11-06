class Consola:
    def __init__(self, srv):
        self.__srv = srv
        self.__tip = ''

    def ui_stergere(self):
        nume = input('Introdu numele: ')
        tip = input('Introdu tipul: ')
        if tip == self.__tip:
            print('Emisiune blocata')
        else:
            try:
                self.__srv.stergere_srv(nume, tip)
            except Exception as e:
                print(str(e))
        self.blocare_default()

    def ui_modificare(self):
        nume = input('Introdu numele: ')
        tip = input('Introdu tipul: ')
        durata = input('Introdu durata noua: ')
        descriere = input('Introdu descriere noua: ')
        if tip == self.__tip:
            print('Emisiune blocata')
        else:
            try:
                self.__srv.modificare_srv(nume, tip, durata, descriere)
            except Exception as e:
                print(str(e))
        self.blocare_default()

    def blocare(self):
        self.__tip = input('Introdu tipul: ')
        self.blocare_default()

    def blocare_default(self):
        if self.__tip != '':
            print(f'Emisiune fara cele blocate dupa {self.__tip}: ')
        for el in self.__srv.blocare(self.__tip):
            print(el)

    def run(self):
        while True:
            print('Comenzi')
            cmd = int(input('Introdu command: '))

            match cmd:
                case 1:
                    self.ui_stergere()
                case 2:
                    self.ui_modificare()
                case 3:
                    self.blocare()
                case _:
                    break
