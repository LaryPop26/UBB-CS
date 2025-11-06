import unittest

from controller.service import SrvAutomobil
from domain.validator import Validator, ValidatorError
from repository.repository import RepoAutomobil
from utils.file_utils import clear_file

class TestSrv(unittest.TestCase):
    def setUp(self):
        clear_file('automobil_test.txt')
        self.test_repo = RepoAutomobil('automobil_test.txt')
        self.test_validator = Validator()
        self.test_srv = SrvAutomobil(self.test_repo, self.test_validator, [])

    def test_adaugare(self):
        self.test_srv.adaugare(1, "Audi", 500, "RS", "25:02:2025")
        self.assertEqual(self.test_srv.size(), 1)
        self.assertRaises(ValidatorError, self.test_srv.adaugare, -1, "", -5, "", "")

    def test_stergere(self):
        self.test_srv.adaugare(1, "Audi", 500, "RS", "25:02:2025")
        self.assertEqual(self.test_srv.size(), 1)
        self.assertEqual(self.test_srv.stergere(5), 1)
        self.assertEqual(self.test_srv.size(), 0)

    def test_filtrare(self):
        self.test_srv.adaugare(1, "Audi", 1550, "RS3", "25:02:2025")
        self.test_srv.adaugare(2, "Audi", 2000, "A4", "16:12:2025")
        self.test_srv.adaugare(3, "Renault", 1000, "Laguna", "14:02:2025")
        self.test_srv.adaugare(4, "Renault", 1500, "Megane", "25:01:2025")
        self.test_srv.adaugare(5, "Mercedes", 3000, "AClass", "16:03:2026")
        self.test_srv.adaugare(6, "Honda", 500, "Civic", "30:07:2028")
        self.test_srv.adaugare(7, "Toyota", 900, "Corolla", "03:05:2020")
        self.test_srv.adaugare(8, "BMW", 1200, "M4", "05:05:2019")
        self.test_srv.adaugare(9, "Toyota", 2395, "CH - R", "16:06:2021")
        self.test_srv.adaugare(10, "Bugatti", 125632, "Chiron", "18:12:2029")

        lista = self.test_srv.get_all()
        self.assertEqual(len(lista), 10)
        lista1 = self.test_srv.filtrare("Ren", 1200)
        self.assertEqual(len(lista1), 1)
        lista2 = self.test_srv.filtrare("Aud", -1)
        self.assertEqual(len(lista2), 2)
        lista3 = self.test_srv.filtrare("", 1200)
        self.assertEqual(len(lista3), 3)
        lista4 = self.test_srv.filtrare("", -1)
        self.assertEqual(len(lista4), 10)

    def test_undo(self):
        self.assertEqual(self.test_srv.size(), 0)
        self.test_srv.adaugare(1, "Audi", 1550, "RS3", "25:02:2025")
        self.assertEqual(self.test_srv.size(), 1)
        self.test_srv.stergere(5)
        self.assertEqual(self.test_srv.size(), 0)
        self.test_srv.undo()
        self.assertEqual(self.test_srv.size(), 1)
        self.test_srv.adaugare(2, "Audi", 1550, "RS3", "25:02:2025")
        self.assertEqual(self.test_srv.size(), 2)
        self.test_srv.undo()
        self.assertEqual(self.test_srv.size(), 1)

    def tearDown(self):
        clear_file('automobil_test.txt')
