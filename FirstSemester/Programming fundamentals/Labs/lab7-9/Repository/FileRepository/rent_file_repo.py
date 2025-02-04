from Domain.rental import Rental
from Repository.InMemoryRepository.rental_repo import RentRepository

class RentFileRepository(RentRepository):
    def __init__(self, filename):
        super().__init__()
        self.__filename = filename
        self.__load_from_file()

    def __load_from_file(self):
        """
        Loads the rent list from a file
        """
        with open(self.__filename, 'r') as f:
            lines = [line.strip() for line in f.readlines() if line.strip() != '']
            for line in lines:
                rent_id, book_id, client_id = line.split(',')
                rent = Rental(int(rent_id), int(book_id), int(client_id))
                super().store_rent(rent)

    def store_rent(self, rent: Rental) -> None:
        """
        Stores rental details and writes it to a file.
        :param rent: The rental object to store.
        """
        super().store_rent(rent)
        self.write_to_file()

    def delete_rent(self, rent_id: int) -> Rental:
        """
        Deletes a rent entry identified by the provided rent_id.
        :param rent_id: The unique identifier of the rent entry to delete.
        :return: The deleted rent entry data obtained from the parent method.
        """
        deleted_rent = super().delete_rent(rent_id)
        self.write_to_file()
        return deleted_rent

    def write_to_file(self):
        """
        Save all rents to file
        """
        rents = [str(rent.get_id_rental()) + ',' + str(rent.book_id) + ',' + str(rent.client_id) for rent in super().get_rents()]
        with open(self.__filename, 'w') as rent_file:
            rent_file.write('\n'.join(rents))
