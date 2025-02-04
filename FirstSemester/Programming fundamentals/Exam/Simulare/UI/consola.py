class Consola:
    def __init__(self, srv):
        self.__srv = srv

    def print(self):
        print("1. Cautare locatii dupa tip")
        print("2. Rezervare")
        print("3. Print locatii")
        print("4. Exit")

    def __cautare(self):
        tip = input("Tip cautat: ")
        gasite = self.__srv.cauta_locatii_dupa_tip(tip)
        self.__show_all(gasite)

    def __rezervare(self):
        id_loc = int(input("Id-ul locatiei: "))
        buget = int(input("Buget: "))
        rezervare = self.__srv.rezervare(id_loc, buget)
        print(rezervare)

    @staticmethod
    def __show_all(lst):
        if len(lst) == 0:
            print("Lista e goala!")
        for el in lst:
            print(el)

    def run(self):
        while True:
            try:
                self.print()
                option = int(input(">>> "))
                match option:
                    case 1:
                        self.__cautare()

                    case 2:
                        self.__rezervare()

                    case 3:
                        self.__show_all(self.__srv.get_all())

                    case 4:
                        break

            except Exception as e:
                print(e)
