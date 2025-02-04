"""
Fie n un număr natural dat. Calculați produsul p al tuturor factorilor
proprii ai lui n.
"""


def produs_factori_proprii(n):
    p = 1
    if n <= 1:
        return 1
    ok = False
    for i in range(2, n):
        if n % i == 0:
            p *= i
            ok = True
    return p if ok else 1


def test_produs_factori_proprii():
    assert produs_factori_proprii(16) == 64
    assert produs_factori_proprii(10) == 10
    assert produs_factori_proprii(13) == 1
    print("Teste finalizate cu succes!")


if __name__ == '__main__':
    test_produs_factori_proprii()

    while True:
        command = input("Doresti introducerea unor date noi?(y/n): ")
        if command == "y":
            x = int(input("Introdu un numar: "))
            produs = produs_factori_proprii(x)
            print(f"Produsul factrilor proprii ai numarului {x} este:{produs}")

        elif command == "n":
            break
