from datetime import datetime

class Console:
    def __init__(self, controller):
        self.__controller = controller

    @staticmethod
    def menu():
        print("Evenimente")
        print("1 - Adaugare")
        print("2 - Filtrare")
        print("3 - Export")

    def ui_add(self):
        data = input("Introdu data: ")
        ora = input("Introdu ora: ")
        descriere = input("Introdu descriere: ")
        self.__controller.add(data, ora, descriere)

    def ui_filter1(self):
        azi = datetime.today().strftime("%d.%m.%Y")
        evenimente = self.__controller.get_evenimente_pt_data(azi)
        for eveniment in evenimente:
            print(eveniment)

    def ui_filter2(self):
        data = input("Introdu data: ")
        evenimente = self.__controller.get_evenimente_pt_data(data)
        for eveniment in evenimente:
            print(eveniment)

    def ui_export(self):
        cuvant = input("Introdu textul cautat: ")
        output = input("Introdu numele fisierului: ")
        print(self.__controller.export_events(cuvant, output))

    def run(self):
        self.ui_filter1()
        while True:
            try:
                self.menu()
                option = int(input(">>> "))
                match option:
                    case 1:
                        self.ui_add()
                    case 2:
                        self.ui_filter2()
                    case 3:
                        self.ui_export()
                    case _:
                        break
            except Exception as e:
                print(e)
