def f(n):
    s = 0
    for i in range(0, n*n+1):
        while i > 0:
            s = s+i
            i -= 1
            print(s)
    return s

