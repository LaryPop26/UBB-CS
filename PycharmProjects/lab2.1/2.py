"""
Se da data nașterii (zi/luna/an), determinați vârsta persoanei in zile.
"""
import datetime


def an_bisect(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def zile_in_luna(month, year, lista):
    """
    Functia cauta numarul de zile pt o anumita luna
    :param month: nr intreg, luna pt care se cauta nr zile
    :param year: nr intreg, anul cautarii
    :param lista: lista cu nr de zile pt fiecare luna
    :return: m - numarul de zile din luna month
    """
    if month == 2 and an_bisect(year):
        return 29
    return lista[month - 1]


def varsta(day, month, year):
    """
    Functia determina varsta persoanei in zile
    :param day: nr intreg, ziua nasterii
    :param month: nr intreg, luna nasterii
    :param year: nr intreg, anul nasterii
    :return: nr_zile - nr intreg = totalul zilelor pana in data curenta
    """
    lista = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    current_time = datetime.datetime.now()
    current_day = current_time.day
    current_month = current_time.month
    current_year = current_time.year
    nr_zile = 0

    if year == current_year:
        if month == current_month:
            nr_zile = current_day - day
        else:
            nr_zile += zile_in_luna(month, year, lista) - day
            for m in range(month + 1, current_month):
                nr_zile += zile_in_luna(m, year, lista)
            nr_zile += current_day
    else:
        nr_zile += zile_in_luna(month, year, lista) - day
        for m in range(month + 1, 13):
            nr_zile += zile_in_luna(m, year, lista)
        for y in range(year + 1, current_year):
            nr_zile += 366 if an_bisect(y) else 365
        for m in range(1, current_month):
            nr_zile += zile_in_luna(m, current_year, lista)
        nr_zile += current_day

    return nr_zile


def test_an_bisect():
    assert an_bisect(1999) == 0
    assert an_bisect(2004) == 1


def test_zile_in_luna():
    lista = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    assert zile_in_luna(3, 2010, lista) == 31
    assert zile_in_luna(2, 2004, lista) == 29


def test_varsta():
    assert varsta(26, 7, 2004) == 7296
    assert varsta(10, 7, 2024) == 7


def teste():
    test_an_bisect()
    test_zile_in_luna()
    test_varsta()
    print("Teste finalozate cu succes!")


def main():
    teste()

    while True:
        command = input("Doresti introducerea unor date noi?(y/n): ")
        if command == "y":
            zi = int(input("zi: "))
            luna = int(input("luna: "))
            an = int(input("an: "))

            varsta_in_zile = varsta(zi, luna, an)
            print("Varsta persoanei este:", varsta_in_zile, "zile")

        if command == "n":
            break


if __name__ == '__main__':
    main()
