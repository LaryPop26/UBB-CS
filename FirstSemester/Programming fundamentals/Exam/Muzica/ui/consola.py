class Consola:
    def __init__(self, srv):
        self.__srv = srv

    def modificare(self):
        titlu = input("Titlu: ")
        artist = input("Artist: ")
        gen = input("Gen: ")
        durata = input("Durata: ")
        try:
            self.__srv.modificare(titlu, artist, gen, durata)
        except Exception as e:
            print(e)

    def add_random(self):
        n = int(input("Nr melodii: "))
        lista_titluri = input("Lista titluri random: ")
        lst_titluri = lista_titluri.split(',')
        lista_artist = input("Lista artist random: ")
        lst_artist = lista_artist.split(',')

        self.__srv.add_random(lista_titluri, lst_titluri)

    def export(self):
        output_fisier = input("Output fisier: ")
        self.__srv.export(output_fisier)

    def run(self):
        while True:
            optiune = int(input("Optiune: "))
            match optiune:
                case 1:
                    self.modificare()
                case 2:
                    self.add_random()
                case 3:
                    self.export()
                case 4:
                    break
                case _:
                    print("reincearca")