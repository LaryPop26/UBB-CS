"""
Găsiți cel mai mare număr prim mai mic decât un număr dat.
Daca nu exista un astfel de număr, tipăriți un mesaj.
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


def previous_prime(number):
    """
    Search the previous prime number after n.
    :param number: an integer value
    :return: i - the previous prime number before n
    """
    for i in range(number-1, 2, -1):
        if check_prime(i):
            return i
    return -1


def test_check_prime():
    assert check_prime(5) == 1
    assert check_prime(9) == 0
    assert check_prime(24) == 0
    assert check_prime(47) == 1


def test_previous_prime():
    assert previous_prime(9) == 7
    assert previous_prime(20) == 19
    assert previous_prime(31) == 29


def teste():
    test_check_prime()
    test_previous_prime()


if __name__ == '__main__':
    teste()
    print("Teste trecute cu succes!")
    while True:
        command = input("Doresti introducerea unor date noi?(y/n): ")
        if command == "y":
            n = int(input("n = "))
            nr_prim_anterior = previous_prime(n)
            if nr_prim_anterior == -1:
                print("nu exista!")
            else:
                print("Cel mai mic numar prim mai mare decat cel dat este", nr_prim_anterior)

        if command == "n":
            break
