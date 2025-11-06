def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5)+1,2):
        if n % i == 0:
            return False
    return True

print(is_prime(6))

def numara(lst):
    if len(lst) == 0:
        return 0
    if len(lst) == 1:
        return 1 if is_prime(lst[0]) else 0
    mid = len(lst)//2
    return numara(lst[:mid]) + numara(lst[mid:])

print(numara([]))