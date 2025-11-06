def produs(lst, left=0, right=None):
    if right is None:
        right = len(lst)-1
    if left > right:
        return 1
    if left == right:
        return lst[left] if left % 2 == 0 else 1
    mid = (left + right) // 2
    left_p = produs(lst,left,mid)
    right_p = produs(lst, mid+1, right)
    return left_p * right_p

# print(produs([]))

def test_p():
    assert produs([1, 2, 3, 4, 5]) == 15
    assert produs([1, 2, 3, 4, 5]) == 15
    assert produs([1, 2, 3, 4, 5]) == 15

def numere_negative(l):
    if len(l) == 0:
        return 0
    if len(l) == 1:
        return 1 if l[0] < 0 else 0
    mid = len(l) // 2
    return numere_negative(l[:mid]) + numere_negative(l[mid:])

# print(numere_negative([-1, -2, 3, -4, -5]))


def maxim(lst):
    if len(lst) == 0:
        return 0
    if len(lst) == 1:
        return lst[0]
    mid = len(lst) // 2
    max1 = maxim(lst[:mid])
    max2 = maxim(lst[mid:])
    return max1 if max1 > max2 else max2

print(maxim([1, 2, 100, 4, 5]))
