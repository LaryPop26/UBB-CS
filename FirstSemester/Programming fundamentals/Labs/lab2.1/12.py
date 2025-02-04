"""
Determinati al n-lea element al șirului 1,2,3,2,5,2,3,7,2,3,2,5,...
obținut din șirul numerelor naturale prin înlocuirea numerelor compuse prin
divizorii lor primi, fără a retine termenii șirului.
NU E GATA
"""
import math

def check_prime(number):
    """
    Verify if a number is prime.
    :param number: an integer value
    :return: True if the number is prime, False otherwise
    """
    if number <= 1:
        return False
    for i in range(2, int(math.sqrt(number))+1):
        if number % i == 0:
            return False
    return True


def count_prime(n):
    """
    Cauta al n-lea el in sirul cerut,verificand la fiecare pas daca s-a ajuns la cel cautat
    :param n:nr intreg
    :return:n-lea el in sirul cerut
    """

    count = 0
    current_number = 1

    while True:
        if n == 1:
            return 1

        if check_prime(current_number):
            count += 1
            if count == n:
                return current_number

        else:
            d = 2
            number = current_number
            while number > 1 and d*d <= number:
                while number % d == 0:
                    if count == n:
                        return d
                    count += 1
                    number //= d
                d += 1
            if number > 1:
                if count == n:
                    return number
                count += 1
        current_number += 1


def test_check_prime():
    assert check_prime(5) == 1
    assert check_prime(9) == 0
    assert check_prime(24) == 0
    assert check_prime(47) == 1


def test_count_prime():
    assert count_prime(1) == 1
    #assert count_prime(5) == 5
    #assert count_prime(7) == 3


def teste():
    test_check_prime()
    test_count_prime()
    print("Teste finalozate cu succes!")


if __name__ == '__main__':
    teste()

    while True:
        command = input("Doresti introducerea unor date noi?(y/n): ")
        if command == "y":
            x = int(input("Introdu un numar: "))
            search = count_prime(x)
            print("Elementul cautat din sir este:", search)

        if command == "n":
            break
