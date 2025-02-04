import unittest

from Controller.srv_tractor import SrvTractor
from Domain.validator import Validator, ValidationError
from Repository.repo_tractor import RepoTractor
from Utils.file_utils import clear_file

class TestSrv(unittest.TestCase):
    def setUp(self):
        clear_file('tractoare_test.txt')
        self.test_repo = RepoTractor('tractoare_test.txt')
        self.validator = Validator()
        self.test_srv = SrvTractor(self.test_repo, self.validator, [])

    def test_adaugare(self):
        self.test_srv.adaugare(11, "dafdvd", 500, "ac", "16:02:2022")
        self.assertEqual(self.test_srv.size(), 1)
        self.assertRaises(ValidationError, self.test_srv.adaugare, -1, "", -6, "", "12")

    def test_stergere(self):
        self.test_srv.adaugare(11, "dafdvd", 500, "ac", "16:02:2022")
        self.test_srv.adaugare(12, "gswges", 1235, "sg", "10:10:2019")
        self.assertEqual(self.test_srv.size(), 2)
        self.test_srv.stergere(5)
        self.assertEqual(self.test_srv.size(), 1)
        self.test_srv.stergere(9)
        self.assertEqual(self.test_srv.size(), 1)

    def test_filtrare(self):
        self.test_srv.adaugare(1, "papapm", 1000, "teren", "25:10:2020")
        self.test_srv.adaugare(2, "akc", 2500, "teren arabil", "12:02:2025")
        self.test_srv.adaugare(3, "abbba", 600, "agronom", "02:06:2022")
        self.test_srv.adaugare(4, "dada", 500, "mobil", "16:04:2026")
        self.test_srv.adaugare(5, "fafa", 3000, "mare", "18:11:2028")
        self.test_srv.adaugare(6, "gagggag", 1858, "mic", "16:10:2000")
        self.test_srv.adaugare(7, "ffaaafaf", 3256, "imens", "26:04:2023")

        lista = self.test_srv.get_all_srv()
        self.assertEqual(len(lista), 7)
        lista1 = self.test_srv.filtrare('k', 6000)
        self.assertEqual(len(lista1), 1)
        self.assertEqual(lista1[0].id_t, 2)
        lista2 = self.test_srv.filtrare('', -1)
        self.assertEqual(len(lista2), 7)
        lista3 = self.test_srv.filtrare('', 1000)
        self.assertEqual(len(lista3), 2)
        lista4 = self.test_srv.filtrare('da', -1)
        self.assertEqual(len(lista4), 1)

    def test_undo(self):
        self.assertEqual(self.test_srv.size(),0)
        self.test_srv.adaugare(1, "papapm", 1000, "teren", "25:10:2020")
        self.assertEqual(self.test_srv.size(), 1)
        self.test_srv.stergere(1)
        self.assertEqual(self.test_srv.size(), 0)
        self.test_srv.undo()
        self.assertEqual(self.test_srv.size(), 1)
        self.test_srv.adaugare(1, "papapm", 1000, "teren", "25:10:2020")
        self.assertEqual(self.test_srv.size(), 2)
        self.test_srv.undo()
        self.assertEqual(self.test_srv.size(), 1)
        self.assertRaises(Exception, self.test_srv.undo)

    def tearDown(self):
        clear_file('tractoare_test.txt')
