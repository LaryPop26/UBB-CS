"""
Determina numerele prime p1 si p2 gemene imediat superioare numărului
natural nenul n dat. Doua numere prime p si q sunt gemene daca q-p = 2.
"""


def check_prime(number):
    """
    Verify if a number is prime.
    :param number: an integer value
    :return: True if the number is prime, False otherwise
    """
    if number <= 1:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True


def next_prime(number):
    """
    Search for the initial prime number that is higher than n.
    :param number: an integer value
    :return: next - the next prime number after n
    """
    next_number = number + 1
    while not check_prime(next_number):
        next_number += 1
    return next_number


def verify_twins(number):
    """
    Search for the numbers with the given property
    :param number: an integer value
    :return: list, [a, b], where a and b are the twin prime numbers
    """
    p = next_prime(number)
    q = next_prime(p)
    while q-p != 2:
        p = q
        q = next_prime(p)
    return [p, q]


def test_check_prime():
    assert check_prime(5) == 1
    assert check_prime(9) == 0
    assert check_prime(24) == 0
    assert check_prime(47) == 1


def test_next_prime():
    assert next_prime(9) == 11
    assert next_prime(20) == 23
    assert next_prime(31) == 37


def test_verify_twins():
    assert verify_twins(10) == [11, 13]
    assert verify_twins(50) == [59, 61]
    assert verify_twins(860) == [881, 883]


def teste():
    test_check_prime()
    test_next_prime()
    test_verify_twins()
    print("Teste finalizate cu succes!")


if __name__ == '__main__':
    teste()

    while True:
        command = input("Doresti introducerea unor date noi?(y/n): ")
        if command == "y":
            n = int(input("Introdu un numar: "))
            result = verify_twins(n)
            print(f"Numerele gemene sunt: {result[0]} si {result[1]}")
        if command == "n":
            break
