import unittest
from Controller.sorting import bubble_sort
from Controller.book_srv import BookService
from Controller.client_srv import ClientService
from Controller.rental_srv import RentalService
from Domain.Validation.validator import BookValidator, ClientValidator, RentalValidator
from Domain.book import Book
from Domain.client import Client
from Exceptions.exceptions import BookAlreadyExists, ValidationException, BookNotFound, ClientAlreadyExists, ClientNotFound, \
    RentAlreadyExists, RentNotFound
from Repository.FileRepository.book_file_repo import BookFileRepository
from Repository.FileRepository.client_file_repo import ClientFileRepository
from Repository.FileRepository.rent_file_repo import RentFileRepository
from Tests.file_utils import clear_file, copy_content

class TestBookService(unittest.TestCase):
    def setUp(self):
        clear_file("testbooks.txt")
        self.book_repo = BookFileRepository("testbooks.txt")
        self.book_validator = BookValidator()
        self.__test_booksrv = BookService(self.book_repo, self.book_validator)

    def test_store_book(self):
        self.__test_booksrv.store_book(1, "Twilight", "Serie de 5 carti cu vampiri", "Stephenie Meyer")
        self.assertEqual(self.__test_booksrv.size(), 1)

        self.__test_booksrv.store_book(2, "Iubita mea", "Poveste de viata", "Irina Binder")
        self.assertEqual(self.__test_booksrv.size(), 2)
        self.assertRaises(ValidationException, self.__test_booksrv.store_book, 3, "", "", "")
        self.assertRaises(BookAlreadyExists, self.__test_booksrv.store_book, 1, "ABC", "DCB", "XYZ")

    def test_update_book(self):
        self.__test_booksrv.store_book(1, "Twilight", "Serie de 5 carti cu vampiri", "Stephenie Meyer")
        self.__test_booksrv.store_book(2, "Iubita mea", "Poveste de viata", "Irina Binder")

        self.assertRaises(BookNotFound, self.__test_booksrv.update_book_by_id, 3, "a", "b", "c")
        self.assertRaises(ValidationException, self.__test_booksrv.update_book_by_id, -9, "", "", "")
        self.assertRaises(ValidationException, self.__test_booksrv.update_book_by_id, 2, "Abc", "", "Da")

        updatedbook = self.__test_booksrv.update_book_by_id(1, "ABC", "DCB", "XYZ")
        self.assertEqual(updatedbook.title, "ABC")
        self.assertEqual(updatedbook.description, "DCB")
        self.assertEqual(updatedbook.author, "XYZ")

    def test_find_book(self):
        self.__test_booksrv.store_book(1, "Twilight", "Serie de 5 carti cu vampiri", "Stephenie Meyer")
        self.__test_booksrv.store_book(2, "Iubita mea", "Poveste de viata", "Irina Binder")
        self.assertIsNotNone(self.__test_booksrv.search_by_id(1))
        self.assertIsNotNone(self.__test_booksrv.search_by_id(2))
        self.assertRaises(BookNotFound, self.__test_booksrv.search_by_id, 3)

    def test_random_book(self):
        self.__test_booksrv.random_book()
        books = self.__test_booksrv.get_all_books()
        self.assertEqual(len(books), 1)
        self.assertIsInstance(books[0], Book)

    def tearDown(self):
        clear_file("testbooks.txt")

