import string
import random

from Domain.book import Book
from Exceptions.exceptions import BookNotFound
from Repository.InMemoryRepository.book_repo import BookRepository
from Domain.Validation.validator import BookValidator

class BookService:
    def __init__(self, repository: BookRepository, book_validator: BookValidator):
        self.__book_validator = book_validator
        self.__repository = repository

    def store_book(self, book_id: int, title: str, description: str, author: str):
        """
        Stores a book in the repository after validating its data.
        :param book_id: Unique identifier for the book.
        :param title: Title of the book.
        :param description: Description or synopsis of the book.
        :param author: Author of the book.
        :return: None
        """
        book = Book(book_id, title, description, author)
        self.__book_validator.book_data_validator(book)
        self.__repository.store_book(book)

    def update_book_by_id(self, book_id: int, title: str, description: str, author: str):
        """
        Updates the details of a book identified by its ID.
        :param book_id: The unique identifier of the book to be updated
        :param title: The new title of the book
        :param description: The new description for the book
        :param author: The name of the author of the book
        :return: A status or result from the repository indicating the success of
            the update operation
        """
        book = Book(book_id, title, description, author)
        self.__book_validator.book_data_validator(book)
        return self.__repository.update_book_by_id(book_id, title, description, author)

    def search_by_id(self, book_id: int):
        """
        Searches for a book in the repository based on its unique identifier.
        :param book_id: The unique ID of the book to be searched.
        :return: The book object matching the provided ID.
        :raises BookNotFound: If the book with the specified ID does not exist in the repository.
        """
        self.__book_validator.book_id_validator(book_id)
        book = self.__repository.find_by_id(book_id)
        if book is None:
            raise BookNotFound()
        return book

    @staticmethod
    def random_id():
        return random.randint(1, 100)

    @staticmethod
    def random_string():
        lenght = random.randrange(5, 40)
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for _ in range(lenght))

    def random_book(self):
        book = Book(self.random_id(), self.random_string(), self.random_string(), self.random_string())
        try:
            self.__repository.store_book(book)
        except book in self.get_all_books():
            self.random_book()

    def get_all_books(self):
        """
        :return: the list of books
        """
        return self.__repository.get_all()

    def size(self):
        return self.__repository.size()
