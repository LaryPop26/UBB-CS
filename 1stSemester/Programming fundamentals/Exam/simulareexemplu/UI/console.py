class Console:
    def __init__(self, srv):
        self.__srv = srv

    @staticmethod
    def print():
        print("1. Add")
        print("2. Show all players from a country , who have more than x points")
        print("3. Jucatori ordonat descendent dupa raport victorii")
        print("4. Evolutie")
        print("5. Print all")
        print("6. Exit")

    def __add_ui(self):
        nume = input("Introdu nume: ")
        tara = input("Introdu tara: ")
        nr_meciuri = int(input("Introdu nr_meciuri: "))
        nr_victorii = int(input("Introdu nr_victorii: "))
        nr_puncte = int(input("Introdu nr_puncte: "))
        self.__srv.store(nume, tara, nr_meciuri, nr_victorii, nr_puncte)

    def __all_players_with_score_higher_than_ui(self):
        tara = input("Introdu tara: ")
        punctaj = int(input("Introdu punctaj: "))
        lista = self.__srv.all_players_with_score_higher_than(tara, punctaj)
        self.__print_all(lista)

    def __procentaj_ui(self):
        lst = self.__srv.procent_descrescator()
        self.__print_all(lst)

    @staticmethod
    def __print_all(lst):
        if len(lst) == 0:
            print("List is empty")
        for el in lst:
            print(el)

    def run(self):
        while True:
            try:
                self.print()
                option = int(input(">>> "))
                match option:
                    case 1:
                        self.__add_ui()

                    case 2:
                        self.__all_players_with_score_higher_than_ui()

                    case 3:
                        self.__procentaj_ui()

                    case 4:
                        self.__print_all(self.__srv.get_all())

                    case 5:
                        break

            except Exception as e:
                print(e)
