"""
Dându-se numărul natural n, determina numerele prime p1 si p2 astfel ca
n = p1 + p2 (verificarea ipotezei lui Goldbach). Pentru ce fel de n exista soluție?
Exista solutie pentru orice numar intreg par mai mare decat 2
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


def goldbach(n):
    """
    verifica daca n=p1+p2, p1 si p2 nr prime
    :param n: nr intreg
    :return: p1 si p2 daca se verifica proprietatea
    """
    result = []
    for i in range(2, n//2+1):
        if check_prime(i) and check_prime(n-i):
            result.append([i, n-i])
    return result


def test_check_prime():
    assert check_prime(5) == 1
    assert check_prime(9) == 0
    assert check_prime(24) == 0
    assert check_prime(47) == 1


def test_goldbach():
    assert goldbach(8) == [[3, 5]]
    assert goldbach(26) == [[3, 23], [7, 19], [13, 13]]


def teste():
    test_check_prime()
    test_goldbach()
    print("Teste finalozate cu succes!")


def main():
    teste()

    while True:
        command = input("Doresti introducerea unor date noi?(y/n): ")
        if command == "y":
            n = int(input("Introdu numarul: "))
            result = goldbach(n)

            print(result)

        if command == "n":
            break


if __name__ == '__main__':
    main()
