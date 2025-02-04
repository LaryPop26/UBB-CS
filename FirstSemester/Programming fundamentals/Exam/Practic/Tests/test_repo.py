import unittest

from domain.entitate import Automobil
from repository.repository import RepoAutomobil
from utils.file_utils import clear_file

class TestRepo(unittest.TestCase):
    def setUp(self):
        clear_file('automobil_test.txt')
        self.__test_repo = RepoAutomobil('automobil_test.txt')

    def test_adaugare(self):
        a = Automobil(1,"Audi", 500, "RS", "15:02:2025")
        self.__test_repo.adaugare(a)
        self.assertEqual(self.__test_repo.size(), 1)

    def test_stergere(self):
        a = Automobil(1, "Audi", 500, "RS", "15:02:2025")
        self.__test_repo.adaugare(a)
        self.assertEqual(self.__test_repo.size(), 1)
        self.__test_repo.stergere(5)

    def tearDown(self):
        clear_file('automobil_test.txt')
