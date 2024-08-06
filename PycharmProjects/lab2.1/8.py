"""
Pentru un număr natural n dat găsiți numărul natural maxim m format cu
aceleași cifre. Ex. n=3658, m=8653.
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


def maxim_din_n(n):
    """
    Prin parcurgerea listei de frecventa, se formeaza numarul maxim cu cifrele nr dat
    :param n: nr intreg
    :return: m - nr intreg - nr cu cifrele lui n sortate descrescator
    """
    cifre = frequency(n)
    m = 0
    for i in range(9, -1, -1):
        while cifre[i] > 0:
            m = m * 10 + i
            cifre[i] -= 1
    return m


def test_frequency():
    assert frequency(3658) == [0, 0, 0, 1, 0, 1, 1, 0, 1, 0]
    assert frequency(335118445) == [0, 2, 0, 2, 2, 2, 0, 0, 1, 0]


def test_maxim_din_n():
    assert maxim_din_n(3658) == 8653
    assert maxim_din_n(335118445) == 855443311


def teste():
    test_frequency()
    test_maxim_din_n()
    print("Teste finalizate cu succes!")


if __name__ == '__main__':
    teste()

    while True:
        command = input("Doresti introducerea unor date noi?(y/n): ")
        if command == "y":
            x = int(input("Introdu un numar:"))
            M = maxim_din_n(x)
            print("Cel mai mare numar format cu cifrele numarului dat este:", M)

        if command == "n":
            break