class TestClientService(unittest.TestCase):
    def setUp(self):
        clear_file("testclients.txt")
        self.client_repo = ClientFileRepository("testclients.txt")
        self.client_validator = ClientValidator()
        self.__test_clientsrv = ClientService(self.client_repo, self.client_validator)

    def test_store_client(self):
        self.__test_clientsrv.store_client(1, "Iulia Dumitrache", "6010203562354")
        self.assertEqual(self.__test_clientsrv.size(), 1)

        self.__test_clientsrv.store_client(2, "Tudor Vladimir", "5020304235625")
        self.assertEqual(self.__test_clientsrv.size(), 2)
        self.assertRaises(ValidationException, self.__test_clientsrv.store_client, 3, "", "")
        self.assertRaises(ClientAlreadyExists, self.__test_clientsrv.store_client, 1, "ABC", "6010203562354")

    def test_update_client(self):
        self.__test_clientsrv.store_client(1, "Iulia Dumitrache", "6010203562354")
        self.__test_clientsrv.store_client(2, "Tudor Vladimir", "5020304235625")

        self.assertRaises(ClientNotFound, self.__test_clientsrv.update_client_by_id, 3, "a", "5020304235625")
        self.assertRaises(ValidationException, self.__test_clientsrv.update_client_by_id, -9, "", "")
        self.assertRaises(ValidationException, self.__test_clientsrv.update_client_by_id, 2, "Abc", "")

        updatedclient = self.__test_clientsrv.update_client_by_id(1, "ABC", "6030204897564")
        self.assertEqual(updatedclient.get_name(), "ABC")
        self.assertEqual(updatedclient.get_cnp(), "6030204897564")

    def test_find_client(self):
        self.__test_clientsrv.store_client(1, "Iulia Dumitrache", "6010203562354")
        self.__test_clientsrv.store_client(2, "Tudor Vladimir", "5020304235625")
        self.assertIsNotNone(self.__test_clientsrv.search_by_id(1))
        self.assertIsNotNone(self.__test_clientsrv.search_by_id(2))
        self.assertRaises(ClientNotFound, self.__test_clientsrv.search_by_id, 3)

    def test_random_client(self):
        self.__test_clientsrv.random_client()
        clients = self.__test_clientsrv.get_all_clients()
        self.assertEqual(len(clients), 1)
        self.assertIsInstance(clients[0], Client)

    def tearDown(self):
        clear_file("testclients.txt")

