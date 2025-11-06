from Domain.tractor import Tractor

class SrvTractor:
    def __init__(self, repo, validator, undolist):
        self.__repo = repo
        self.__validator = validator
        self.__undo_lista = undolist

    def adaugare(self, id_t: int, denumire: str, pret: int, model: str, data: str):
        """
        Adaugare entitate
        :param id_t: id tractor
        :param denumire: denumire
        :param pret: pret
        :param model: model
        :param data: data revizie
        :return:
        """
        self.__undo_lista = self.__repo.get_all()[:]
        t = Tractor(id_t, denumire, pret, model, data)
        self.__validator.validare(t)
        self.__repo.adaugare(t)

    def stergere(self, cifra):
        """
        Stergere entitate daca pretul sau contine cifra data
        :param cifra: cifra cautate
        :return:
        """
        self.__undo_lista = self.__repo.get_all()[:]
        self.__repo.stergere(cifra)

    def filtrare(self, text="", numar=-1):
        """
        Filtreaza lista dupa criteriile date
        :param text: text cautat
        :param numar: nr cautat
        :return:
        """
        lista = self.__repo.get_all()
        if text != "" and numar > -1:
            lista_filtrata = [t for t in lista if text in t.denumire and t.pret < numar]
        elif text == "" and numar > -1:
            lista_filtrata = [t for t in lista if t.pret < numar]
        elif text != "" and numar == -1:
            lista_filtrata = [t for t in lista if text in t.denumire]
        else:
            lista_filtrata = lista
        return lista_filtrata

    def undo(self):
        """
        Readuce lista la starea precedenta
        :return:
        :raises: Exception, daca nu mai exista posibilitatea de undo
        """
        if not self.__undo_lista:
            raise Exception("Nu exista alte operatii!")

        self.__repo.save(self.__undo_lista)
        self.__repo.reload()
        self.__undo_lista = []

    def get_all_srv(self):
        return self.__repo.get_all()

    def size(self):
        return self.__repo.size()
