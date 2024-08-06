"""
Determina o data calendaristica (sub forma an, luna, zi) pornind de
la doua numere întregi care reprezintă anul si numărul
de ordine al zilei in anul respectiv.
"""


def an_bisect(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def det_data(day_number, year):
    lista = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if an_bisect(year):
        lista[1] = 29

    month = 0
    while day_number > lista[month]:
        day_number -= lista[month]
        month += 1

    return [year, month + 1, day_number]


def test_an_bisect():
    assert an_bisect(1999) == 0
    assert an_bisect(2004) == 1


def test_det_data():
    assert det_data(76, 2023) == [2023, 3, 17]


def teste():
    test_an_bisect()
    test_det_data()
    print("Teste finalozate cu succes!")


def main():
    teste()

    while True:
        command = input("Doresti introducerea unor date noi?(y/n): ")
        if command == "y":
            an = int(input("an:"))
            nr_zi = int(input("nr_ordine_zi:"))
            data = det_data(nr_zi, an)
            print(f"Data e: {data[0]}-{data[1]:02}-{data[2]:02}")
        if command == "n":
            break


if __name__ == '__main__':
    main()
