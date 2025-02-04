from Domain.dto import JucatorDTO
from Domain.jucator import Jucator
from Exceptions.exceptions import NoInput

class SrvJucator:
    def __init__(self, repo, validator):
        self.__repo = repo
        self.__validator = validator

    def store(self, nume, tara, nr_meciuri, nr_victorii, nr_puncte):
        p = Jucator(nume, tara, nr_meciuri, nr_victorii, nr_puncte)
        self.__validator.player_validator(p)
        self.__repo.store_player(p)

    def all_players_with_score_higher_than(self, tara, punctaj):
        if self.size() == 0:
            raise NoInput
        # jucatori = []
        # players = self.__repo.get_all()
        # for player in players:
        #     if player.tara == tara:
        #         if player.nr_puncte > punctaj:
        #             jucatori.append(player)

        jucatori = [player for player in self.__repo.get_all() if player.tara == tara and player.nr_puncte > punctaj]
        return jucatori

    def procent_descrescator(self):
        if self.size() == 0:
            raise NoInput
        players = self.__repo.get_all()
        procent = {}
        for player in players:
            procentaj = (player.nr_victorii / player.nr_meciuri) * 100
            procent[player.nume] = JucatorDTO(player, procentaj)
        sorted_dto = sorted(procent.values(), key=lambda dto: dto.procentaj, reverse=True)
        return sorted_dto

    def get_all(self):
        return self.__repo.get_all()

    def size(self):
        return self.__repo.size()
