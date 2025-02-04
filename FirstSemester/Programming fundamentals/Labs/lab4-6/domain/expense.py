def create_expense(id_expense: int, apartment: int, day: int, value: float, expense_type: str) -> dict:
    """
    Creates a new expense with the given information
    :param id_expense: an identifier for the expense
    :param apartment: number of apartment
    :param day: day of the expense
    :param value: value of the expense
    :param expense_type: type of expense
    :return: a dict with the new expense
    """
    return {'id': id_expense, 'apartment number': apartment, 'day': day, 'value': value, 'expense type': expense_type}
    # return [id_expense, apartment, day, value, expense_type]

def get_id(expense):
    return expense['id']
    # return expense[0]
def get_ap(expense):
    return expense['apartment number']
    # return expense[1]

def get_day(expense):
    return expense['day']
    # return expense[2]

def get_value(expense):
    return expense['value']
    # return expense[3]

def get_expense_type(expense):
    return expense['expense type']
    # return expense[4]

def set_ap(expense, new_ap):
    expense['apartment number'] = new_ap
    # expense[0] = new_ap

def set_day(expense, new_day):
    expense['day'] = new_day
    # expense[1] = new_day

def set_value(expense, new_value):
    expense['value'] = new_value
    # expense[2] = new_value

def set_expense_type(expense, new_type):
    expense['expense type'] = new_type
    # expense[3] = new_type

def id_equal(expense1, expense2):
    """
    Verify if 2 expenses have the same id
    :param expense1: first expense
    :param expense2: second expense
    :return: True if the two expenses have the same id
            False otherwise
    """
    return get_id(expense1) == get_id(expense2)
