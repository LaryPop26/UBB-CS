from domain.expense_manager import setup_expenses_manager, get_lst_expense, print_as_list
from repository.repo_expenses import undo
from service.service_expense import add_expense_srv, modify_expense_srv, delete_all_expense_from_apartment_srv, \
    delete_consecutive_apartments_srv, delete_by_type_srv, value_higher_than_srv, expense_by_type_srv, \
    expense_higher_than_and_before_srv, sum_for_type_srv, apartment_after_type_srv, sum_for_an_apartment_srv, \
    remove_by_type_srv, remove_less_than_srv
from tests.tests import run_tests

def read_info() -> tuple:
    id_expense = int(input("Enter an identifier for the expense: "))
    apartament = int(input("Enter the apartment number: "))
    day = int(input("Enter the day of the expense: "))
    value = float(input("Enter the value of expense: "))
    expense_type = input("Enter the type of expense: ").lower().strip()
    return id_expense, apartament, day, value, expense_type

# add ui
def ui_add_expense(expenses_manager):
    try:
        id_expense, apartment, day, value, expense_type = read_info()
        add_expense_srv(expenses_manager, id_expense, apartment, day, value, expense_type)
        print("Expense added to list!")
    except ValueError as ve:
        print(ve)

def ui_modify(lst_expense):
    try:
        print("Enter new values:")
        id_expense, apartment, day, value, expense_type = read_info()
        modify_expense_srv(lst_expense, id_expense, apartment, day, value, expense_type)
        print("Expense modified!")
    except ValueError as ve:
        print(ve)

# delete ui
def ui_delete_all_expense_from_apartment(lst_expense):

    try:
        apartment = int(input("Enter the apartment number: "))
        delete_all_expense_from_apartment_srv(lst_expense, apartment)
        print(f"All expenses from apartment {apartment} deleted from list!")
    except ValueError as ve:
        print(ve)

def ui_delete_consecutive_apartments(lst_expense):
    first_apartment = int(input("Enter the first apartment number: "))
    last_apartment = int(input("Enter the last apartment number: "))
    try:
        delete_consecutive_apartments_srv(lst_expense, first_apartment, last_apartment)
        print(f"All expenses from apartments between {first_apartment} and {last_apartment} deleted from list!")
    except ValueError as ve:
        print(ve)


def ui_delete_by_type(lst_expense):
    expense_type = input("Enter the type of expense: ")
    try:
        delete_by_type_srv(lst_expense, expense_type)
        print(f"All {expense_type} expenses deleted from list!")
    except ValueError as ve:
        print(ve)

# search ui
def ui_value_higher_than(lst_expense):
    value = float(input("Enter the value: "))
    try:
        values = value_higher_than_srv(lst_expense, value)
        str_info = ""
        for s in range(len(values)):
            str_info += f"{values[s]} | "
        print(f"Apartments with higher expenses than: {value} are: {str_info}")
    except ValueError as ve:
        print(ve)

def ui_expense_by_type(lst_expense):
    expense_type = input("Enter the type of expense: ")
    try:
        expenses = expense_by_type_srv(lst_expense, expense_type)
        if len(expenses) == 0:
            print("There are not compatible expenses!")
        else:
            print_as_list(expenses)
    except ValueError as ve:
        print(ve)

def ui_expense_higher_than_and_before(lst_expense):
    day = int(input("Enter the day of the expense: "))
    value = int(input("Enter the value of expense: "))
    try:
        expenses = expense_higher_than_and_before_srv(lst_expense, day, value)
        if len(expenses) == 0:
            print("There are not compatible expenses!")
        else:
            print_as_list(expenses)
    except ValueError as ve:
        print(ve)

# report ui
def ui_sum_for_type(expenses_manager):
    expense_type = input("Enter the type of expense: ").lower()
    try:
        s = sum_for_type_srv(expenses_manager, expense_type)
        print(f"The total amount for {expense_type} expense is {s}")
    except ValueError as ve:
        print(ve)

def ui_apartments_by_type(lst_expense):
    expense_type = input("Enter the type of expense: ").lower()
    try:
        expenses = apartment_after_type_srv(lst_expense, expense_type)
        str_info = ""
        for s in range(len(expenses)):
            str_info += f"{expenses[s]} | "
        print(f"Apartments type {expense_type} are: {str_info}")
    except ValueError as ve:
        print(ve)

def ui_sum_apartment(lst_expense):
    apartment = int(input("Enter the apartment number: "))
    try:
        s = sum_for_an_apartment_srv(lst_expense, apartment)
        print(f"The total amount of expense for apartment {apartment} is {s}")
    except ValueError as ve:
        print(ve)

# filter ui
def ui_remove_by_type(lst_expense):
    expense_type = input("Enter the type of expense: ")
    try:
        list_without_type = remove_by_type_srv(lst_expense, expense_type)
        if len(list_without_type) == 0:
            print("There is no expense with expense_type")
        else:
            print_as_list(list_without_type)
    except ValueError as ve:
        print(ve)

def ui_remove_less_than(lst_expense):
    value = float(input("Enter a value: "))
    try:
        list_higher = remove_less_than_srv(lst_expense, value)
        if len(list_higher) == 0:
            print(f"There is no expense with less that {value}")
        else:
            print_as_list(list_higher)
    except ValueError as ve:
        print(ve)