class TestRentService(unittest.TestCase):
    def setUp(self):
        copy_content("defaultbooks.txt", "testbooks.txt")
        copy_content("defaultclients.txt", "testclients.txt")
        copy_content("defaultrent.txt", "testrents.txt")
        self.rent_repo = RentFileRepository("testrents.txt")
        self.rent_validator = RentalValidator()
        self.book_repo = BookFileRepository("testbooks.txt")
        self.book_validator = BookValidator()
        self.client_repo = ClientFileRepository("testclients.txt")
        self.client_validator = ClientValidator()
        self.__test_rentsrv = RentalService(self.rent_repo, self.book_repo, self.client_repo, self.rent_validator,
                                            self.book_validator, self.client_validator)

    def test_store_rent(self):
        initialsize = self.rent_repo.size()
        self.__test_rentsrv.store_rental(16, 4, 5)
        self.assertEqual(self.rent_repo.size(), initialsize + 1)
        self.assertRaises(BookNotFound, self.__test_rentsrv.store_rental, 2, 100, 2)
        self.assertRaises(ClientNotFound, self.__test_rentsrv.store_rental, 3, 1, 200)
        self.assertRaises(ValidationException, self.__test_rentsrv.store_rental, -5, 1, 3)
        self.assertRaises(RentAlreadyExists, self.__test_rentsrv.store_rental, 1, 1, 1)

    def test_delete_rent(self):
        initialsize = self.rent_repo.size()
        deleted_rent = self.__test_rentsrv.delete_rental(15)
        self.assertEqual(self.__test_rentsrv.size(), initialsize - 1)
        self.assertEqual(deleted_rent.get_id_rental(), 15)
        self.assertEqual(deleted_rent.book_id, 3)
        self.assertEqual(deleted_rent.client_id, 9)
        self.assertRaises(ValidationException, self.__test_rentsrv.delete_rental, -1)
        self.assertRaises(RentNotFound, self.__test_rentsrv.delete_rental, 16)

    def test_delete_book_and_rent(self):
        self.assertRaises(BookNotFound, self.__test_rentsrv.delete_rent_and_book, 200)
        self.assertRaises(ValidationException, self.__test_rentsrv.delete_rent_and_book, -5)
        initialsize = self.rent_repo.size()
        deleted_book = self.__test_rentsrv.delete_rent_and_book(1)
        self.assertEqual(self.__test_rentsrv.size(), initialsize - 3)
        self.assertEqual(deleted_book.get_book_id(), 1)
        self.assertEqual(deleted_book.title, "Twilight")
        deleted_book = self.__test_rentsrv.delete_rent_and_book(5)
        self.assertEqual(self.__test_rentsrv.size(), initialsize - 4)
        self.assertEqual(deleted_book.get_book_id(), 5)
        self.assertEqual(deleted_book.title, "O viata secreta")

    def test_delete_client_and_rent(self):
        self.assertRaises(ClientNotFound, self.__test_rentsrv.delete_rent_and_client, 200)
        self.assertRaises(ValidationException, self.__test_rentsrv.delete_rent_and_client, -5)
        initialsize = self.rent_repo.size()
        deleted_client = self.__test_rentsrv.delete_rent_and_client(1)
        self.assertEqual(self.__test_rentsrv.size(), initialsize - 1)
        self.assertEqual(deleted_client.get_client_id(), 1)
        self.assertEqual(deleted_client.get_name(), "Ionescu Gabriela")
        deleted_client = self.__test_rentsrv.delete_rent_and_client(5)
        self.assertEqual(self.__test_rentsrv.size(), initialsize - 1)
        self.assertEqual(deleted_client.get_client_id(), 5)
        self.assertEqual(deleted_client.get_name(), "Ardelean David")

    def test_most_rented_books(self):
        """
        based on the current file content:
        These are the most rented books:
            Book Twilight written by Stephenie Meyer was rented 3 times.
            Book Wprkywmxdnpxwmmydw written by Pcbqetvigjheyag awvoutrwtudqvim was rented 3 times.
            Book It starts with us written by Colleen Hoover was rented 3 times.
            Book Portocalele verzi written by Vitali Cipileaga was rented 2 times.
            Book Vswblbsdjoo written by Yvcudrrxvpn ayvkdymsozlekapdorhu was rented 1 times.
            Book Bmrremtpxkxabwvfblkpovdkbznrtu written by Xowuvzqnno Dmcppnsrj was rented 1 times.
            Book Iubita mea written by Irina Binder was rented 1 times.
            Book O viata secreta written by Ella Carrey was rented 1 times.
          """
        dto_list = self.__test_rentsrv.most_rented_books()
        self.assertEqual(len(dto_list), 8)

        self.assertEqual(dto_list[0].title, "Twilight")
        self.assertEqual(dto_list[0].nr_rents, 3)

        self.assertEqual(dto_list[-1].title, "O viata secreta")
        self.assertEqual(dto_list[-1].nr_rents, 1)

        self.setsecundar()
        self.assertRaises(ValueError, self.__test_rentsrv.most_rented_books)

        self.setsecundar()
        self.__test_rentsrv.store_rental(1, 1, 1)
        self.__test_rentsrv.store_rental(2, 1, 2)
        dto = self.__test_rentsrv.most_rented_books()
        self.assertEqual(len(dto), 1)

    def test_name_clients_rents(self):
        """
        These are clients who have at least one book rented, sorted by name:
            Client: Ionescu Gabriela had rented the following books: Twilight.
            Client: Kzwd had rented the following books: O viata secreta.
            Client: Nnzelxvjn yhjsjr had rented the following books: Iubita mea, Portocalele verzi.
            Client: Priafg had rented the following books: Twilight, Wprkywmxdnpxwmmydw.
            Client: Teofil Robert had rented the following books: Portocalele verzi, Wprkywmxdnpxwmmydw.
            Client: Titu Ioan had rented the following books: Vswblbsdjoo.
            Client: Veres Laura had rented the following books: Twilight, It starts with us.
            Client: Whu hzjqlohu had rented the following books: It starts with us, Bmrremtpxkxabwvfblkpovdkbznrtu.
            Client: Xotrbuwf wcfmatvhhm had rented the following books: It starts with us, Wprkywmxdnpxwmmydw.
        """
        dto_list = self.__test_rentsrv.name_clients_rents()
        self.assertEqual(len(dto_list), 9)

        self.assertEqual(dto_list[0].name, "Ionescu Gabriela")
        self.assertEqual(dto_list[0].book_titles, ["Twilight"])

        self.assertEqual(dto_list[-1].name, "Xotrbuwf wcfmatvhhm")
        self.assertEqual(dto_list[-1].book_titles, ["It starts with us", "Wprkywmxdnpxwmmydw"])

        self.setsecundar()
        self.assertRaises(ValueError, self.__test_rentsrv.name_clients_rents)

        self.setsecundar()
        self.__test_rentsrv.store_rental(1, 1, 1)
        self.__test_rentsrv.store_rental(2, 1, 2)
        dto = self.__test_rentsrv.name_clients_rents()
        self.assertEqual(len(dto), 2)

    def test_books_number_clients(self):
        """
        These are clients who have at least one book rented, sorted by number of books:
            Client Veres Laura has 2 books.
            Client Priafg has 2 books.
            Client Whu hzjqlohu has 2 books.
            Client Teofil Robert has 2 books.
            Client Xotrbuwf wcfmatvhhm has 2 books.
            Client Nnzelxvjn yhjsjr has 2 books.
            Client Ionescu Gabriela has 1 books.
            Client Kzwd has 1 books.
            Client Titu Ioan has 1 books.
        """
        dto_list = self.__test_rentsrv.books_number_clients()
        self.assertEqual(len(dto_list), 9)

        self.assertEqual(dto_list[0].name, "Veres Laura")
        self.assertEqual(dto_list[0].nr_rents, 2)

        self.assertEqual(dto_list[-2].name, "Kzwd")
        self.assertEqual(dto_list[-2].nr_rents, 1)

        self.assertEqual(dto_list[-1].name, "Titu Ioan")
        self.assertEqual(dto_list[-1].nr_rents, 1)

        self.setsecundar()
        self.assertRaises(ValueError, self.__test_rentsrv.books_number_clients)

        self.setsecundar()
        self.__test_rentsrv.store_rental(1, 1, 1)
        dto = self.__test_rentsrv.books_number_clients()
        self.assertEqual(len(dto), 1)

    def test_most_active_clients(self):
        """
        These are the first 20% of clients who have at least one book rented, sorted by number of books:
            Client Veres Laura has 2 books.
        """
        dto_list = self.__test_rentsrv.most_active_clients()
        self.assertEqual(len(dto_list), 1)

        self.assertEqual(dto_list[0].name, "Veres Laura")
        self.assertEqual(dto_list[0].nr_rents, 2)

        clear_file("testrents.txt")
        copy_content("defaultrent.txt", "testrents.txt")
        self.rent_repo = RentFileRepository("testrents.txt")
        self.__test_rentsrv = RentalService(self.rent_repo, self.book_repo, self.client_repo, self.rent_validator,
                                            self.book_validator, self.client_validator)

        self.__test_rentsrv.store_rental(16, 4, 5)
        self.__test_rentsrv.store_rental(17, 11, 10)
        self.__test_rentsrv.store_rental(18, 11, 2)
        self.__test_rentsrv.store_rental(19, 11, 3)
        self.__test_rentsrv.store_rental(20, 7, 3)
        self.__test_rentsrv.store_rental(21, 4, 3)

        dto_list = self.__test_rentsrv.most_active_clients()
        self.assertEqual(len(dto_list), 2)

        self.assertEqual(dto_list[0].name, "Titu Ioan")
        self.assertEqual(dto_list[0].nr_rents, 4)

        self.assertEqual(dto_list[1].name, "Teofil Robert")
        self.assertEqual(dto_list[1].nr_rents, 3)

        self.setsecundar()
        self.assertRaises(ValueError, self.__test_rentsrv.most_active_clients)

    def test_least_rented_books(self):
        """
        These are the least rented books:
            Book O viata secreta written by Ella Carrey was rented once by Kzwd
            Book Iubita mea written by Irina Binder was rented once by Nnzelxvjn yhjsjr
            Book Bmrremtpxkxabwvfblkpovdkbznrtu written by Xowuvzqnno Dmcppnsrj was rented once by Whu hzjqlohu
            Book Vswblbsdjoo written by Yvcudrrxvpn ayvkdymsozlekapdorhu was rented once by Titu Ioan
        """
        dto_list = self.__test_rentsrv.least_rented_books()
        self.assertEqual(len(dto_list), 4)
        self.assertEqual(dto_list[0].title, "O viata secreta")
        self.assertEqual(dto_list[0].author, "Ella Carrey")
        self.assertEqual(dto_list[0].name, "Kzwd")

        self.assertEqual(dto_list[-1].title, "Vswblbsdjoo")
        self.assertEqual(dto_list[-1].author, "Yvcudrrxvpn ayvkdymsozlekapdorhu")
        self.assertEqual(dto_list[-1].name, "Titu Ioan")

        self.setsecundar()
        self.assertRaises(ValueError, self.__test_rentsrv.least_rented_books)

        self.setsecundar()
        self.__test_rentsrv.store_rental(1, 1, 1)
        self.__test_rentsrv.store_rental(2, 1, 2)
        dto = self.__test_rentsrv.least_rented_books()
        self.assertEqual(len(dto), 0)

    def setsecundar(self):
        clear_file("testrents.txt")
        self.rent_repo = RentFileRepository("testrents.txt")
        self.__test_rentsrv = RentalService(self.rent_repo, self.book_repo, self.client_repo, self.rent_validator,
                                            self.book_validator, self.client_validator)

    def tearDown(self):
        clear_file("testbooks.txt")
        clear_file("testclients.txt")
        clear_file("testrents.txt")
