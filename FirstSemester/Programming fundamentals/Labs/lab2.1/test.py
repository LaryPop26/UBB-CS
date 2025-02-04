import math


def is_prime(num):
    """
    Verifică dacă un număr este prim.
    """
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

n= int(input("Enter a number: "))
count = 1
if n == 1:
    print(1)
i = 2
ok = 1
while count < n and ok == 1:
    if is_prime(i):
        count += 1
        if count == n:
            print(i)
            ok = 0
    else:
        ci = i
        d = 2
        while ci > 1 and ok == 1:
            p = 0
            while ci % d == 0:
                ci = ci / d
                p += 1
            if p:
                count += d
                if count > n:
                    print(d)
                    ok = 0
            d += 1
    i += 1


