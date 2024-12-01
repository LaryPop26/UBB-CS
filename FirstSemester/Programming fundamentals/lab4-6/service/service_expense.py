from domain.expense import create_expense
from domain.expense_manager import get_lst_expense
from repository.repo_expenses import add_expense, modify_expense, delete_all_expense_from_apartment, delete_by_type, \
    value_higher_than, expense_by_type, expense_higher_than_and_before, sum_for_type, apartment_after_type, \
    sum_for_an_apartment, remove_by_type, remove_less_than, delete_consecutive_apartments, add_state_to_undo
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

def value_higher_than_srv(lst_expense, value):
    validate_value(value)
    return value_higher_than(lst_expense, value)

def expense_by_type_srv(lst_expense, expense_type):
    validate_expense_type(expense_type)
    return expense_by_type(lst_expense, expense_type)

def expense_higher_than_and_before_srv(lst_expense, day, value):
    validate_day(day)
    validate_value(value)
    return expense_higher_than_and_before(lst_expense, day, value)

def sum_for_type_srv(lst_expense, expense_type):
    validate_expense_type(expense_type)
    return sum_for_type(lst_expense, expense_type)

def apartment_after_type_srv(lst_expense, expense_type):
    validate_expense_type(expense_type)
    return apartment_after_type(lst_expense, expense_type)

def sum_for_an_apartment_srv(lst_expense, apartment):
    validate_apartment(apartment)
    return sum_for_an_apartment(lst_expense, apartment)

def remove_by_type_srv(lst_expense, expense_type):
    validate_expense_type(expense_type)
    return remove_by_type(lst_expense, expense_type)

def remove_less_than_srv(lst_expense, value):
    validate_value(value)
    return remove_less_than(lst_expense, value)
