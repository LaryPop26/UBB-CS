from _pydatetime import datetime

from domain.entitate import Automobil

class SrvAutomobil:
    def __init__(self, repo, validator, undolist):
        """
        Constructor
        :param repo: repository object
        :param validator: validator object
        """
        self.__repo = repo
        self.__validator = validator
        self.__undo_list = undolist

    def adaugare(self, id_a: int, marca: str, pret: int, model: str, data: str):
        """
        Adauga o noua entitate in lista
        :return: lista se modifica
        """
        self.__undo_list = self.__repo.get_all()[:]
        automobil = Automobil(id_a, marca, pret, model, data)
        self.__validator.validate(automobil)
        self.__repo.adaugare(automobil)

    def stergere(self, cifra):
        """
        Stergere entitate daca e valida
        :param cifra: cifra cautata
        :return: lista modificata daca s-au gasit entitati valide,None - altfel
        """
        self.__undo_list = self.__repo.get_all()[:]
        initial = self.__repo.size()
        self.__repo.stergere(cifra)
        after = self.__repo.size()

        return initial - after

    def filtrare(self, text, numar):
        """
        Filtreaza lista dupa anumite criterii
        :param text: str cautat in marca
        :param numar: pretul maxim dorit
        :return: list, lista filtrata
        """
        lista = self.__repo.get_all()
        if text != "" and numar > -1:
            lista_filtrata = [a for a in lista if text in a.marca and a.pret < numar]
        elif text == "" and numar > -1:
            lista_filtrata = [a for a in lista if a.pret < numar]
        elif text != "" and numar == -1:
            lista_filtrata = [a for a in lista if text in a.marca]
        else:
            lista_filtrata = lista

        return lista_filtrata

    def undo(self):
        """
        Reface ultima operatie
        :return: Lista cu un pas inainte
        """
        if not self.__undo_list:
            raise Exception("Nu se mai poate face undo!")

        self.__repo.save(self.__undo_list)
        self.__repo.reload()
        self.__undo_list = []

    def get_all(self):
        return self.__repo.get_all()

    def size(self):
        return self.__repo.size()
