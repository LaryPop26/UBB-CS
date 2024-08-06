"""
Găsiți primul număr prim mai mare decât un număr dat.
"""


def check_prime(number):
    """
    Verify if a number is prime.
    :param number: an integer value
    :return: True if the number is prime, False otherwise
    """
    if number <= 1:
        return False
    for i in range(2, int(number**0.5)+1):
        if number % i == 0:
            return False
    return True


def next_prime(number):
    """
    Search the next prime number after n.
    :param number: an integer value
    :return: next - the next prime number after n
    """
    next_number = number + 1
    while not check_prime(next_number):
        next_number += 1
    return next_number


def test_check_prime():
    assert check_prime(5) == 1
    assert check_prime(9) == 0
    assert check_prime(24) == 0
    assert check_prime(47) == 1


def test_next_prime():
    assert next_prime(9) == 11
    assert next_prime(20) == 23
    assert next_prime(31) == 37


def teste():
    test_check_prime()
    test_next_prime()
    print("Teste finalozate cu succes!")


if __name__ == '__main__':
    teste()

    while True:
        command = input("Doresti introducerea unor date noi?(y/n): ")
        if command == "y":
            n = int(input("n = "))
            urm_nr_prim = next_prime(n)
            print("Cel mai mic numar prim mai mare decat cel dat este", urm_nr_prim)
        if command == "n":
            break
