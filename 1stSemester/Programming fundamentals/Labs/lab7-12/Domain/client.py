from colorama import Fore, Style

class Client:
    def __init__(self, client_id: int, name: str, cnp: str):
        """
        Class Constructor for Client class
        :param client_id: id of the client, for the clients_list
        :param name: client's name
        :param cnp: client's cnp
        """
        # self.__client_id = client_id
        # self.__name = name
        # self.__cnp = cnp
        self.__client = [client_id, name, cnp]

    def get_client_id(self):
        # return self.__client_id
        return self.__client[0]

    def get_name(self):
        # return self.__name
        return self.__client[1]

    def get_cnp(self):
        # return self.__cnp
        return self.__client[2]

    def set_name(self, new_name):
        # self.__name = new_name
        self.__client[1] = new_name

    def set_cnp(self, new_cnp):
        # self.__cnp = new_cnp
        self.__client[2] = new_cnp

    def __eq__(self, other):
        # if type(self) != type(other):
        #     return False
        # return self.__client_id == other.__client_id
        return self.__client[0] == other.__client[0] or self.__client[2] == other.__client[2]

    def __str__(self):
        return ("ID: " + str(self.get_client_id()) + " | " + Fore.BLUE + "Name: " + self.get_name()
                + " | " + Fore.CYAN + "CNP: " + str(self.get_cnp()) + Style.RESET_ALL)
