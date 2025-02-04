import unittest

from Domain.booking import BookingInquiry
from Domain.locatie import Locatie

class TestsLocatieDomain(unittest.TestCase):
    def setUp(self):
        pass

    def test_create_locatie(self):
        l = Locatie(1, "La Ionel", "munte", 85)
        self.assertEqual(l.id_locatie, 1)
        self.assertEqual(l.denumire, "La Ionel")
        self.assertEqual(l.tip, "munte")
        self.assertEqual(l.pret_pe_zi, 85)

    def test_str_locatie(self):
        l = Locatie(1, "La Ionel", "munte", 85)
        self.assertEqual(str(l), "Locatie 1 | Denumire La Ionel | Tip munte | Pret Pe Zi 85")

    def test_creaate_booking(self):
        l = Locatie(1, "La Ionel", "munte", 85)
        b = BookingInquiry(l, 500)
        self.assertEqual(b.locatie.id_locatie, 1)
        self.assertEqual(b.locatie.denumire, "La Ionel")
        self.assertEqual(b.locatie.tip, "munte")
        self.assertEqual(b.locatie.pret_pe_zi, 85)
        self.assertEqual(b.buget, 500)

    def test_str_booking(self):
        l = Locatie(1, "La Ionel", "munte", 85)
        b = BookingInquiry(l, 500)
        self.assertEqual(str(b), "Locatie La Ionel | Tip munte | Nr zile 5")
