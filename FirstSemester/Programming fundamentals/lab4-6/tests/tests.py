from domain.expense import create_expense, get_ap, get_day, get_value, get_expense_type, get_id
from domain.expense_manager import setup_expenses_manager, get_lst_expense
from repository.repo_expenses import (add_expense, delete_all_expense_from_apartment, delete_by_type,
                                      value_higher_than, expense_by_type, expense_higher_than_and_before, sum_for_type,
                                      sum_for_an_apartment, remove_by_type, remove_less_than,
                                      delete_consecutive_apartments, apartment_after_type, modify_expense, undo)
from service.service_expense import add_expense_srv, delete_all_expense_from_apartment_srv, \
    delete_consecutive_apartments_srv, delete_by_type_srv, modify_expense_srv
from validation.validation import validate_inputs, validate_id

def test_validate_inputs():
    id_expense = 1
    apartment = 2
    day = 3
    value = 10
    expense_type = 'apa'
    expense = create_expense(id_expense, apartment, day, value, expense_type)
    validate_inputs(expense)

    id_expense = -1
    apartment = -2
    day = -3
    value = -10
    expense_type = 'abc'
    wrong_expense = create_expense(id_expense, apartment, day, value, expense_type)
    try:
        validate_inputs(wrong_expense)
        assert False
    except ValueError as ve:
        assert (str(ve) == "Error! Id must be greater than 0.\nError! You must enter a valid apartment number!\n"
                           "Error! You must enter a valid day number!\nError! You must enter a value greater than 0!\n"
                           "Error! You must enter a valid expense type!\n")

def test_create_expense():
    id_expense = 1
    apartment = 1
    day = 1
    value = 2
    expense_type = "gaz"
    expense1 = create_expense(id_expense, apartment, day, value, expense_type)
    assert (get_ap(expense1) == apartment)
    assert (get_day(expense1) == day)
    assert (get_value(expense1) == value)
    assert (get_expense_type(expense1) == expense_type)

def test_add_expense():
    test_list = []
    assert (len(test_list) == 0)
    add_expense(test_list, create_expense(1, 1, 1, 2, 'gaz'))
    assert (len(test_list) == 1)
    add_expense(test_list, create_expense(2, 2, 2, 30, 'gaz'))
    assert (len(test_list) == 2)

def test_modify_expense():
    exp1 = create_expense(1, 1, 1, 110, 'gaz')
    exp2 = create_expense(2, 1, 14, 116, 'apa')
    test_list = [exp1, exp2]
    new_exp1 = create_expense(1, 9, 10, 50, 'canal')
    modify_expense(test_list, new_exp1)
    assert (test_list == [new_exp1, exp2])

    try:
        new_exp2 = create_expense(16, 9, 10, 50, 'canal')
        validate_id(get_id(new_exp2), test_list)
        modify_expense(test_list, new_exp2)
        assert False
    except ValueError:
        assert True

def test_delete_all_expense_from_apartment():
    exp1 = create_expense(1, 1, 1, 2, 'gaz')
    exp2 = create_expense(2, 2, 2, 30, 'gaz')
    exp3 = create_expense(3, 3, 3, 4, 'gaz')
    test_list = [exp1, exp2, exp3]
    assert (len(test_list) == 3)
    delete_all_expense_from_apartment(test_list, 1)
    assert (len(test_list) == 2)
    delete_all_expense_from_apartment(test_list, 1)
    assert (len(test_list) == 2)

def test_delete_consecutive_apartments():
    exp1 = create_expense(1, 1, 1, 109, 'gaz')
    exp2 = create_expense(2, 1, 14, 105, 'apa')
    exp3 = create_expense(3, 2, 16, 55, 'canal')
    exp4 = create_expense(4, 3, 17, 64, 'canal')
    exp5 = create_expense(5, 4, 15, 64, 'apa')
    test_list = [exp1, exp2, exp3, exp4, exp5]
    assert (len(test_list) == 5)
    delete_consecutive_apartments(test_list, 1, 3)
    assert (len(test_list) == 1)

