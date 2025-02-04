"""
Numerele n1 si n2 au proprietatea P daca scrierile lor in baza 10 conțin
aceleași cifre (ex. 2113 si 323121). Determinați daca doua numere naturale
au proprietatea P.
"""


def frequency(n):
    """
    Stabileste frecventa fiecarei cifre din n
    :param n: nr intreg
    :return: cifre - lista frecventelor cifrelor lui n
    """
    cifre = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    while n > 0:
        cifre[n % 10] += 1
        n = n//10
    return cifre


def verifica_prop(n1, n2):
    """
    Verifica daca cele 2 numere contin aceleasi cifre
    :param n1: nr intreg
    :param n2: nr intreg
    :return: true, daca conditia e verificata, false altfel
    """
    cifre1 = frequency(n1)
    cifre2 = frequency(n2)
    for i in range(0, len(cifre1)):
        for j in range(0, len(cifre2)):
            if i == j:
                if cifre1[i] == 0 and not cifre2[j] == 0:
                    return False
                if cifre2[j] == 0 and not cifre1[i] == 0:
                    return False
    return True


def test_frequency():
    assert frequency(3658) == [0, 0, 0, 1, 0, 1, 1, 0, 1, 0]
    assert frequency(335118445) == [0, 2, 0, 2, 2, 2, 0, 0, 1, 0]


def test_verifica_prop():
    assert verifica_prop(2113, 323121) == 1
    assert verifica_prop(2153, 112112) == 0


def teste():
    test_frequency()
    test_verifica_prop()
    print("Teste finalozate cu succes!")


if __name__ == '__main__':
    teste()

    while True:
        command = input("Doresti introducerea unor date noi?(y/n): ")
        if command == "y":
            x1 = int(input("Introdu un numar:"))
            x2 = int(input("Introdu un numar:"))
            if verifica_prop(x1, x2):
                print("Cele 2 numere verifica proprietatea P")
            else:
                print("Cele 2 numere nu verifica proprietatea P")

        if command == "n":
            break
