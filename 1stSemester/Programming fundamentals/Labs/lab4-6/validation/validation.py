from domain.expense import get_id, get_ap, get_day, get_value, get_expense_type

def validate_inputs(expense) -> None:
    """
    Used to verify if input data is valid
    :param expense: expense to verify
    :return: -;
    :raises: ValueError if the input is not valid
    """

    errors = ""
    if get_id(expense) <= 0:
        errors += "Error! Id must be greater than 0.\n"
    if get_ap(expense) <= 0:
        errors += "Error! You must enter a valid apartment number!\n"
    if get_day(expense) <= 0 or get_day(expense) > 31:
        errors += "Error! You must enter a valid day number!\n"
    if get_value(expense) < 0:
        errors += "Error! You must enter a value greater than 0!\n"
    if get_expense_type(expense) not in ['apa', 'canal', 'incalzire', 'gaz', 'altele']:
        errors += "Error! You must enter a valid expense type!\n"
    if len(errors) > 0:
        raise ValueError(errors)

def validate_id(id_exp, lst_expense) -> None:
    errors = []
    for expense in lst_expense:
        if id_exp != get_id(expense):
            errors.append(1)
    if len(errors) != (len(lst_expense)-1):
        raise ValueError("Id not valid!")

def validate_apartment(apartment) -> None:
    """
    Used to verify if input data is valid
    :param apartment: apartment to verify
    :return: -;
    :raises: ValueError if the input is not valid
    """
    if apartment <= 0:
        raise ValueError("Error! You must enter a valid apartment number!\n")

def validate_day(day) -> None:
    """
    Used to verify if input data is valid
    :param day: day to verify
    :return: -;
    :raises: ValueError if the input is not valid
    """
    if day <= 0 or day > 31:
        raise ValueError("Error! You must enter a valid day number!\n")

def validate_value(value) -> None:
    """
    Used to verify if input data is valid
    :param value: value to verify
    :return: -;
    :raises: ValueError if the input is not valid
    """
    if value <= 0.0:
        raise ValueError("Error! You must enter a value greater than 0!\n")

def validate_expense_type(expense_type) -> None:
    """
    Used to verify if input data is valid
    :param expense_type: expense type to verify
    :return: -;
    :raises: ValueError if the input is not valid
    """
    if expense_type not in ['apa', 'canal', 'incalzire', 'gaz', 'altele']:
        raise ValueError("Error! You must enter a valid expense type!\n")