def test_delete_by_type():
    exp1 = create_expense(1, 1, 1, 24, 'gaz')
    exp2 = create_expense(2, 2, 5, 56, 'canal')
    exp3 = create_expense(3, 3, 3, 1, 'altele')
    test_list = [exp1, exp2, exp3]
    assert (len(test_list) == 3)
    delete_by_type(test_list, 'canal')
    assert (len(test_list) == 2)
    delete_by_type(test_list, 'gaz')
    assert (len(test_list) == 1)
    delete_by_type(test_list, 'altele')
    assert (len(test_list) == 0)

def test_value_higher_than():
    exp1 = create_expense(1, 1, 2, 50, 'canal')
    exp2 = create_expense(2, 2, 2, 100, 'canal')
    exp3 = create_expense(3, 3, 3, 150, 'canal')
    test_list = [exp1, exp2, exp3]
    value = 75
    value_list = value_higher_than(test_list, value)
    assert len(value_list) == 2

def test_expense_by_type():
    exp1 = create_expense(1, 1, 1, 10, 'gaz')
    exp2 = create_expense(2, 1, 14, 100, 'apa')
    exp3 = create_expense(3, 2, 16, 55, 'canal')
    exp4 = create_expense(4, 3, 17, 64, 'canal')
    exp5 = create_expense(5, 6, 15, 64, 'apa')
    test_list = [exp1, exp2, exp3, exp4, exp5]
    expenses = expense_by_type(test_list, 'gaz')
    assert (len(expenses) == 1)
    expenses2 = expense_by_type(test_list, 'canal')
    assert (len(expenses2) == 2)
    expenses3 = expense_by_type(test_list, 'apa')
    assert (len(expenses3) == 2)

def test_expense_higher_than_and_before():
    exp1 = create_expense(1, 1, 1, 55, 'canal')
    exp2 = create_expense(2, 16, 19, 100, 'canal')
    exp3 = create_expense(3, 1, 25, 65, 'canal')
    test_list = [exp1, exp2, exp3]
    lst = expense_higher_than_and_before(test_list, 20, 70)
    assert (len(lst) == 1)
    lst2 = expense_higher_than_and_before(test_list, 20, 50)
    assert (len(lst2) == 2)
    lst3 = expense_higher_than_and_before(test_list, 1, 100)
    assert (len(lst3) == 0)

def test_sum_for_type():
    exp1 = create_expense(1, 1, 1, 2, 'gaz')
    exp2 = create_expense(2, 2, 2, 30, 'gaz')
    exp3 = create_expense(3, 3, 3, 4, 'canal')
    test_lst = [exp1, exp2, exp3]
    assert (sum_for_type(test_lst, 'gaz') == 32)
    assert (sum_for_type(test_lst, 'canal') == 4)
    assert (sum_for_type(test_lst, 'incalzire') == 0)

def test_apartment_after_type():
    exp1 = create_expense(1, 1, 1, 2, 'gaz')
    exp2 = create_expense(2, 2, 2, 30, 'gaz')
    exp3 = create_expense(3, 3, 3, 4, 'canal')
    test_lst = [exp1, exp2, exp3]
    assert (apartment_after_type(test_lst, 'gaz') == [1, 2])
    assert (apartment_after_type(test_lst, 'altele') == [])

def test_sum_for_an_apartment():
    exp1 = create_expense(1, 1, 1, 10, 'canal')
    exp2 = create_expense(2, 2, 15, 100, 'gaz')
    exp3 = create_expense(3, 1, 8, 109, 'incalzire')
    test_list = [exp1, exp2, exp3]
    assert (sum_for_an_apartment(test_list, 1) == 119)
    assert (sum_for_an_apartment(test_list, 2) == 100)

def test_remove_by_type():
    exp1 = create_expense(1, 1, 6, 10, 'gaz')
    exp2 = create_expense(2, 1, 15, 100, 'apa')
    exp3 = create_expense(3, 2, 19, 55, 'canal')
    exp4 = create_expense(4, 3, 17, 64, 'canal')
    exp5 = create_expense(5, 6, 15, 64, 'apa')
    test_list = [exp1, exp2, exp3, exp4, exp5]
    list_elim = remove_by_type(test_list, 'canal')
    assert (len(list_elim) == 3)
    list_elim2 = remove_by_type(test_list, 'apa')
    assert (len(list_elim2) == 3)
    test_list2 = []
    list_elim3 = remove_by_type(test_list2, 'canal')
    assert (len(list_elim3) == 0)

