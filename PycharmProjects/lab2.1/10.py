"""
Pentru un număr natural n dat găsiți numărul natural minim m format cu
aceleași cifre. Ex. n=3658, m=3568.
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


def minim_din_n(n):
    """
    Prin parcurgerea listei de frecventa, se formeaza numarul minim cu cifrele nr dat
    :param n: nr intreg
    :return: m - nr intreg - nr cu cifrele lui n sortate crescator
    """
    cifre = frequency(n)
    minim = 0
    for i in range(1, len(cifre)):
        while cifre[i] > 0:
            minim = minim * 10 + i
            cifre[i] -= 1
    return minim


def test_frequency():
    assert frequency(3658) == [0, 0, 0, 1, 0, 1, 1, 0, 1, 0]
    assert frequency(335118445) == [0, 2, 0, 2, 2, 2, 0, 0, 1, 0]


def test_minim_din_n():
    assert minim_din_n(3658) == 3568
    assert minim_din_n(335118445) == 113344558


def teste():
    test_frequency()
    test_minim_din_n()
    print("Teste finalozate cu succes!")


if __name__ == '__main__':
    teste()

    while True:
        command = input("Doresti introducerea unor date noi?(y/n): ")
        if command == "y":
            x = int(input("Introdu un numar:"))
            m = minim_din_n(x)
            print("Cel mai mic numar format cu cifrele numarului dat este:", m)

        if command == "n":
            break
