def f(n):
    if n <= 0:
        raise ValueError
    l = [x for x in range(n-1,-1,-1)]
    for i in range(n-1):
        l[i+1] += l[i]
    return l[-1]

# print(f(1))

def test_f():
    try:
        f(0)
        assert False
    except ValueError:
        assert True
    try:
        f(-1)
        assert False
    except ValueError:
        assert True
    assert f(1) == 0
    assert f(2) == 1
    assert f(3) == 3
    assert f(8) == 28
    # print('passed')

# test_f()

def complexitate(l):
    if len(l) == 1:
        return l[0]
    if l[0] == 0:
        return 0
    return l[0]*complexitate(l[1:])

# print(complexitate([1,2,3,5,0]))

def f(n):
    if n <= 0:
        raise ValueError
    while n > 0:
        c = n % 10
        n = n // 10
        if c%2 == 0:
            return True
    return False

def test_par():
    try:
        f(-2)
    except ValueError:
        pass
    assert f(1) == False
    assert f(2) == True
    assert f(125) == True
    print("passed")

test_par()