def ui_undo(expenses_manager):
    try:
        undo(expenses_manager)
        print("Successfully undo")
    except ValueError as ve:
        print(ve)

# ui menu
def menu():
    print("1. Add menu")
    print("2. Delete menu")
    print("3. Search menu")
    print("4. Reports menu")
    print("5. Filter menu")
    print("6. Undo")
    print("P. Print all")
    print("E. Exit app")

def add_menu():
    print("Add")
    print("1. Add a new expense for an apartment.")
    print("2. Modify an existing expense.")
    print("3. Undo")
    print("'print' Show the current expenses list.")
    print("'back' Return to main menu.")

def delete_menu():
    print("Delete")
    print("1. Delete all expenses from an apartment.")
    print("2. Delete expenses from consecutive apartments.")
    print("3. Delete the expenses of a certain type from all apartments.")
    print("4. Undo")
    print("'print' Show the current expenses list.")
    print("'back' Return to main menu.")

def search_menu():
    print("Search")
    print("1. Print all apartments that have expenses higher than a given amount.")
    print("2. Print the expenses of a certain type from all apartments.")
    print("3. Print all expenses incurred before a day and higher than an amount.")
    print("'print' Show the current expenses list.")
    print("'back' Return to main menu.")

def report_menu():
    print("Report")
    print("1. Print the total amount for a type of expense.")
    print("2. Print all apartments sorted by expense type.")
    print("3. Print total expenses for a given apartment.")
    print("'print' Show the current expenses list.")
    print("'back' Return to main menu.")

def filter_menu():
    print("Filter")
    print("1. Remove all expenses of a certain type.")
    print("2. Remove all expenses less than a given amount ")
    print("'print' Show the current expenses list.")
    print("'back' Return to main menu.")


def start_app():
    run_tests()
    expenses_manager = setup_expenses_manager(True)
    menu()
    while True:
        print("'menu' - show the app menu")
        option = input("Choose an option: ").upper()
        if option == "MENU":
            menu()
        elif option == "1":
            while option == "1":
                add_menu()
                cmd = input(">>> ").lower()
                if cmd == "1":
                    ui_add_expense(expenses_manager)
                    print_as_list(get_lst_expense(expenses_manager))
                elif cmd == "2":
                    ui_modify(expenses_manager)
                elif cmd == "3":
                    ui_undo(expenses_manager)
                elif cmd == "print":
                    print_as_list(get_lst_expense(expenses_manager))
                elif cmd == "back":
                    option = "back"
                else:
                    print("Invalid command! Try Again!")
        elif option == "2":
            while option == "2":
                delete_menu()
                cmd = input(">>> ")
                if cmd == "1":
                    ui_delete_all_expense_from_apartment(expenses_manager)
                elif cmd == "2":
                    ui_delete_consecutive_apartments(expenses_manager)
                elif cmd == "3":
                    ui_delete_by_type(expenses_manager)
                elif cmd == "4":
                    ui_undo(expenses_manager)
                elif cmd == "print":
                    print_as_list(get_lst_expense(expenses_manager))
                elif cmd == "back":
                    option = "back"
                else:
                    print("Invalid command! Try Again!")
        elif option == "3":
            while option == "3":
                search_menu()
                cmd = input(">>> ")
                if cmd == "1":
                    ui_value_higher_than(get_lst_expense(expenses_manager))
                elif cmd == "2":
                    ui_expense_by_type(get_lst_expense(expenses_manager))
                elif cmd == "3":
                    ui_expense_higher_than_and_before(get_lst_expense(expenses_manager))
                elif cmd == "print":
                    print_as_list(get_lst_expense(expenses_manager))
                elif cmd == "back":
                    option = "back"
                else:
                    print("Invalid command! Try Again!")
        elif option == "4":
            while option == "4":
                report_menu()
                cmd = input(">>> ")
                if cmd == "1":
                    ui_sum_for_type(get_lst_expense(expenses_manager))
                elif cmd == "2":
                    ui_apartments_by_type(get_lst_expense(expenses_manager))
                elif cmd == "3":
                    ui_sum_apartment(get_lst_expense(expenses_manager))
                elif cmd == "print":
                    print_as_list(get_lst_expense(expenses_manager))
                elif cmd == "back":
                    option = "back"
                else:
                    print("Invalid command! Try Again!")
        elif option == "5":
            while option == "5":
                filter_menu()
                cmd = input(">>> ")
                if cmd == "1":
                    ui_remove_by_type(get_lst_expense(expenses_manager))
                elif cmd == "2":
                    ui_remove_less_than(get_lst_expense(expenses_manager))
                elif cmd == "print":
                    print_as_list(get_lst_expense(expenses_manager))
                elif cmd == "back":
                    option = "back"
                else:
                    print("Invalid command! Try Again!")
        elif option == "6":
            ui_undo(expenses_manager)
        elif option == "PRINT":
            print_as_list(get_lst_expense(expenses_manager))
        elif option == "EXIT":
            break
        else:
            print("Invalid command! Try Again!")
