from domain.expense import create_expense, get_ap, get_value, get_expense_type, get_day
from domain.expense_manager import get_lst_expense
from repository.repo_expenses import add_expense, modify_expense, delete_all_expense_from_apartment, delete_by_type, \
    delete_consecutive_apartments, add_state_to_undo, undo
from validation.validation import validate_inputs, validate_id, validate_value, validate_apartment, validate_expense_type, \
    validate_day

def add_expense_srv(expenses_manager: list, id_expense: int, apartment: int, day: int, value: float, expense_type: str)\
        -> None:
    """
    Creates a new expense and adds it to the list
    :param expenses_manager: a structure which containt the list of expenses and the previous saved list
    :param id_expense: id of the expense
    :param apartment: apartment number
    :param day: day of the expense
    :param value: value of the expense
    :param expense_type: type of expense
    :return:-; list is modified
    """
    expense = create_expense(id_expense, apartment, day, value, expense_type)
    validate_inputs(expense)
    lst_expense = get_lst_expense(expenses_manager)
    add_state_to_undo(expenses_manager)
    add_expense(lst_expense, expense)

def modify_expense_srv(expenses_manager: list, id_expense: int, apartament: int, day: int, value: float,
                       expense_type: str) -> None:
    """
    Using the input data try to modify an expense if the id already exists
    :param expenses_manager: a structure which containt the list of expenses and the previous saved list
    :param id_expense: id of the expense
    :param apartament: new apartment number
    :param day: new day of the expense
    :param value: new value for the expense
    :param expense_type: new type of expense
    :return:-; list is modified if id is valif
    """
    new_expense = create_expense(id_expense, apartament, day, value, expense_type)
    validate_inputs(new_expense)
    lst_expense = get_lst_expense(expenses_manager)
    validate_id(id_expense, lst_expense)
    add_state_to_undo(expenses_manager)
    modify_expense(lst_expense, new_expense)

def delete_all_expense_from_apartment_srv(expenses_manager: list, apartment):
    lst_expense = get_lst_expense(expenses_manager)
    validate_apartment(apartment)
    add_state_to_undo(expenses_manager)
    delete_all_expense_from_apartment(lst_expense, apartment)

def delete_consecutive_apartments_srv(expenses_manager: list, first_apartment, last_apartment):
    validate_apartment(first_apartment)
    validate_apartment(last_apartment)
    lst_expense = get_lst_expense(expenses_manager)
    add_state_to_undo(expenses_manager)
    delete_consecutive_apartments(lst_expense, first_apartment, last_apartment)

def delete_by_type_srv(expenses_manager: list, expense_type):
    validate_expense_type(expense_type)
    lst_expense = get_lst_expense(expenses_manager)
    add_state_to_undo(expenses_manager)
    delete_by_type(lst_expense, expense_type)

# search
def value_higher_than(lst_expense: list, value: float) -> list:
    """
    Search for all apartments where is at least one expense higher than the given value
    :param lst_expense:list of all the expenses
    :param value: search value
    :return: copy list with all expenses higher than the given value, if there are
        None, otherwise
    """
    validate_value(value)
    lst = []
    sum = 0
    for expense in lst_expense:
        ap = get_ap(expense)
        sum += get_value(expense)
        if ap not in lst:
            if sum > value:
                lst.append(ap)
    return lst

def expense_by_type(lst_expense: list, expense_type: str) -> list:
    """
    Search for all expenses with an expense_type
    :param lst_expense: list of all expenses
    :param expense_type: type of expense to search
    :return:copy list with all expenses with an expense_type, if there are
                None, otherwise
    """
    validate_expense_type(expense_type)
    lst = []
    for expense in lst_expense:
        if get_expense_type(expense) == expense_type:
            lst.append(expense)
    return lst

# report
def expense_higher_than_and_before(lst_expense: list, day: int, value: float) -> list:
    """
    Search for all expenses higher than the given value and before the given day
    :param lst_expense:list of all the expenses
    :param day: maximum day of the expense
    :param value: value from where starts
    :return: copy list with all good expenses, if there are
            None, otherwise
    """
    validate_day(day)
    validate_value(value)
    lst = []
    for expense in lst_expense:
        ex_day = get_day(expense)
        ex_value = get_value(expense)
        if ex_day < day and ex_value > value:
            lst.append(expense)
    return lst

def sum_for_type(lst_expense: list, expense_type: str) -> float:
    """
    Calculate the total amount spent on a type of expense
    :param lst_expense: list of all expenses
    :param expense_type: type for which the expenses are summed
    :return: the sum of all expenses with the given expense_type
    """
    validate_expense_type(expense_type)
    sum = 0.0
    for expense in lst_expense:
        if get_expense_type(expense) == expense_type:
            sum += get_value(expense)
    return sum

def apartment_after_type(lst_expense: list, expense_type: str) -> list:
    """
    Search for all apartments where is an expense with a given type
    :param lst_expense: list of all expenses
    :param expense_type: expense_type for search
    :return: a list with all apartments with the given expense_type, if there are
            None, otherwise
    """
    validate_expense_type(expense_type)
    lst = []
    for expense in lst_expense:
        ap = get_ap(expense)
        if ap not in lst:
            if get_expense_type(expense) == expense_type:
                lst.append(ap)
    return lst

# filter
def sum_for_an_apartment(lst_expense: list, apartment: int) -> float:
    """
    Calculate the total amount spent on an apartment
    :param lst_expense: list of all expenses
    :param apartment:apartment for which is the sum calculated
    :return: the sum of all expenses for the given apartment
    """
    validate_apartment(apartment)
    sum = 0.0
    for expense in lst_expense:
        if get_ap(expense) == apartment:
            sum += get_value(expense)
    return sum

def remove_by_type(lst_expense: list, expense_type: str) -> list:
    """
    Search all expenses with another expense_type than the given one
    :param lst_expense: list of all expenses
    :param expense_type: type of expense to remove
    :return: a new list which does not include the given expense_type
    """
    validate_expense_type(expense_type)
    lst = []
    for expense in lst_expense:
        if get_expense_type(expense) != expense_type:
            lst.append(expense)
    return lst

def remove_less_than(lst_expense: list, value: float) -> list:
    """
    Search for all expenses higher than the given value
    :param lst_expense: list of all expenses
    :param value: a given value
    :return: a new list which includes only the expenses higher than the given value
    """
    validate_value(value)
    lst = []
    for expense in lst_expense:
        if get_value(expense) >= value:
            lst.append(expense)
    return lst

def undo_srv(expense_manager):
    return undo(expense_manager)
