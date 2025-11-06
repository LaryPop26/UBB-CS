import unittest

from Domain.dto import JucatorDTO
from Domain.jucator import Jucator

class TestsDomain(unittest.TestCase):
    def setUp(self):
        pass

    def test_create_player(self):
        p = Jucator("Rafael Nadal", "Spain", 1285, 1120, 12400)
        self.assertEqual(p.nume, "Rafael Nadal")
        self.assertEqual(p.tara, "Spain")
        self.assertEqual(p.nr_meciuri, 1285)
        self.assertEqual(p.nr_victorii, 1120)
        self.assertEqual(p.nr_puncte, 12400)

        p.nume = "Roger Federer"
        self.assertEqual(p.nume, "Roger Federer")
        p.tara = "Germany"
        self.assertEqual(p.tara, "Germany")
        p.nr_meciuri = 1526
        self.assertEqual(p.nr_meciuri, 1526)
        p.nr_victorii = 1250
        self.assertEqual(p.nr_victorii, 1250)
        p.nr_puncte = 11275
        self.assertEqual(p.nr_puncte, 11275)

    def test_eq_player(self):
        p1 = Jucator("Rafael Nadal", "Spain", 1285, 1120, 12400)
        p2 = Jucator("Roger Federer", "Germany", 1285, 1120, 12400)
        self.assertNotEqual(p1, p2)

        p3 = Jucator("Rafael Nadal", "Spain", 1285, 1120, 12400)
        self.assertEqual(p1, p3)

        p4 = Jucator("Alexander Zverev", "Spain", 620, 510, 4465)
        self.assertNotEqual(p1, p4)

        p5 = 1
        self.assertNotEqual(p5, p1)

    def test_str_player(self):
        p1 = Jucator("Rafael Nadal", "Spain", 1285, 1120, 12400)
        self.assertEqual(str(p1),
                         "Nume: Rafael Nadal | Tara: Spain | Numar meciuri: 1285 | Numar victorii: 1120 | Numar punncte: 12400")

    def test_create_dto(self):
        p = Jucator("Rafael Nadal", "Spain", 1285, 1120, 12400)
        d = JucatorDTO(p, (1120/1285)*100)
        self.assertEqual(d.player.nume, "Rafael Nadal")
        self.assertEqual(d.player.tara, "Spain")
        self.assertEqual(d.player.nr_meciuri, 1285)
        self.assertEqual(d.player.nr_victorii, 1120)
        self.assertEqual(d.player.nr_puncte, 12400)
        self.assertEqual(d.procentaj, (1120/1285)*100)

    def test_eq_dto(self):
        p1 = Jucator("Rafael Nadal", "Spain", 1285, 1120, 12400)
        p2 = Jucator("Roger Federer", "Germany", 1285, 1120, 12400)
        d1 = JucatorDTO(p1, (1120/1285)*100)
        d2 = JucatorDTO(p2, (1120/1285)*100)
        self.assertNotEqual(d1, d2)

        p3 = Jucator("Rafael Nadal", "Spain", 1110, 1000, 12400)
        d3 = JucatorDTO(p3, (1000/1110)*100)
        self.assertEqual(d1, d3)

        d4 = 1
        self.assertNotEqual(d4, d1)

    def test_str_dto(self):
        p1 = Jucator("Rafael Nadal", "Spain", 1285, 1120, 12400)
        d1 = JucatorDTO(p1, (1120/1285)*100)
        self.assertEqual(str(d1),
                         "Nume: Rafael Nadal | Tara: Spain | Numar meciuri: 1285 | Numar victorii: 1120 | "
                         "Numar punncte: 12400 | Procentaj: 87.15953307392996")

    def tearDown(self):
        pass
