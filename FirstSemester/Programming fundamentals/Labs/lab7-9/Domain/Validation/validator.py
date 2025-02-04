from Domain.book import Book
from Domain.client import Client
from Exceptions.exceptions import ValidationException

class BookValidator:

    @staticmethod
    def book_data_validator(book: Book):
        """
        Verifies if a book is valid or not.
        :param book: Book to validate.
        :return: -;
        :raises: ValueError if the book data is not valid.
        """
        errors = ""
        if book.get_book_id() <= 0:
            errors += "Id must be a positive number!\n"
        if len(book.title.strip()) == 0:
            errors += "Title cannot be an empty string!\n"

        if len(book.description.strip()) == 0:
            errors += "Description cannot be an empty string!\n"

        if len(book.author.strip()) == 0:
            errors += "Author cannot be an empty string!\n"

        if len(errors) > 0:
            raise ValidationException(errors)

    @staticmethod
    def book_id_validator(book_id: int):
        if book_id <= 0:
            raise ValidationException("Id must be a positive number!")

class ClientValidator:

    @staticmethod
    def client_data_validator(client: Client):
        """
        Verifies if the client is valid.
        :param client: Client object
        :return: -;
        :raises: ValidationException if the client data is not valid
        """
        errors = ""
        if client.get_client_id() <= 0:
            errors += "Client ID must be a positive number.\n"

        if len(client.get_name()) == 0:
            errors += "Client Name cannot be an empty string.\n"

        if len(client.get_cnp()) != 13:
            errors += "Client CNP must be a 13 digit number.\n"

        if len(errors) > 0:
            raise ValidationException(errors)

    @staticmethod
    def client_id_validator(client_id: int):
        if client_id <= 0:
            raise ValidationException("Client ID must be a positive number.")

class RentalValidator:
    @staticmethod
    def rental_id_validator(rent_id: int):
        """
        Verifies if the rent_id is valid.
        :param rent_id: id to validate.
        :return: -;
        :raises: ValidationException if the rent_id is negative
        """
        if rent_id <= 0:
            raise ValidationException("Rental ID cannot be negative\n")
