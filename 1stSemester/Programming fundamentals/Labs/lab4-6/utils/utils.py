from domain.expense import create_expense

def add_default():
    e1 = create_expense(1, 1, 1, 10.5, 'gaz')
    e2 = create_expense(2, 1, 14, 100.0, 'apa')
    e3 = create_expense(3, 2, 16, 55.6, 'canal')
    e4 = create_expense(4, 3, 17, 64.9, 'altele')
    e5 = create_expense(5, 4, 15, 150.4, 'apa')
    e6 = create_expense(6, 9, 19, 250.0, 'incalzire')
    lst = [e1, e2, e3, e4, e5, e6]
    return lst

def copy_lst(lst):
    new_lst = []
    for el in lst:
        new_el = {}
        for key,value in el.items():
            new_el[key] = value

        new_lst.append(new_el)
    return new_lst
