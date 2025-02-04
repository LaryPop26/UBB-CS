import unittest

from Domain.book import Book
from Domain.client import Client
from Domain.rental import Rental

class TestBook(unittest.TestCase):
    def test_create_book(self):
        book = Book(1, "Twilight", "Viata unor vampiri", "Stephenie Meyer")
        self.assertEqual(book.get_book_id(), 1)
        self.assertEqual(book.title, "Twilight")
        self.assertEqual(book.description, "Viata unor vampiri")
        self.assertEqual(book.author, "Stephenie Meyer")

        book.title = "It was a day"
        self.assertEqual(book.title, "It was a day")
        book.description = "Biography"
        self.assertEqual(book.description, "Biography")
        book.author = "Him Timber"
        self.assertEqual(book.author, "Him Timber")

    def test_eq_book(self):
        book1 = Book(1, "Twilight", "Viata unor vampiri", "Stephenie Meyer")
        book2 = Book(1, "Iubita mea", "Poveste de viata", "Irina Binder")
        self.assertEqual(book1, book2)

        book3 = Book(2, "Iubita mea", "Poveste de viata", "Irina Binder")
        self.assertNotEqual(book1, book3)

    def test_str(self):
        book1 = Book(1, "Twilight", "Serie de 5 carti cu vampiri", "Stephenie Meyer")
        self.assertEqual(str(book1), "[32mID: 1 | [34mTitle: Twilight "
                                     "| [36mDescription: Serie de 5 carti cu vampiri | [35mAuthor: Stephenie Meyer[0m")


class TestClients(unittest.TestCase):
    def test_create_client(self):
        client = Client(1, "Ionescu Gabriela", "6030415966685")
        self.assertEqual(client.get_client_id(), 1)
        self.assertEqual(client.get_name(), "Ionescu Gabriela")
        self.assertEqual(client.get_cnp(), "6030415966685")

        client.set_name("Tomescu Briana")
        client.set_cnp("6090405326452")
        self.assertEqual(client.get_name(), "Tomescu Briana")
        self.assertEqual(client.get_cnp(), "6090405326452")

    def test_eq_client(self):
        client1 = Client(1, "Ionescu Gabriela", "6030415966685")
        client2 = Client(1, "Tomescu Briana", "6090405326452")
        self.assertEqual(client1, client2)

        client3 = Client(2, "Tomescu Briana", "6090405326452")
        self.assertNotEqual(client1, client3)

    def test_str(self):
        client1 = Client(1, "Ionescu Gabriela", "6030415966685")
        self.assertEqual(str(client1), "ID: 1 | [34mName: Ionescu Gabriela | [36mCNP: 6030415966685[0m")


class TestRent(unittest.TestCase):
    def test_create_rent(self):
        rent = Rental(1, 1, 1)
        self.assertEqual(rent.get_id_rental(), 1)
        self.assertEqual(rent.book_id, 1)
        self.assertEqual(rent.client_id, 1)

    def test_eq_rent(self):
        rent1 = Rental(1, 1, 1)
        rent2 = Rental(1, 1, 1)
        self.assertEqual(rent1, rent2)

        rent3 = Rental(2, 2, 1)
        self.assertNotEqual(rent1, rent3)

    def test_str(self):
        rent1 = Rental(1, 1, 1)
        self.assertEqual(str(rent1), "[32mRent ID: 1: [36mBook 1 rent by [35mClient 1[0m")
