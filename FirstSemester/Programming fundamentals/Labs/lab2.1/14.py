"""
Generați cel mai mic număr perfect mai mare decât un număr dat. Un număr este perfect daca
este egal cu suma divizorilor proprii. Ex. 6 este un număr perfect (6=1+2+3).
"""


def suma_divizori(num):
    """
    Calculeaza suma divizorilor numarului num
    :param num: nr intreg
    :return: sum - nr intreg
    """
    s = 0
    for i in range(1, num):
        if num % i == 0:
            s += i
    return s


def bigger_perfect_nr(num):
    """
    Cauta urmatorul numar perfect dupa num
    Un nr e perfect daca suma div lui e egala cu el insusi
    :param num: nr intreg
    :return: current - nr intreg , nr cautat
    """
    current = num + 1
    while True:
        if suma_divizori(current) == current:
            return current
        current += 1


def test_suma_divizori():
    assert suma_divizori(6) == 6
    assert suma_divizori(9) == 4


def test_nr_perfect():
    assert bigger_perfect_nr(5) == 6
    assert bigger_perfect_nr(14) == 28


def teste():
    test_suma_divizori()
    test_nr_perfect()
    print("Teste efectuate cu succes!")


if __name__ == '__main__':
    teste()

    while True:
        command = input("Doresti introducerea unor date noi?(y/n): ")
        if command == "y":
            n = int(input("Introdu un numar:"))
            urm = bigger_perfect_nr(n)
            print(f"Cel mai mic număr perfect mai mare decât {n} este {urm}")

        if command == "n":
            break
