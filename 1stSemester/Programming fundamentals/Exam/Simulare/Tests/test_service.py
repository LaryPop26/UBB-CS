import unittest

from Controller.locatie_srv import LocatieSrv, ServiceError
from Domain.validator import Validator, ValidatorError
from Repository.locatie_repo import LocatieFileRepo

class TestService(unittest.TestCase):
    def setUp(self):
        self.test_repo = LocatieFileRepo("test_locatii.txt")
        self.validator = Validator()
        self.__test_srv = LocatieSrv(self.test_repo, self.validator)

    def test_cauta_locatii_dupa_tip(self):
        locatii = self.__test_srv.cauta_locatii_dupa_tip("munte")
        self.assertEqual(len(locatii), 2)

        self.assertRaises(ValidatorError, self.__test_srv.cauta_locatii_dupa_tip, "")

    def test_rezervare(self):
        self.assertRaises(ValidatorError, self.__test_srv.rezervare, -1, -2)
        self.assertRaises(ServiceError, self.__test_srv.rezervare, 100, 2)
        rezervare = self.__test_srv.rezervare(1, 100)
        self.assertEqual(rezervare.get_number_of_days(), 1)
        self.assertEqual(rezervare.locatie.denumire, "La Ionel")

    def tearDown(self):
        pass
