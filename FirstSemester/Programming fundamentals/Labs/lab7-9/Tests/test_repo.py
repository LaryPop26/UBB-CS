import unittest

from Domain.book import Book
from Domain.client import Client
from Domain.rental import Rental
from Exceptions.exceptions import BookNotFound, BookAlreadyExists, ClientAlreadyExists, ClientNotFound, RentAlreadyExists
from Repository.FileRepository.book_file_repo import BookFileRepository
from Repository.FileRepository.client_file_repo import ClientFileRepository
from Repository.FileRepository.rent_file_repo import RentFileRepository
from Tests.file_utils import clear_file

class TestBookRepository(unittest.TestCase):
    def setUp(self):
        clear_file("testbooks.txt")
        self.test_repo = BookFileRepository("testbooks.txt")

    def test_store_book(self):
        book = Book(1, "Twilight", "Serie de 5 carti cu vampiri", "Stephenie Meyer")
        self.test_repo.store_book(book)
        self.assertEqual(self.test_repo.size(), 1)
        self.assertRaises(BookAlreadyExists, self.test_repo.store_book, book)

    def test_find_book(self):

        book1 = Book(1, "Ehrb", "Atebdf", "Atnbdf")
        self.test_repo.store_book(book1)
        self.assertEqual(self.test_repo.size(), 1)

        self.assertIsNotNone(self.test_repo.find_by_id(1))
        self.assertIsNone(self.test_repo.find_by_id(20))

    def test_delete_book(self):
        self.assertEqual(self.test_repo.size(), 0)
        book1 = Book(1, "Twilight", "Serie de 5 carti cu vampiri", "Stephenie Meyer")
        book2 = Book(2, "Iubita mea", "Poveste de viata", "Irina Binder")
        book3 = Book(3, "Ehrb", "Atebdf", "Atnbdf")

        self.test_repo.store_book(book1)
        self.test_repo.store_book(book2)
        self.test_repo.store_book(book3)
        self.assertEqual(self.test_repo.size(), 3)

        deleted_book = self.test_repo.delete_book(1)
        self.assertEqual(self.test_repo.size(), 2)
        self.assertIsNone(self.test_repo.find_by_id(1))
        self.assertEqual(deleted_book.title, "Twilight")

        deleted_book = self.test_repo.delete_book(2)
        self.assertEqual(self.test_repo.size(), 1)
        self.assertIsNone(self.test_repo.find_by_id(2))
        self.assertEqual(deleted_book.title, "Iubita mea")

        book3 = Book(2, "Iubirea mea", "Poveste de viata", "Irina Binder")
        self.test_repo.store_book(book3)
        self.assertEqual(self.test_repo.size(), 2)

        deleted_book = self.test_repo.delete_book(2)
        self.assertEqual(self.test_repo.size(), 1)
        self.assertIsNone(self.test_repo.find_by_id(2))
        self.assertEqual(deleted_book.title, "Iubirea mea")
        self.assertRaises(BookNotFound, self.test_repo.delete_book, 2)

        self.test_repo.delete_book(3)
        self.assertEqual(self.test_repo.size(), 0)

        self.assertRaises(BookNotFound, self.test_repo.delete_book, 3)

    def test_update_book(self):
        self.assertEqual(self.test_repo.size(), 0)
        book1 = Book(1, "Ehrb", "Atebdf", "Atnbdf")
        self.test_repo.store_book(book1)
        self.assertEqual(self.test_repo.size(), 1)

        updated_book = self.test_repo.update_book_by_id(1, "haha", "HIHI", "HUHU")
        self.assertEqual(updated_book.title, "haha")
        self.assertEqual(updated_book.description, "HIHI")
        self.assertEqual(updated_book.author, "HUHU")

        self.assertRaises(BookNotFound, self.test_repo.update_book_by_id, 10, "haha", "HIHI", "HUHU")

    def tearDown(self):
        clear_file("testbooks.txt")

