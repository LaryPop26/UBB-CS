from Domain.jucator import Jucator
from Exceptions.exceptions import AlreadyExists, RepoException

class RepoFileJucator:
    def __init__(self, filename):
        self.__players_list = []
        self.__filename = filename
        self.__load_from_file()

    def __load_from_file(self):
        with open(self.__filename, 'r') as file:
            lines = file.readlines()
            for line in lines:
                if line != "\n":
                    nume, tara, nr_meciuri, nr_victorii, nr_puncte = [i.strip() for i in line.split(",")]
                    p = Jucator(nume, tara, int(nr_meciuri), int(nr_victorii), int(nr_puncte))
                    self.__players_list.append(p)

    def store_player(self, player):
        """
        Adauga un nou jucator in lista
        """
        if self.find_player(player):
            raise AlreadyExists()
        self.__players_list.append(player)
        self.__save_to_file()

    def find_player(self, player: Jucator) -> bool:
        """
        Cauta un jucator in lista
        :param player: jucatorul cautat
        :return: True daca jucatorul e gasit, false altfel
        """
        for existing_player in self.__players_list:
            if existing_player == player:
                return True
        return False

    def __save_to_file(self):
        players = self.get_all()
        players = [player.nume + ',' + player.tara + ',' + str(player.nr_meciuri) + ',' + str(player.nr_victorii) + ','
                   + str(player.nr_puncte) for player in players]
        with open(self.__filename, 'w') as file:
            file.write('\n'.join(players))

    def get_all(self):
        return self.__players_list

    def size(self):
        return len(self.__players_list)
