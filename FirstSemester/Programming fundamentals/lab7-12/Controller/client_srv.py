import random
import string

from Domain.client import Client
from Exceptions.exceptions import ClientNotFound
from Repository.InMemoryRepository.client_repo import ClientRepository
from Domain.Validation.validator import ClientValidator

class ClientService:
    def __init__(self, repo: ClientRepository, client_validator: ClientValidator):
        """Constructor"""
        self.__repository = repo
        self.__client_validator = client_validator

    def store_client(self, client_id: int, name: str, cnp: str):
        """
        Stores a new client in the repository after validation of provided data.
        :param client_id: Unique identifier of the client.
        :param name: Full name of the client as a string.
        :param cnp: Personal numerical code of the client as a string.
        :return: None
        """
        client = Client(client_id, name, cnp)
        self.__client_validator.client_data_validator(client)
        self.__repository.store_client(client)

    def update_client_by_id(self, client_id: int, new_name: str, new_cnp: str):
        """
        Updates an existing client's information in the repository by their unique identifier.
        :param client_id: An integer representing the unique identifier of the client.
        :param new_name: A string representing the new name of the client.
        :param new_cnp: A string representing the new CNP (personal numerical code)
            for the client.
        :return: The result of the update operation as defined by the repository.
        """
        client = Client(client_id, new_name, new_cnp)
        self.__client_validator.client_data_validator(client)
        return self.__repository.update_client_by_id(client_id, new_name, new_cnp)

    def search_by_id(self, client_id: int):
        """
        Searches for a client using the provided client ID.
        :param client_id: The unique identifier of the client to be searched.
                          Must be a valid integer.
        :returns: The client object retrieved from the repository if found.
        :raises ClientNotFound: If no client is associated with the given client ID.
        """
        self.__client_validator.client_id_validator(client_id)
        client = self.__repository.find_by_id(client_id)
        if client is None:
            raise ClientNotFound()
        return client

    @staticmethod
    def random_id():
        return random.randint(1, 100)

    @staticmethod
    def random_name():
        lenght = random.randrange(1, 40)
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for _ in range(lenght))

    @staticmethod
    def random_cnp():
        lenght = 13
        numbers = string.digits
        return ''.join(random.choice(numbers) for _ in range(lenght))

    def random_client(self):
        client = Client(self.random_id(), self.random_name(), self.random_cnp())
        try:
            self.__repository.store_client(client)
        except client in self.get_all_clients():
            self.random_client()

    def get_all_clients(self):
        """
        :return: the clients list
        """
        return self.__repository.get_all()

    def size(self):
        return self.__repository.size()
