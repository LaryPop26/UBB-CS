from domain.expense_manager import setup_expenses_manager, get_lst_expense, print_as_list
from repository.repo_expenses import undo
from service.service_expense import (add_expense_srv, delete_all_expense_from_apartment_srv,
                                     sum_for_type, remove_by_type, value_higher_than)
from tests.tests import run_tests_batch

def menu():
    print("App menu")
    print("1. (Add): Add a new expense for an apartment.")
    print("2. (Delete): Delete all expenses from an apartment.")
    print("3. (Search): Print all apartments that have expenses higher than a given amount.")
    print("4. (Report): Print the total amount for a type of expense.")
    print("5. (Filter): Remove all expenses of a certain type.")
    print("6. (Undo): Undo")
    print("E. (Exit): Exit")

def start_v2():
    menu()
    run_tests_batch()
    expenses_manager = setup_expenses_manager(False)
    while True:
        txt = input(">>> ").lower()
        text = txt.split(";")

        for i in text:
            x = i.split()

            if x[0] == "add":
                try:
                    add_expense_srv(expenses_manager, int(x[1]), int(x[2]), int(x[3]), float(x[4]), str(x[5]))
                    print("Successfully added expense!")
                except ValueError as e:
                    print(e)

            elif x[0] == "delete":
                try:
                    delete_all_expense_from_apartment_srv(expenses_manager, int(x[1]))
                    print("Successfully deleted expenses from apartment!")
                except ValueError as e:
                    print(e)

            elif x[0] == "search":
                try:
                    values = value_higher_than(get_lst_expense(expenses_manager), float(x[1]))
                    str_info = ""
                    for s in range(len(values)):
                        str_info += f"{values[s]} | "
                    print(f"Apartments with higher expenses than: {float(x[1])} are: {str_info}")
                except ValueError as e:
                    print(e)

            elif x[0] == "report":
                try:
                    s = sum_for_type(get_lst_expense(expenses_manager), str(x[1]))
                    print(f"The total amount for {x[1]} expense is {s}")
                except ValueError as e:
                    print(e)

            elif x[0] == "filter":
                try:
                    lst = remove_by_type(get_lst_expense(expenses_manager), str(x[1]))
                    print(f"Filter list by removing {x[1]} type of expense")
                    print_as_list(lst)
                except ValueError as e:
                    print(e)

            elif x[0] == "undo":
                try:
                    undo(expenses_manager)
                    print("Successfully undo")
                except ValueError as ve:
                    print(ve)

            elif x[0] == "print":
                print_as_list(get_lst_expense(expenses_manager))

            elif x[0] == "menu":
                menu()

            elif x[0] == "exit":
                return

# Add 4 1 14 15 canal;Add 5 4 26 15 apa;Delete 4;Add 6 14 15 16 canal;Search 10;Filter apa;Report canal;Print;Undo;Print;Exit
# Add 1 1 14 15 canal;Add 2 4 26 15 apa;Add 3 14 15 16 canal;Print;Delete 4;Print;Search 10;Filter apa;
# Report canal;Print;Undo;Print;Exit
# Add 1 1 14 15 canal;Add 2 4 26 15 apa;Add 3 14 15 16 canal;Print;Delete 4;Print;Undo;Print;Search 10;Undo;Print;Exit