def test_remove_less_than():
    exp1 = create_expense(1, 6, 6, 10, 'gaz')
    exp2 = create_expense(2, 1, 15, 200, 'apa')
    exp3 = create_expense(3, 2, 19, 55, 'canal')
    exp4 = create_expense(4, 3, 17, 100, 'canal')
    exp5 = create_expense(5, 6, 15, 64, 'apa')
    test_list = [exp1, exp2, exp3, exp4, exp5]
    list_elim = remove_less_than(test_list, 50)
    assert (len(list_elim) == 4)
    list_elim2 = remove_less_than(test_list, 70)
    assert (len(list_elim2) == 2)

def test_undo():
    expense_manager = setup_expenses_manager(False)

    add_expense_srv(expense_manager, 1, 1, 1, 10.5, 'gaz')
    assert (len(get_lst_expense(expense_manager)) == 1)

    undo(expense_manager)
    assert (len(get_lst_expense(expense_manager)) == 0)

    add_expense_srv(expense_manager, 1, 1, 1, 10.5, 'gaz')
    add_expense_srv(expense_manager, 2, 1, 14, 100.0, 'apa')
    add_expense_srv(expense_manager, 3, 2, 16, 55.6, 'canal')
    add_expense_srv(expense_manager, 4, 3, 17, 64.9, 'altele')
    add_expense_srv(expense_manager, 5, 4, 15, 150.4, 'apa')
    add_expense_srv(expense_manager, 6, 9, 19, 250.0, 'incalzire')
    assert (len(get_lst_expense(expense_manager)) == 6)

    delete_all_expense_from_apartment_srv(expense_manager, 1)
    assert (len(get_lst_expense(expense_manager)) == 4)
    undo(expense_manager)
    assert (len(get_lst_expense(expense_manager)) == 6)

    delete_consecutive_apartments_srv(expense_manager, 2, 5)
    assert (len(get_lst_expense(expense_manager)) == 3)
    undo(expense_manager)
    assert (len(get_lst_expense(expense_manager)) == 6)

    delete_by_type_srv(expense_manager, 'canal')
    assert (len(get_lst_expense(expense_manager)) == 5)
    undo(expense_manager)
    assert (len(get_lst_expense(expense_manager)) == 6)
    try:
        undo(expense_manager)
        assert False
    except AssertionError:
        assert True

    modify_expense_srv(expense_manager, 1, 9, 10, 50, 'canal')
    assert (get_id(get_lst_expense(expense_manager)[0]) == 1)
    assert (get_ap(get_lst_expense(expense_manager)[0]) == 9)
    assert (get_day(get_lst_expense(expense_manager)[0]) == 10)
    assert (get_value(get_lst_expense(expense_manager)[0]) == 50)
    assert (get_expense_type(get_lst_expense(expense_manager)[0]) == 'canal')
    undo(expense_manager)
    assert (get_id(get_lst_expense(expense_manager)[0]) == 1)
    assert (get_ap(get_lst_expense(expense_manager)[0]) == 1)
    assert (get_day(get_lst_expense(expense_manager)[0]) == 1)
    assert (get_value(get_lst_expense(expense_manager)[0]) == 10.5)
    assert (get_expense_type(get_lst_expense(expense_manager)[0]) == 'gaz')


def run_tests():
    test_validate_inputs()
    test_create_expense()
    test_add_expense()
    test_modify_expense()
    test_delete_all_expense_from_apartment()
    test_delete_consecutive_apartments()
    test_delete_by_type()
    test_value_higher_than()
    test_expense_by_type()
    test_expense_higher_than_and_before()
    test_sum_for_type()
    test_apartment_after_type()
    test_sum_for_an_apartment()
    test_remove_by_type()
    test_remove_less_than()
    test_undo()
    print("All tests passed!")

def run_tests_batch():
    test_validate_inputs()
    test_create_expense()
    test_add_expense()
    test_delete_all_expense_from_apartment()
    test_expense_higher_than_and_before()
    test_sum_for_type()
    test_remove_by_type()
    test_undo()
    print("All tests passed!")
