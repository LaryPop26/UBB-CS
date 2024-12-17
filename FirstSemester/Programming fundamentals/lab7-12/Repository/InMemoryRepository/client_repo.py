
from Domain.client import Client
from Exceptions.exceptions import ClientNotFound, ClientAlreadyExists

class ClientRepository:
    def __init__(self):
        self.__clients_list = []

    def store_client(self, client: Client) -> None:
        """
        Stores a client in the internal clients list.
        :param client: The client to be stored, represented as an instance of the
                       Client class.
        :raises ClientAlreadyExists: Raised when the client already exists in the
                                      internal clients list.
        """
        if self.find(client):
            raise ClientAlreadyExists()
        self.__clients_list.append(client)

    def delete_client(self, client_id: int) -> Client:
        """
        Deletes a client with the specified client ID from the client list.
        :param client_id: The unique identifier of the client to be deleted.
        :return: The `Client` instance of the deleted client.
        :raises ClientNotFound: If no client with the specified ID exists
            in the client list.
        """
        client_to_delete = self.find_by_id(client_id)
        if client_to_delete is None:
            raise ClientNotFound()
        self.__clients_list.remove(client_to_delete)
        return client_to_delete

    def find_by_id(self, client_id: int) -> Client or None:
        """
        Finds a client in the list by their unique client ID.
        :param client_id: The unique identifier of the client to be searched for.
        :return: The client object if found; otherwise, None.
        """
        for client in self.__clients_list:
            if client.get_client_id() == client_id:
                return client
        return None

    def find(self, client: Client, index: int = 0) -> bool:
        """
        Searches for a specific client in the list of clients
        :param client: The client object that needs to be searched for in the client list
        :param index: An optional integer index parameter. Although it is not utilized
                      in the function, it can be passed as a descriptor. Defaults to 0.
        :return: Returns True if the passed client is found in the list.
            Otherwise, returns False.
        """
        if index >= len(self.__clients_list):
            return False
        if self.__clients_list[index] == client:
            return True
        return self.find(client, index + 1)

    def update_client_by_id(self, client_id: int, new_name: str, new_cnp: str) -> Client:
        """
        Updates a client's name and CNP by their unique identifier.
        :param client_id: Unique integer identifier of the client to be updated.
        :param new_name: New name to assign to the client.
        :param new_cnp: New CNP (unique identifier) to assign to the client.
        :return: The updated client object with the modified name and CNP.
        :raises ClientNotFound: If no client is found with the given ID.
        """
        client_to_update = self.find_by_id(client_id)
        if client_to_update is None:
            raise ClientNotFound()
        client_to_update.set_name(new_name)
        client_to_update.set_cnp(new_cnp)
        return client_to_update

    def get_all(self) -> list:
        """
        :return: the clients list
        """
        return self.__clients_list

    def size(self) -> int:
        """
        :return: the number of clients in the list
        """
        return len(self.__clients_list)
