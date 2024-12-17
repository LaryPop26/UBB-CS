from Controller.sorting import bubble_sort, shell_sort
from Domain.dtos import MostRentedBooksDTO, ClientsNamesDTO, ClientsDTO, OneTimeRentDTO
from Domain.rental import Rental
from Exceptions.exceptions import ClientNotFound, BookNotFound
from Repository.InMemoryRepository.book_repo import BookRepository
from Repository.InMemoryRepository.client_repo import ClientRepository
from Repository.InMemoryRepository.rental_repo import RentRepository
from Domain.Validation.validator import BookValidator, ClientValidator, RentalValidator

"""
sortare cu criterii combinate pe o entitate
"""

class RentalService:
    def __init__(self, rent_repo: RentRepository, book_repo: BookRepository, client_repo: ClientRepository,
                 rent_validator: RentalValidator, book_validator: BookValidator, client_validator: ClientValidator):
        """Constructor"""
        self.__rent_repo = rent_repo
        self.__book_repo = book_repo
        self.__client_repo = client_repo
        self.__rent_validator = rent_validator
        self.__book_validator = book_validator
        self.__client_validator = client_validator

    def store_rental(self, rent_id: int, book_id: int, client_id: int):
        """
        Stores a new rental record
        :param rent_id: ID of the rental to be stored.
        :param book_id: ID of the book to be rented out.
        :param client_id: ID of the client renting the book.
        :raises BookNotFound: If the book with the specified ID does not exist.
        :raises ClientNotFound: If the client with the specified ID does not exist.
        """
        book = self.__book_repo.find_by_id(book_id)
        if book is None:
            raise BookNotFound()
        client = self.__client_repo.find_by_id(client_id)
        if client is None:
            raise ClientNotFound()
        rental = Rental(rent_id, book_id, client_id)
        self.__rent_validator.rental_id_validator(rent_id)
        self.__rent_repo.store_rent(rental)

    def delete_rental(self, rent_id) -> object or None:
        """
        Deletes a rental entry from the rental repository using the provided rental ID.
        :param rent_id: The unique identifier of the rental to be deleted.
        """
        self.__rent_validator.rental_id_validator(rent_id)
        return self.__rent_repo.delete_rent(rent_id)

    def delete_rent_and_book(self, book_id: int) -> object:
        """
        Deletes a rent record and associated rentals, in a recursive way.
        :param book_id: ID of the book to be deleted.
        :return: Result of the client deletion process, or None if book deletion occurs recursively.
        """
        self.__book_validator.book_id_validator(book_id)
        rents = self.__rent_repo.get_rents()
        rent_books = [r for r in rents if r.book_id == book_id]
        if not rent_books:
            return self.__book_repo.delete_book(book_id)
        else:
            rent_to_delete = rent_books[0]
            self.__rent_repo.delete_rent(rent_to_delete.get_id_rental())
            return self.delete_rent_and_book(book_id)

    def delete_rent_and_client(self, client_id: int) -> object:
        """
        Deletes a client and all associated rentals.
        :param client_id: The unique identifier of the client to be deleted.
        :return: True if the client and their associated rentals were successfully
                 deleted, False otherwise.
        :raises ValueError: If the provided client_id is invalid.
        """
        self.__client_validator.client_id_validator(client_id)
        rents = self.__rent_repo.get_rents()
        rent_clients = [r for r in rents if r.client_id == client_id]
        for rent_book in rent_clients:
            self.__rent_repo.delete_rent(rent_book.get_id_rental())
        return self.__client_repo.delete_client(client_id)

    def most_rented_books(self) -> list:
        """
        Retrieves the most rented books sorted in descending order by the number
        of times they were rented.
        :raises ValueError: If there are no rents in the repository.
        :return: A list of `MostRentedBooksDTO` sorted by the number of rents in
                 descending order.
        """
        if self.__rent_repo.size() == 0:
            raise ValueError("There are no rents!")

        rents = self.__rent_repo.get_rents()
        rented_books = {}
        for rent in rents:
            book_id = rent.book_id
            if book_id in rented_books:
                rented_books[book_id].increase_nr_rents()
            else:
                book = self.__book_repo.find_by_id(book_id)
                rented_books[book_id] = MostRentedBooksDTO(book.title, book.author, 1)

        return bubble_sort(list(rented_books.values()), key=lambda dto: (dto.nr_rents, dto.author), reverse=True)

    def name_clients_rents(self) -> list:
        """
        Generates a list of clients along with the titles of books they have rented, sorted alphabetically
        by client names.
        :raises ValueError: Raised if there are no rental records in the rental repository.
        :return: A sorted list of `ClientsNamesDTO` objects, where each object contains a client's name
                 and a list of book titles rented by the client.
        """
        rents = self.__rent_repo.get_rents()
        if self.__rent_repo.size() == 0:
            raise ValueError("There are no rents!")
        clients_rents = {}
        for rent in rents:
            client_id = rent.client_id
            book = self.__book_repo.find_by_id(rent.book_id)
            if client_id in clients_rents:
                clients_rents[client_id].add_book_title(book.title)
            else:
                client = self.__client_repo.find_by_id(client_id)
                clients_rents[client_id] = ClientsNamesDTO(client.get_name(), [book.title])

        clients_list = list(clients_rents.values())
        return shell_sort(clients_list, len(clients_list), key=lambda dto: dto.name)

    def books_number_clients(self) -> list:
        """
        Generates a sorted list of clients and the number of books they have rented.
        :return: A sorted list of ClientsDTO objects each containing the client's name
                 and the number of books they rented, in descending order of rentals.
        :raises ValueError: If no rents are found in the rental repository.
        """
        rents = self.__rent_repo.get_rents()
        if self.__rent_repo.size() == 0:
            raise ValueError("There are no rents!")
        clients_with_rented_books = {}
        for rent in rents:
            client_id = rent.client_id
            if client_id in clients_with_rented_books:
                clients_with_rented_books[client_id].increase_nr_rents()
            else:
                client = self.__client_repo.find_by_id(client_id)
                clients_with_rented_books[client_id] = ClientsDTO(client.get_name(), 1)

        return sorted(clients_with_rented_books.values(), key=lambda dto: dto.nr_rents, reverse=True)

    def most_active_clients(self) -> list:
        """
        Calculate the top 20% clients based on the number of books borrowed by each client.
        :return: A list of the most active clients based on their borrowing activity.
        """
        clients_list = self.books_number_clients()
        percentage = int(20/100 * len(clients_list))
        top = max(1, percentage)
        return clients_list[:top]

    def least_rented_books(self) -> list:
        """
        Determines and returns the list of books that have been rented exactly once.
        :return: A sorted list of `OneTimeRentDTO` objects, where each object represents a book that
                 has been rented exactly once.
        :raises ValueError: If there are no rentals to evaluate.
        """
        if self.__rent_repo.size() == 0:
            raise ValueError("There are no rents!")

        rents = self.__rent_repo.get_rents()
        rented_books = {}
        for rent in rents:
            book_id = rent.book_id
            client_id = rent.client_id
            if book_id in rented_books:
                rented_books[book_id].increase_nr_rents()
            else:
                book = self.__book_repo.find_by_id(book_id)
                client = self.__client_repo.find_by_id(client_id)
                rented_books[book_id] = OneTimeRentDTO(book.title, book.author, client.get_name(), 1)

        return sorted((dto for dto in rented_books.values() if dto.nr_rents == 1), key=lambda dto: dto.author)

    def get_all_rentals(self):
        return self.__rent_repo.get_rents()

    def size(self):
        return self.__rent_repo.size()