class TestClientRepository(unittest.TestCase):
    def setUp(self):
        clear_file("testclients.txt")
        self.test_repo = ClientFileRepository("testclients.txt")

    def test_store_client(self):
        client = Client(1, "Ionescu Gabriela", "6040203562362")
        self.test_repo.store_client(client)
        self.assertEqual(self.test_repo.size(), 1)
        self.assertRaises(ClientAlreadyExists, self.test_repo.store_client, client)
        self.assertEqual(self.test_repo.size(), 1)

    def test_find_client(self):
        self.assertEqual(self.test_repo.size(), 0)

        client = Client(1, "Ionescu Gabriela", "6040203562362")
        self.test_repo.store_client(client)
        self.assertEqual(self.test_repo.size(), 1)

        self.assertIsNotNone(self.test_repo.find_by_id(1))
        self.assertIsNone(self.test_repo.find_by_id(20))

    def test_delete_client(self):
        self.assertEqual(self.test_repo.size(), 0)
        client1 = Client(1, "Ionescu Gabriela", "6040203562362")
        client2 = Client(2, "Tomescu Briana", "6090405326452")
        client3 = Client(3, "Toma Ion", "5090405326452")

        self.test_repo.store_client(client1)
        self.test_repo.store_client(client2)
        self.test_repo.store_client(client3)
        self.assertEqual(self.test_repo.size(), 3)

        deleted_client = self.test_repo.delete_client(1)
        self.assertEqual(self.test_repo.size(), 2)
        self.assertIsNone(self.test_repo.find_by_id(1))
        self.assertEqual(deleted_client.get_name(), "Ionescu Gabriela")

        deleted_client = self.test_repo.delete_client(2)
        self.assertEqual(self.test_repo.size(), 1)
        self.assertIsNone(self.test_repo.find_by_id(2))
        self.assertEqual(deleted_client.get_name(), "Tomescu Briana")

        client2 = Client(2, "Tomescu Briana", "6090405326452")
        self.test_repo.store_client(client2)
        self.assertEqual(self.test_repo.size(), 2)

        deleted_client = self.test_repo.delete_client(2)
        self.assertEqual(self.test_repo.size(), 1)
        self.assertIsNone(self.test_repo.find_by_id(2))
        self.assertEqual(deleted_client.get_name(), "Tomescu Briana")

        self.test_repo.delete_client(3)
        self.assertEqual(self.test_repo.size(), 0)

        self.assertRaises(ClientNotFound, self.test_repo.delete_client, 3)

    def test_update_client(self):
        self.assertEqual(self.test_repo.size(), 0)
        client1 = Client(1, "Ionescu Gabriela", "6040203562362")
        self.test_repo.store_client(client1)
        self.assertEqual(self.test_repo.size(), 1)

        updated_client = self.test_repo.update_client_by_id(1, "haha", "602030452631")
        self.assertEqual(updated_client.get_name(), "haha")
        self.assertEqual(updated_client.get_cnp(), "602030452631")

        self.assertRaises(ClientNotFound, self.test_repo.update_client_by_id, 10, "haha", "602030452631")

    def tearDown(self):
        clear_file("testclients.txt")

class TestRentRepository(unittest.TestCase):
    def setUp(self):
        clear_file("testrents.txt")
        self.test_repo = RentFileRepository("testrents.txt")

    def test_store_rent(self):
        rent = Rental(1, 1, 1)
        self.test_repo.store_rent(rent)
        self.assertEqual(self.test_repo.size(), 1)
        self.assertEqual(rent.book_id, 1)
        self.assertEqual(rent.client_id, 1)
        self.assertRaises(RentAlreadyExists, self.test_repo.store_rent, Rental(1, 2, 1))
        self.assertEqual(self.test_repo.size(), 1)

    def test_find_rent(self):
        rent = Rental(1, 1, 1)
        self.test_repo.store_rent(rent)

        self.assertIsNotNone(self.test_repo.find_rent_by_id(1))
        self.assertIsNone(self.test_repo.find_rent_by_id(2))

    def test_delete_rent(self):
        self.assertEqual(self.test_repo.size(), 0)

    def tearDown(self):
        clear_file("testrents.txt")
