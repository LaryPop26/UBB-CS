"""
Determinați al n-lea element al șirului 1,2,3,2,2,5,2,2,3,3,3,7,2,2,3,3,3,...
obținut din șirul numerelor naturale prin înlocuirea numerelor compuse prin
divizorii lor primi, fiere divizor prim d repetându-se de d ori, fără a retine termenii șirului!
NU E GATA
"""


def check_prime(number):
    """
    Verify if a number is prime.
    :param number: an integer value
    :return: True if the number is prime, False otherwise
    """
    if number <= 1:
        return False
    if number == 2:
        return True
    if number % 2 == 0 or number % 3 == 0:
        return False
    i = 5
    while i*i <= number:
        if number % i == 0 or number % (i+2) == 0:
            return False
        i += 6
    return True


def det_factori(num):
    """
    Gaseste toti factorii primi ai unui numar
    In acest caz, lista returnata va avea toti termenii multiplicati a.i. nr lor e egal cu divizorul
    :param num:nr intreg
    :return: factoriprimi - lista tuturor factorilor primi ai nr num
    """
    factoriprimi = []
    if num % 2 == 0:
        factoriprimi.append(2)
        factoriprimi.append(2)
    while num % 2 == 0:
        num = num // 2

    for i in range(3, num, 2):
        if num % i == 0:
            while num % i == 0:
                num = num // i
            j = i
            while j > 0:
                factoriprimi.append(i)
                j -= 1

    if num > 2:
        num1 = num
        while num1 > 0:
            factoriprimi.append(num)
            num1 -= 1
    return factoriprimi


def count_second(n):
    """
    Cauta al n-lea el in sirul cerut,verificand la fiecare pas daca s-a ajuns la cel cautat
    :param n:nr intreg
    :return:n-lea el in sirul cerut
    """
    count = 0
    current_number = 1
    while True:
        if n == 1:
            return current_number
        if check_prime(current_number):
            count += 1
            if count == n:
                return current_number
        else:
            factori = det_factori(current_number)
            for f in factori:
                count += 1
                if count == n:
                    return f
        current_number += 1


def test_check_prime():
    assert check_prime(5) == 1
    assert check_prime(9) == 0
    assert check_prime(24) == 0
    assert check_prime(47) == 1


def test_det_factori():
    assert det_factori(4) == [2, 2]
    assert det_factori(6) == [2, 2, 3, 3, 3]


def test_count():
    assert count_second(5) == 2
    assert count_second(9) == 2


def teste():
    test_check_prime()
    test_det_factori()
    test_count()
    print("Teste finalozate cu succes!")


if __name__ == '__main__':
    teste()

    while True:
        command = input("Doresti introducerea unor date noi?(y/n): ")
        if command == "y":
            x = int(input("Introdu un numar: "))
            search = count_second(x)
            print("Elementul cautat din sir este:", search)

        if command == "n":
            break
