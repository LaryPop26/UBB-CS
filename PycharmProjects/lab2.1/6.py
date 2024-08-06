"""
Găsește cel mai mic număr m din șirul lui Fibonacci definit de
f[0]=f[1]=1, f[n]=f[n-1]+f[n-2], pentru n>2,
mai mare decât numărul natural n dat, deci exista k astfel ca f[k]=m si m>n.
"""


def fibonacci(n):
    """
    Calculeaza pe rand termenii din sirul fibonacci, pana cand valoarea depaseste nr n
    :param n: nr natural , nr de termeni din sir
    :return: f_next, termenul din sir ce verifica proprietatea cautata
    """
    f0, f1 = 1, 1

    while True:
        f_next = f0 + f1
        if f_next > n:
            return f_next
        f0, f1 = f1, f_next


def test_fibonacci():
    assert fibonacci(6) == 8
    assert fibonacci(1) == 2
    assert fibonacci(10) == 13
    print("Teste finalozate cu succes!")


if __name__ == '__main__':
    test_fibonacci()

    while True:
        command = input("Doresti introducerea unor date noi?(y/n): ")
        if command == "y":
            x = int(input("n="))
            result = fibonacci(x)
            print(result)

        elif command == "n":
            break
