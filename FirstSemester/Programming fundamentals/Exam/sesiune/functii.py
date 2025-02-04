"""
x = [1, 2, 3]
x1 = [1] + x[1:]
x2 = x[:2] + [x[-1]]
print(x1, id(x1) == id(x))
print(x2, id(x2) == id(x))
print(id(x1) == id(x2))
"""

def f(n):
    """
    S
    :param n:
    :return:
    """
    if n < 0:
        raise ValueError()
    x = [0] * (n+1)
    x[0] = 0
    x[1] = 1
    for i in range(2, n+1):
        x[i] = x[i-1] + x[i-2]
    return x[n]

print(f(4))

def test_f():

    assert f(1) == 1
    assert f(4) == 3
    try:
        f(-5)
    except ValueError:
        assert True
    try:
        f(0)
    except IndexError:
        assert True
    print("good")

test_f()


