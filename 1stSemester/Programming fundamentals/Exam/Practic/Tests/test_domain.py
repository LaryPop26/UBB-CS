import unittest

from domain.entitate import Automobil

class TestDomain(unittest.TestCase):
    def test_create(self):
        automobil = Automobil(1, "Audi", 500, "A4", "25:02:2024")
        self.assertEqual(automobil.id_a, 1)
        self.assertEqual(automobil.marca, "Audi")
        self.assertEqual(automobil.pret, 500)
        self.assertEqual(automobil.model, "A4")
        self.assertEqual(automobil.data, "25:02:2024")

