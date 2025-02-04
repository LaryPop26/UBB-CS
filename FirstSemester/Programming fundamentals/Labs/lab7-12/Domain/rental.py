from colorama import Fore, Style

class Rental:
    def __init__(self, id_rental, book_id, client_id):
        self.__id_rental = id_rental
        # if I only choose InMemoryRepository , I can send the entire entity to this class, but with files it is not necessary
        # self.__book = book
        # self.__client = client

        self.__book_id = book_id
        self.__client_id = client_id

    def get_id_rental(self):
        return self.__id_rental

    @property
    def book_id(self):
        return self.__book_id

    @property
    def client_id(self):
        return self.__client_id

    # def get_book(self):
    #     return self.__book
    #
    # def get_client(self):
    #     return self.__client

    def __eq__(self, other):
        return (self.__id_rental == other.__id_rental or
                (self.__book_id == other.__book_id and self.__client_id == other.__client_id))

    def __str__(self):
        # return (Fore.GREEN + "Rent ID:" + str(self.get_id_rental()) + ":" + Fore.CYAN + "Book " + str(self.__book.get_book_id())
        # + Fore.GREEN + " rent by " + Fore.MAGENTA + "Client " + str(self.__client.get_client_id()) + Style.RESET_ALL)

        return (Fore.GREEN + "Rent ID: " + str(self.get_id_rental()) + ": " + Fore.CYAN + "Book " + str(self.__book_id) +
                " rent by " + Fore.MAGENTA + "Client " + str(self.__client_id) + Style.RESET_ALL)
