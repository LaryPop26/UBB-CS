class Console:
    def __init__(self, srv):
        self.__srv = srv
        self.__text = ""
        self.__numar = -1

    @staticmethod
    def menu():
        print("Gestiune Tractoare")
        print("1. Adaugare")
        print("2. Stergere")
        print("3. Filtrare")
        print("4. Undo")

    def ui_adaugare(self):
        print("Adaugare")
        id_t = int(input("Id: "))
        denumire = str(input("Denumire: "))
        pret = int(input("Pret: "))
        model = input("Model: ")
        data = input("Data Revizie: ")

        self.__srv.adaugare(id_t, denumire, pret, model, data)

    def ui_stergere(self):
        print("Stergere")
        cifra = int(input("Cifra de cautat: "))

        self.__srv.stergere(cifra)

    def ui_filtrare1(self):
        print("Filtrare")
        self.__text = input("Denumire cautata: ")
        self.__numar = int(input("Pret cautat: "))

        self.ui_filtrare2()

    def ui_filtrare2(self):
        lista = self.__srv.filtrare(self.__text, self.__numar)
        if self.__text != "" and self.__numar > -1:
            print(f"Lista filtrata dupa sirul {self.__text} si pretul {self.__numar}:")
        elif self.__text == "" and self.__numar > -1:
            print(f"Lista filtrata dupa pretul {self.__numar}:")
        elif self.__text != "" and self.__numar == -1:
            print(f"Lista filtrata dupa sirul {self.__text}:")
        else:
            print(f"Lista fara filtre:")

        self.print_lst(lista)

    def ui_undo(self):
        self.__srv.undo()
        self.print_lst(self.__srv.get_all_srv())

    @staticmethod
    def print_lst(lst):
        if len(lst) == 0:
            print("Lista e goala!")
        for item in lst:
            print(item)

    def run(self):
        while True:
            try:
                self.menu()
                self.ui_filtrare2()
                option = int(input(">>> "))
                match option:
                    case 1:
                        self.ui_adaugare()
                    case 2:
                        self.ui_stergere()
                    case 3:
                        self.ui_filtrare1()
                    case 4:
                        self.ui_undo()
                    case _:
                        break
            except Exception as e:
                print(e)
