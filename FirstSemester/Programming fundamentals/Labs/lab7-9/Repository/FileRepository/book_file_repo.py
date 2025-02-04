from Domain.book import Book
from Repository.InMemoryRepository.book_repo import BookRepository

class BookFileRepository(BookRepository):
    def __init__(self, filename):
        super().__init__()
        self.__filename = filename
        self.__load_from_file()

    def __load_from_file(self) -> None:
        """
        Private method for loading book data from a file into the repository. This
        method reads all lines from a specified file, processes non-empty lines
        to extract book information, and adds the extracted book data into the
        repository.

        :raises ValueError: If the data in the file does not match the expected
            format or fails during conversion.
        """
        f = open(self.__filename, 'r')
        try:
            lines = [line.strip() for line in f.readlines() if line.strip() != '']
            for line in lines:
                book_id, title, description, author = line.split(',')
                super().store_book(Book(int(book_id), title, description, author))
        finally:
            f.close()

    def store_book(self, book: Book):
        """
        Store a book in the system and persist it to the file system.

        :param book: The book object to be stored.
        :return: None
        """
        super().store_book(book)
        self.__write_to_file()

    def delete_book(self, book_id: int) -> Book:
        """
        Deletes a book from the system and updates the associated file storage.

        :param book_id: The unique identifier of the book to be deleted.
        :return: The deleted book object, typically provided by the parent class's
            delete_book method.
        """
        deleted_book = super().delete_book(book_id)
        self.__write_to_file()
        return deleted_book

    def update_book_by_id(self, book_id: int, title: str, description: str, author: str) -> object:
        """
        Updates a book's information by its unique identifier.
        :param book_id: The unique identifier for the book to be updated.
        :param title: The updated title of the book.
        :param description: The updated description of the book.
        :param author: The updated author name for the book.
        :return: A dictionary or object representation of the updated book with
            the updated details reflected.
        """
        updated_book = super().update_book_by_id(book_id, title, description, author)
        self.__write_to_file()
        return updated_book

    def __write_to_file(self):
        """
        Writes the list of books to a file in a specific format.

        Raises exceptions in case the file cannot be opened or written.
        :raises OSError: If the file cannot be opened or written.
        :return: None
        """
        books = [str(book.get_book_id()) + ',' + book.title + ',' + book.description + ',' + book.author
                 for book in super().get_all()]
        f = open(self.__filename, 'w')
        try:
            f.writelines('\n'.join(books))
        finally:
            f.close()
