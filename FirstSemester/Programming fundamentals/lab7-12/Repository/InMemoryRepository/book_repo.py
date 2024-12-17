from Domain.book import Book
from Exceptions.exceptions import BookNotFound, BookAlreadyExists

class BookRepository:
    def __init__(self):
        self.__book_list = []

    def store_book(self, book: Book) -> None:
        """
        Stores a book in the repository if it does not already exist.
        :param book: Book instance to be stored in the repository.
        :raises BookAlreadyExists: If the provided book already exists in the
            repository.
        """
        # if book.get_book_id() == 0:
        #     for index in range(len(self.__book_list)):
        #         if index + 1 != self.__book_list[index].getId():
        #             BookRepository.id = index + 1
        #             break
        #         if index == len(self.__book_list):
        #             BookRepository.id = index + 1
        #     book.set_book_id(BookRepository.id)
        if self.find(book):
            raise BookAlreadyExists()
        self.__book_list.append(book)

    def delete_book(self, book_id: int) -> Book:
        """
        Deletes a book from the book list by its unique identifier
        :param book_id: The unique identifier of the book to delete.
        :return: The book object that was deleted.
        :raises BookNotFound: If no book with the given ID exists in the book list.
        """
        book_to_delete = self.find_by_id(book_id)
        if book_to_delete is None:
            raise BookNotFound()
        self.__book_list.remove(book_to_delete)
        return book_to_delete

    def update_book_by_id(self, book_id: int, new_title: str, new_description: str, new_author: str) -> object:
        """
        Updates the details of an existing book in the collection identified by its unique ID.
        This method allows modifying the title, description, and author of a book.

        :param book_id: The unique identifier of the book to be updated.
        :param new_title: The new title to be assigned to the book.
        :param new_description: The new description to be assigned to the book.
        :param new_author: The new author to be assigned to the book.
        :return: The updated book object with the new details.
        :raises BookNotFound: If no book is found with the specified ID.
        """
        book_to_update = self.find_by_id(book_id)
        if book_to_update is None:
            raise BookNotFound()
        book_to_update.title = new_title
        book_to_update.description = new_description
        book_to_update.author = new_author
        return book_to_update

    def find_by_id(self, book_id: int) -> object or None:
        """
        Searches for a book in the internal book list by its unique identifier.

        :param book_id: Unique identifier of the book to be searched.
        :return: The book object if found, otherwise None.
        """
        for book in self.__book_list:
            if book.get_book_id() == book_id:
                return book
        return None

    def find(self, book: Book) -> bool:
        """
        Searches for a specific book in the list of books.
        :param book: The book to search for in the book list.
        :return: Returns True if the book exists in the list, otherwise returns False.
        """
        for existing_book in self.__book_list:
            if existing_book == book:
                return True
        return False

    def get_all(self):
        return self.__book_list

    def size(self):
        return len(self.__book_list)
