class JucatorDTO:
    def __init__(self, player, procentaj):
        self.__player = player
        self.__procentaj = procentaj

    @property
    def player(self):
        return self.__player

    @property
    def procentaj(self):
        return self.__procentaj

    def __eq__(self, other):
        if type(other) != type(self):
            return False
        return self.player.nume == other.player.nume and self.player.tara == other.player.tara

    def __str__(self):
        return ("Nume: " + self.__player.nume + " | Tara: " + self.__player.tara + " | Numar meciuri: "
                + str(self.__player.nr_meciuri) + " | Numar victorii: " + str(self.__player.nr_victorii)
                + " | Numar punncte: " + str(self.__player.nr_puncte) + " | Procentaj: " + str(self.__procentaj))
