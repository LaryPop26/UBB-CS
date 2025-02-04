import unittest

from Repository.locatie_repo import LocatieFileRepo

class TestRepository(unittest.TestCase):
    def setUp(self):
        self.test_repo = LocatieFileRepo("test_locatii.txt")

    def test_cauta_dupa_id(self):
        self.assertIsNotNone(self.test_repo.cauta_dupa_id(1))
        self.assertIsNone(self.test_repo.cauta_dupa_id(100))

    def tearDown(self):
        pass

