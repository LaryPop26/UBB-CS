from colorama import Fore, Style

from Controller.book_srv import BookService
from Controller.client_srv import ClientService
from Controller.rental_srv import RentalService
from Exceptions.exceptions import RepositoryException, ValidationException

class Console:

    def __init__(self, book_srv: BookService, client_srv: ClientService, rent_srv: RentalService):
        self.__book_service = book_srv
        self.__client_service = client_srv
        self.__rent_service = rent_srv

    @staticmethod
    def __menu():
        print(Fore.LIGHTCYAN_EX + "Library")
        print("1. Book list management")
        print("2. Clients list management")
        print("3. Rentals list management")
        print("'exit' - Exit app" + Style.RESET_ALL)

    @staticmethod
    def __book_list_menu():
        print(Fore.LIGHTCYAN_EX + "Book list management")
        print("1. Add book")
        print("2. Remove book")
        print("3. Modify book")
        print("4. Search book")
        print("'random' - Generate random books data")
        print("'print' - Print book list")
        print("'back' - Back to the main menu" + Style.RESET_ALL)

    @staticmethod
    def __client_list_menu():
        print(Fore.LIGHTCYAN_EX + "Clients list management")
        print("1. Add client")
        print("2. Remove client")
        print("3. Modify client")
        print("4. Search client")
        print("'random' - Generate random clients data")
        print("'print' - Print client list")
        print("'back' - Back to the main menu" + Style.RESET_ALL)

    @staticmethod
    def __rent_list_menu():
        print(Fore.LIGHTCYAN_EX + "Rentals list management")
        print("1. Add rental")
        print("2. Remove rental")
        print("3. Most rented books")
        print("4. Clients with rented books sorted after name")
        print("5. Clients with rented books sorted after number of books")
        print("6. First 20% active clients")
        print("7. All the books that have been rented 1 time sorted after author name")
        print("'print' - Print rental list")
        print("'back' - Back to the main menu" + Style.RESET_ALL)

    def ui_add_book(self):
        try:
            book_id = int(input("ID: "))
            title = str(input("TITLE: "))
            description = str(input("DESCRIPTION: "))
            author = str(input("AUTHOR: "))
            self.__book_service.store_book(book_id, title, description, author)
            print(Fore.YELLOW + f"Book {book_id} added successfully" + Style.RESET_ALL)

        except ValidationException as v:
            print(Fore.LIGHTRED_EX + "Error! " + str(v) + Style.RESET_ALL)
        except RepositoryException as r:
            print(Fore.LIGHTRED_EX + "Error! " + str(r) + Style.RESET_ALL)

    def ui_delete_book(self):
        try:
            book_id = int(input("ID: "))
            self.__rent_service.delete_rent_and_book(book_id)
            print(Fore.YELLOW + f"Book {book_id} deleted successfully" + Style.RESET_ALL)
        except ValidationException as v:
            print(Fore.LIGHTRED_EX + "Error! " + str(v) + Style.RESET_ALL)
        except RepositoryException as r:
            print(Fore.LIGHTRED_EX + "Error! " + str(r) + Style.RESET_ALL)

    def ui_update_book(self):
        try:
            book_id = int(input("Book Id to be modified: "))
            title = str(input("New Title: "))
            description = str(input("New Description: "))
            author = str(input("New Author: "))
            self.__book_service.update_book_by_id(book_id, title, description, author)
            print(Fore.YELLOW + f"Book: {book_id} updated successfully" + Style.RESET_ALL)
        except ValidationException as v:
            print(Fore.LIGHTRED_EX + "Error! " + str(v) + Style.RESET_ALL)
        except RepositoryException as r:
            print(Fore.LIGHTRED_EX + "Error! " + str(r) + Style.RESET_ALL)

    def ui_search_book(self):
        try:
            book_id = int(input("Book Id to be searched: "))
            book = self.__book_service.search_by_id(book_id)
            print(Fore.YELLOW + f"Book: {book}" + Style.RESET_ALL)
        except RepositoryException as r:
            print(Fore.LIGHTRED_EX + "Error! " + str(r) + Style.RESET_ALL)

    def ui_random_book(self):
        nr = int(input("Enter number of books: "))
        if nr <= 0:
            print("Invalid number!")
        for i in range(nr):
            self.__book_service.random_book()

        print(Fore.YELLOW + "Books generated successfully" + Style.RESET_ALL)

    def ui_add_client(self):
        try:
            id_client = int(input("ID: "))
            name = str(input("Name: "))
            cnp = str(input("CNP: "))
            self.__client_service.store_client(id_client, name, cnp)
            print(Fore.YELLOW + f"Client {id_client} added successfully" + Style.RESET_ALL)

        except ValidationException as v:
            print(Fore.LIGHTRED_EX + "Error! " + str(v) + Style.RESET_ALL)
        except RepositoryException as r:
            print(Fore.LIGHTRED_EX + "Error! " + str(r) + Style.RESET_ALL)

    def ui_remove_client(self):
        try:
            client_id = int(input("ID: "))
            deleted_client = self.__rent_service.delete_rent_and_client(client_id)
            print(Fore.YELLOW + f"Client with {str(deleted_client)} data has been deleted" + Style.RESET_ALL)
        except ValidationException as v:
            print(Fore.LIGHTRED_EX + "Error! " + str(v) + Style.RESET_ALL)
        except RepositoryException as r:
            print(Fore.LIGHTRED_EX + "Error! " + str(r) + Style.RESET_ALL)

    def ui_update_client(self):
        try:
            client_id = int(input("Client Id to be modified: "))
            name = str(input("New Name: "))
            cnp = str(input("New CNP: "))
            self.__client_service.update_client_by_id(client_id, name, cnp)
            print(Fore.YELLOW + f"Client {client_id} updated successfully" + Style.RESET_ALL)
        except ValidationException as v:
            print(Fore.LIGHTRED_EX + "Error! " + str(v) + Style.RESET_ALL)
        except RepositoryException as r:
            print(Fore.LIGHTRED_EX + "Error! " + str(r) + Style.RESET_ALL)

    def ui_search_client(self):
        try:
            client_id = int(input("Client Id to be searched: "))
            client = self.__client_service.search_by_id(client_id)
            print(Fore.YELLOW + f"Client: {client}" + Style.RESET_ALL)
        except RepositoryException as r:
            print(Fore.LIGHTRED_EX + "Error! " + str(r) + Style.RESET_ALL)

    def ui_random_client(self):
        nr = int(input("Enter number of clients: "))
        if nr <= 0:
            print("Invalid number!")
        for i in range(nr):
            self.__client_service.random_client()
        print(Fore.YELLOW + "Clients generated successfully" + Style.RESET_ALL)

    def ui_add_rental(self):
        try:
            id_rental = int(input("ID Rental: "))
            book_id = int(input("Enter book id: "))
            client_id = int(input("Enter client id: "))
            self.__rent_service.store_rental(id_rental, book_id, client_id)
            print(Fore.YELLOW + f"Rent {id_rental} added successfully" + Style.RESET_ALL)
        except ValidationException as v:
            print(Fore.LIGHTRED_EX + "Error! " + str(v) + Style.RESET_ALL)
        except RepositoryException as r:
            print(Fore.LIGHTRED_EX + "Error! " + str(r) + Style.RESET_ALL)

    def ui_delete_rental(self):
        try:
            rent_id = int(input("Enter rent id: "))
            r = self.__rent_service.delete_rental(rent_id)
            print(Fore.YELLOW + f"Rent {r} deleted successfully")
        except ValidationException as v:
            print(Fore.LIGHTRED_EX + "Error! " + str(v) + Style.RESET_ALL)
        except RepositoryException as r:
            print(Fore.LIGHTRED_EX + "Error! " + str(r) + Style.RESET_ALL)

    def ui_most_rented_books(self):
        try:
            book_list = self.__rent_service.most_rented_books()
            print(Fore.YELLOW + "These are the most rented books:" + Style.RESET_ALL)
            self.print_entity(book_list)
        except ValidationException as v:
            print(Fore.LIGHTRED_EX + "Error! " + str(v) + Style.RESET_ALL)
        except RepositoryException as r:
            print(Fore.LIGHTRED_EX + "Error! " + str(r) + Style.RESET_ALL)
        except ValueError as v:
            print(Fore.LIGHTRED_EX + "Error! " + str(v) + Style.RESET_ALL)

    def ui_clients_after_name(self):
        try:
            client_list = self.__rent_service.name_clients_rents()
            print(Fore.YELLOW + "These are clients who have at least one book rented, sorted by name:" + Style.RESET_ALL)
            self.print_entity(client_list)
        except ValidationException as v:
            print(Fore.LIGHTRED_EX + "Error! " + str(v) + Style.RESET_ALL)
        except RepositoryException as r:
            print(Fore.LIGHTRED_EX + "Error! " + str(r) + Style.RESET_ALL)
        except ValueError as v:
            print(Fore.LIGHTRED_EX + "Error! " + str(v) + Style.RESET_ALL)

    def ui_clients_after_number_of_books(self):
        try:
            clients_list = self.__rent_service.books_number_clients()
            print(Fore.YELLOW + "These are clients who have at least one book rented, sorted by number of books:"
                  + Style.RESET_ALL)
            self.print_entity(clients_list)
        except ValidationException as v:
            print(Fore.LIGHTRED_EX + "Error! " + str(v) + Style.RESET_ALL)
        except RepositoryException as r:
            print(Fore.LIGHTRED_EX + "Error! " + str(r) + Style.RESET_ALL)
        except ValueError as v:
            print(Fore.LIGHTRED_EX + "Error! " + str(v) + Style.RESET_ALL)

    def ui_active_clients(self):
        try:
            clients_list = self.__rent_service.most_active_clients()
            print(Fore.YELLOW + "These are the first 20% of clients who have at least one book rented, sorted by number of books:"
                  + Style.RESET_ALL)
            self.print_entity(clients_list)
        except ValidationException as v:
            print(Fore.LIGHTRED_EX + "Error! " + str(v) + Style.RESET_ALL)
        except RepositoryException as r:
            print(Fore.LIGHTRED_EX + "Error! " + str(r) + Style.RESET_ALL)
        except ValueError as v:
            print(Fore.LIGHTRED_EX + "Error! " + str(v) + Style.RESET_ALL)

    def ui_new_function(self):
        try:
            sorted_list = self.__rent_service.least_rented_books()
            print("These are the least rented books:")
            self.print_entity(sorted_list)
        except ValidationException as v:
            print(Fore.LIGHTRED_EX + "Error! " + str(v) + Style.RESET_ALL)
        except RepositoryException as r:
            print(Fore.LIGHTRED_EX + "Error! " + str(r) + Style.RESET_ALL)
        except ValueError as v:
            print(Fore.LIGHTRED_EX + "Error! " + str(v) + Style.RESET_ALL)

    @staticmethod
    def print_entity(entity_list):
        if len(entity_list) == 0:
            print("No entities.")
        for entity in entity_list:
            print(entity)

    def start(self):
        while True:
            self.__menu()
            option = input(">>> ").lower()

            if option == "1":
                while option == "1":
                    self.__book_list_menu()
                    cmd = input(">>> ").lower()
                    if cmd == "1":
                        self.ui_add_book()
                    elif cmd == "2":
                        self.ui_delete_book()
                    elif cmd == "3":
                        self.ui_update_book()
                    elif cmd == "4":
                        self.ui_search_book()
                    elif cmd == "random":
                        self.ui_random_book()
                    elif cmd == "print":
                        self.print_entity(self.__book_service.get_all_books())
                    elif cmd == "back":
                        break
                    else:
                        print("Invalid command!")

            elif option == "2":
                while option == "2":
                    self.__client_list_menu()
                    cmd = input(">>> ").lower()
                    if cmd == "1":
                        self.ui_add_client()
                    elif cmd == "2":
                        self.ui_remove_client()
                    elif cmd == "3":
                        self.ui_update_client()
                    elif cmd == "4":
                        self.ui_search_client()
                    elif cmd == "random":
                        self.ui_random_client()
                    elif cmd == "print":
                        self.print_entity(self.__client_service.get_all_clients())
                    elif cmd == "back":
                        option = "back"
                    else:
                        print("Invalid command!")

            elif option == "3":
                while option == "3":
                    self.__rent_list_menu()
                    cmd = input(">>> ").lower()
                    if cmd == "1":
                        self.ui_add_rental()
                    elif cmd == "2":
                        self.ui_delete_rental()
                    elif cmd == "3":
                        self.ui_most_rented_books()
                    elif cmd == "4":
                        self.ui_clients_after_name()
                    elif cmd == "5":
                        self.ui_clients_after_number_of_books()
                    elif cmd == "6":
                        self.ui_active_clients()
                    elif cmd == "7":
                        self.ui_new_function()
                    elif cmd == "print":
                        self.print_entity(self.__rent_service.get_all_rentals())
                    elif cmd == "back":
                        break
                    else:
                        print("Invalid command!")

            elif option == "exit":
                break

            else:
                print("Invalid command!")
