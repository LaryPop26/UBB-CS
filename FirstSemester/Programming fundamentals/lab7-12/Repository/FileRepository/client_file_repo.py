from Domain.client import Client
from Repository.InMemoryRepository.client_repo import ClientRepository

class ClientFileRepository(ClientRepository):
    def __init__(self, filename):
        super().__init__()
        self.__filename = filename
        self.__load_from_file()

    def __load_from_file(self):
        """
        Loads the clients list from a file
        """
        with open(self.__filename, 'r') as f:
            lines = [line.strip() for line in f.readlines() if line.strip() != '']
            for line in lines:
                client_id, name, cnp = line.split(',')
                super().store_client(Client(int(client_id), name, cnp))

    def store_client(self, client: Client) -> None:
        """
        Stores a client object in a persistent storage and writes the client data to the file system.
        :param client: Instance of the ``Client`` class representing the client to be stored.
        """
        super().store_client(client)
        self.__write_to_file()

    def delete_client(self, client_id: int) -> Client:
        """
        Deletes a client by the given client ID and ensures the operation is persisted by
        writing the updated data to the storage file.

        :param client_id: The unique identifier of the client to delete
        :return: The deleted client object as returned by the parent class method
        """
        deleted_book = super().delete_client(client_id)
        self.__write_to_file()
        return deleted_book

    def update_client_by_id(self, client_id: int, new_name: str, new_cnp: str) -> Client:
        """
        Updates an existing client's details by their unique identifier.
        :param client_id: The unique identifier of the client to be updated.
        :param new_name: The new name to be assigned to the client.
        :param new_cnp: The new personal identification number (cnp) of the client.
        :return: The updated client object containing the modified details.
        """
        updated_client = super().update_client_by_id(int(client_id), new_name, new_cnp)
        self.__write_to_file()
        return updated_client

    def __write_to_file(self):
        """
        Save all clients to file
        """
        clients = [str(client.get_client_id()) + ',' + client.get_name() + ',' + client.get_cnp() for client in super().get_all()]
        with open(self.__filename, 'w') as clients_file:
            clients_file.write('\n'.join(clients))
