from domain.expense import get_expense_type, get_value, get_ap, get_day, id_equal, get_id
from domain.expense_manager import get_lst_expense, get_undo_lst_expense, set_expenses_manager
from utils.utils import copy_lst

# add
def add_expense(lst_expense: list, expense: dict) -> None:
    """
    Try to add the given expense to the list
    :param lst_expense: a list of all the expenses
    :param expense: a new expense
    :return: -; list is modified with the new expense
    """
    for another in lst_expense:
        if id_equal(another, expense):
            raise ValueError("Id already exists!")
    lst_expense.append(expense)

def modify_expense(lst_expense: list, expense: dict) -> None:
    """
    Try to moify the expense with the given id
    :param lst_expense: list of all the expenses
    :param expense: new data for expense
    :return: list is modified with the new expense if the id already exists
            Otherwise => ValueError
    """
    id_exp = get_id(expense)
    lst_expense[id_exp-1] = expense

# delete
def delete_all_expense_from_apartment(lst_expense: list, apartment: int) -> None:
    """
    Delete all expenses from an apartment
    :param lst_expense:list of all the expenses
    :param apartment:apartment for which the expenses are deleted
    :return:-; list is modified by deleting all expenses from an apartment, if there are
                Otherwise, list is the same as before
    """
    lst = []
    for expense in lst_expense:
        if get_ap(expense) != apartment:
            lst.append(expense)
    lst_expense[:] = lst

def delete_consecutive_apartments(lst_expense: list, first_apartment: int, last_apartment: int) -> None:
    """
    Delete all expenses from consecutive apartments
    :param lst_expense: list of all the expenses
    :param first_apartment: first apartment to be deleted
    :param last_apartment: last apartment to be deleted
    :return: list is modified with the deleted expenses from apartments between first and last
            Otherwise, list is the same as before
    """
    lst = []
    for expense in lst_expense:
        if first_apartment > get_ap(expense) or get_ap(expense) > last_apartment:
            lst.append(expense)
    lst_expense[:] = lst

def delete_by_type(lst_expense: list, expense_type: str) -> None:
    """
    Delete all expenses with the given expense type
    :param lst_expense: list of all the expenses
    :param expense_type: type of expense which should be deleted
    :return:-; list is modified by deleting all expenses with a type, if there are
                Otherwise, list is the same as before
    """
    lst = []
    for expense in lst_expense:
        if get_expense_type(expense) != expense_type:
            lst.append(expense)
    lst_expense[:] = lst

# undo
def add_state_to_undo(expense_manager):
    """
    Adds the current state of the list to the undo_list
    :param expense_manager: list which contains the expense list and the undo list
    :return: -; undo_list is modified by adding the current state of the list to the undo list
    """
    lst_expense = get_lst_expense(expense_manager)
    undo_lst_expense = get_undo_lst_expense(expense_manager)
    undo_lst_expense.append(copy_lst(lst_expense))

def undo(expense_manager) -> None:
    """
    Undo the last operation
    :param expense_manager: list which contains the expense list and the undo list
    :return: -
    :raises: ValueError if the undo is not possible anymore
    """
    undo_lst_expense = get_undo_lst_expense(expense_manager)
    if len(undo_lst_expense) > 0:
        previous = undo_lst_expense.pop()
        set_expenses_manager(expense_manager, previous)
    else:
        raise ValueError("Undo impossible!")
