import shutil
import unittest

from Domain.jucator import Jucator
from Exceptions.exceptions import AlreadyExists
from Repository.repo_jucator import RepoFileJucator

class TestRepository(unittest.TestCase):
    def setUp(self):
        self.test_repo = RepoFileJucator("test_players.txt")

    def test_store(self):
        self.assertEqual(self.test_repo.size(), 0)
        p = Jucator("Rafael Nadal", "Spain", 1285, 1120, 12400)
        self.test_repo.store_player(p)
        self.assertEqual(self.test_repo.size(), 1)

        p2 = Jucator("Rafael Nadal", "Spain", 1285, 1200, 12500)
        self.assertRaises(AlreadyExists, self.test_repo.store_player, p2)
        self.assertEqual(self.test_repo.size(), 1)

    def test_find(self):
        pass

    def tearDown(self):
        with open("test_players.txt", "w"):
            pass
