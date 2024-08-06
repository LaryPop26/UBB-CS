"""
Palindromul unui număr este numărul obținut prin scrierea cifrelor in ordine
inversa (Ex. palindrom(237) = 732). Pentru un n dat calculați palindromul sau.
"""


def det_palindrom(n):
    """
    Calculeaza palindromul numarului n
    :param n: nr intreg
    :return: invers - nr intreg obtinut prin inversarea cifrelor lui n
    """
    copie = n
    invers = 0
    while copie > 0:
        invers = invers * 10 + copie % 10
        copie = copie//10
    return invers


def test_palindrom():
    assert det_palindrom(237) == 732
    assert det_palindrom(70) == 7
    print("Test efectuat cu succes!")


if __name__ == '__main__':
    test_palindrom()

    while True:
        command = input("Doresti introducerea unor date noi?(y/n): ")
        if command == "y":
            x = int(input("Introdu un numar: "))
            result = det_palindrom(x)
            print("Palindromul nr", x, "este", result)

        if command == "n":
            break
