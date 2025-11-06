from domain.expense import get_id, get_ap, get_day, get_value, get_expense_type
from utils.utils import add_default

def setup_expenses_manager(default_add: bool) -> list:
    """

    :param default_add:
    :return:
    """
    if default_add:
        lst_expense = add_default()
    else:
        lst_expense = []

    undo_lst_expense = []

    return [lst_expense, undo_lst_expense]

def get_lst_expense(expense_manager):
    return expense_manager[0]

def get_undo_lst_expense(expense_manager):
    return expense_manager[1]

def set_expenses_manager(expense_manager, new_lst_expense):
    expense_manager[0] = new_lst_expense

def set_undo_lst_expense(expense_manager, new_undo_lst_expense):
    expense_manager[1] = new_undo_lst_expense

def print_as_list(lst):
    if len(lst) == 0:
        print("No expenses!")
    else:
        for exp in lst:
            print("Expense # " + str(get_id(exp)) + ": ")
            print('Apartment number: ' + str(get_ap(exp)) +
                  ' | Day: ' + str(get_day(exp)) +
                  ' | Value: ' + str(get_value(exp)) +
                  ' | Expense type: ' + str(get_expense_type(exp)))