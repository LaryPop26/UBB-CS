import unittest

from Domain.tractor import Tractor
from Repository.repo_tractor import RepoTractor
from Utils.file_utils import clear_file

class TestRepo(unittest.TestCase):
    def setUp(self):
        clear_file('tractoare_test.txt')
        self.test_repo = RepoTractor('tractoare_test.txt')

    def test_adaugare(self):
        tractor = Tractor(10, "afvse", 600, "csd", "12:02:2025")
        self.test_repo.adaugare(tractor)
        self.assertEqual(self.test_repo.size(), 1)

    def test_stergere(self):
        self.assertEqual(self.test_repo.size(), 0)
        t1 = Tractor(1, "afvse", 600, "csd", "12:02:2025")
        t2 = Tractor(2, "dacc", 1500, "scd", "12:10:2025")

        self.test_repo.adaugare(t1)
        self.test_repo.adaugare(t2)
        self.assertEqual(self.test_repo.size(), 2)

        self.test_repo.stergere(6)
        self.assertEqual(self.test_repo.size(), 1)

        self.test_repo.stergere(3)
        self.assertEqual(self.test_repo.size(), 1)

    def tearDown(self):
        clear_file('tractoare_test.txt')
