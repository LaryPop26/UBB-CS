class Service:
    def __init__(self, repo):
        self.__repo = repo

    def stergere_srv(self, nume, tip):
        """

        :param nume:
        :param tip:
        :return:
        """
        self.__repo.stergere(nume, tip)

    def modificare_srv(self, nume, tip, durata, descriere):
        """

        :param nume:
        :param tip:
        :param durata:
        :param descriere:
        :return:
        """
        self.__repo.modificare(nume, tip, durata, descriere)

    def blocare(self, tip):
        lista = self.__repo.load_from_file()
        lista_noua = [el for el in lista if tip not in el.tip]

        return lista_noua