from colorama import Fore, Style

class Book:
    def __init__(self, book_id: int, title: str, description: str, author: str):
        """
        Class Constructor for Book class
        :param book_id: id of the book, for the book_list
        :param title: book's title
        :param description: book's description
        :param author: book's author
        """
        self.__book_id = book_id
        self.__title = title
        self.__description = description
        self.__author = author

    def get_book_id(self):
        return self.__book_id

    @property
    def title(self):
        return self.__title

    @property
    def description(self):
        return self.__description

    @property
    def author(self):
        return self.__author

    @title.setter
    def title(self, new_title):
        self.__title = new_title

    @description.setter
    def description(self, new_description):
        self.__description = new_description

    @author.setter
    def author(self, new_author):
        self.__author = new_author

    def __eq__(self, other):
        # if type(self) != type(other):
        #     return False
        return self.__book_id == other.__book_id or (self.__title == other.__title and self.__author == other.__author)

    def __str__(self):
        return (Fore.GREEN + "ID: " + str(self.get_book_id()) + " | " +
                Fore.BLUE + "Title: " + self.__title + " | " +
                Fore.CYAN + "Description: " + self.__description + " | " +
                Fore.MAGENTA + "Author: " + self.__author + Style.RESET_ALL)
