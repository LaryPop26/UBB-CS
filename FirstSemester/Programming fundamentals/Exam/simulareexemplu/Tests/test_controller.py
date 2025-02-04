import shutil
import unittest

from Controller.srv_jucator import SrvJucator
from Domain.validator import Validator
from Exceptions.exceptions import ValidationError, NoInput
from Repository.repo_jucator import RepoFileJucator

class TestController(unittest.TestCase):
    def setUp(self):
        shutil.copy("default_jucatori.txt", "test_players.txt")
        self.test_repo = RepoFileJucator("test_players.txt")
        self.test_validator = Validator()
        self.__test_srv = SrvJucator(self.test_repo, self.test_validator)

    def test_store(self):
        initialsize = self.__test_srv.size()
        self.assertEqual(self.__test_srv.size(), initialsize)
        self.__test_srv.store("Rafael Nadal", "Spain", 1285, 1120, 12400)
        self.assertEqual(self.__test_srv.size(), initialsize + 1)
        self.assertRaises(ValidationError, self.__test_srv.store, "", "", -6, -1, -2)

    def test_all_players(self):
        players = self.__test_srv.all_players_with_score_higher_than("Spain", 100)
        self.assertEqual(len(players), 1)

        with open("test_players.txt", "w"):
            pass
        self.test_repo = RepoFileJucator("test_players.txt")
        self.__test_srv = SrvJucator(self.test_repo, self.test_validator)

        self.assertRaises(NoInput, self.__test_srv.all_players_with_score_higher_than, "Spain", 100)

    def test_procentaj(self):

        """
        Nume: Daniil Medvedev | Tara: Russia | Numar meciuri: 725 | Numar victorii: 650 | Numar punncte: 7280 | Procentaj: 89.65517241379311
Nume: Carlos Alcaraz | Tara: Spain | Numar meciuri: 172 | Numar victorii: 150 | Numar punncte: 8945 | Procentaj: 87.20930232558139
Nume: Rafael Nadal | Tara: Spain | Numar meciuri: 1285 | Numar victorii: 1120 | Numar punncte: 12400 | Procentaj: 87.15953307392996
Nume: Andrey Rublev | Tara: Russia | Numar meciuri: 440 | Numar victorii: 380 | Numar punncte: 4745 | Procentaj: 86.36363636363636
Nume: Casper Ruud | Tara: Norway | Numar meciuri: 360 | Numar victorii: 310 | Numar punncte: 4360 | Procentaj: 86.11111111111111
Nume: Stefanos Tsitsipas | Tara: Greece | Numar meciuri: 500 | Numar victorii: 420 | Numar punncte: 4630 | Procentaj: 84.0
Nume: Taylor Fritz | Tara: USA | Numar meciuri: 315 | Numar victorii: 260 | Numar punncte: 3960 | Procentaj: 82.53968253968253
Nume: Alexander Zverev | Tara: Germany | Numar meciuri: 620 | Numar victorii: 510 | Numar punncte: 4465 | Procentaj: 82.25806451612904
Nume: Jannik Sinner | Tara: Italy | Numar meciuri: 280 | Numar victorii: 230 | Numar punncte: 4900 | Procentaj: 82.14285714285714
Nume: Roger Federer | Tara: Switzerland | Numar meciuri: 1526 | Numar victorii: 1250 | Numar punncte: 11275 | Procentaj: 81.91349934469201

        """
        procentaj = self.__test_srv.procent_descrescator()

        self.assertEqual(self.__test_srv.size(), 9)

        self.assertEqual(procentaj[0].nume, "Daniil Medvedev")
        self.assertEqual(procentaj[0].tara, "Russia")
        self.assertEqual(procentaj[0].procentaj, 89.65517241379311)

        self.assertEqual(procentaj[-1].nume, "Roger Federer")
        self.assertEqual(procentaj[-1].tara, "Switzerland")
        self.assertEqual(procentaj[-1].procentaj, 81.91349934469201)

        with open("test_players.txt", "w"):
            pass
        self.test_repo = RepoFileJucator("test_players.txt")
        self.__test_srv = SrvJucator(self.test_repo, self.test_validator)
        self.assertRaises(NoInput, self.__test_srv.procent_descrescator)

    def tearDown(self):
        with open("test_players.txt", "w"):
            pass
