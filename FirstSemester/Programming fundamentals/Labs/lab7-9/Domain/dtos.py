from colorama import Fore, Style

class MostRentedBooksDTO:
    def __init__(self, title, author, nr_rents):
        self.__title = title
        self.__author = author
        self.__nr_rents = nr_rents

    @property
    def title(self):
        return self.__title

    @property
    def author(self):
        return self.__author

    @property
    def nr_rents(self):
        return self.__nr_rents

    def increase_nr_rents(self):
        self.__nr_rents += 1

    def __str__(self):
        return (Fore.GREEN + "Book " + self.__title + Fore.BLUE + " written by " + self.__author + Fore.CYAN + " was rented "
                + str(self.__nr_rents) + " times." + Style.RESET_ALL)

class ClientsNamesDTO:
    def __init__(self, name, book_titles=None):
        self.__name = name
        self.__book_titles = book_titles if book_titles is not None else []

    @property
    def name(self):
        return self.__name

    @property
    def book_titles(self):
        return self.__book_titles

    def add_book_title(self, book_title):
        self.__book_titles.append(book_title)

    def __str__(self):
        return (Fore.GREEN + "Client: " + self.__name + Fore.BLUE + " had rented the following books: " + Fore.CYAN +
                ', '.join(self.__book_titles) + "." + Style.RESET_ALL)

class ClientsDTO:
    def __init__(self, name, nr_rents):
        self.__name = name
        self.__nr_rents = nr_rents

    @property
    def name(self):
        return self.__name

    @property
    def nr_rents(self):
        return self.__nr_rents

    def increase_nr_rents(self):
        self.__nr_rents += 1

    def __str__(self):
        return (Fore.GREEN + "Client " + self.__name + Fore.BLUE + " has " + Fore.CYAN + str(self.__nr_rents) + " books."
                + Style.RESET_ALL)

class OneTimeRentDTO:
    def __init__(self, title, author, name, nr_rents):
        self.__title = title
        self.__author = author
        self.__name = name
        self.__nr_rents = nr_rents

    @property
    def title(self):
        return self.__title

    @property
    def author(self):
        return self.__author

    @property
    def name(self):
        return self.__name

    @property
    def nr_rents(self):
        return self.__nr_rents

    def increase_nr_rents(self):
        self.__nr_rents += 1

    def __str__(self):
        return (Fore.GREEN + "Book " + self.__title + Fore.BLUE + " written by " + self.__author + Fore.CYAN +
                " was rented once by " + self.__name + Style.RESET_ALL)
