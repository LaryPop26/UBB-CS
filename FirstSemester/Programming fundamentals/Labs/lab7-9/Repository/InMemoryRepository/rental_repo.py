from Domain.rental import Rental
from Exceptions.exceptions import RentAlreadyExists, RentNotFound

class RentRepository:
    def __init__(self):
        self.__rents = []

    def store_rent(self, rent) -> None:
        """
        Stores the specified rent in the storage if it does not already exist.
        :param rent: The rent object to be stored.
        :return: None
        :raises RentAlreadyExists: If the rent already exists in the storage.
        """
        if self.find_rent(rent):
            raise RentAlreadyExists()
        self.__rents.append(rent)

    def delete_rent(self, rent_id: int) -> object:
        """
        Deletes a rent entry from the list of rents based on the given rent ID.
        :param rent_id: The unique identifier of the rent entry to delete.
        :raises RentNotFound: If no rent entry is found for the given rent ID.
        :return: The rent entry that was successfully deleted.
        """
        rent_to_delete = self.find_rent_by_id(rent_id)
        if rent_to_delete is None:
            raise RentNotFound()
        self.__rents.remove(rent_to_delete)
        return rent_to_delete

    def find_rent_by_id(self, rent_id: int) -> Rental or None:
        """
        Finds and returns a rental object matching the given rental ID from the list of rental objects.
        :param rent_id: The unique identifier of the rental to be searched.
        :return: The rental object if a match is found, otherwise None.
        """
        for rent in self.__rents:
            if rent.get_id_rental() == rent_id:
                return rent
        return None

    def find_rent(self, rent: Rental) -> bool:
        """
        Checks if a specific rental exists in the list of stored rentals.
        :param rent: The rental object to search for.
        :return: True if the rental exists in the list; otherwise, False.
        """
        for existing_rent in self.__rents:
            if existing_rent == rent:
                return True
        return False

    def get_rents(self):
        return self.__rents

    def size(self):
        return len(self.__rents)
