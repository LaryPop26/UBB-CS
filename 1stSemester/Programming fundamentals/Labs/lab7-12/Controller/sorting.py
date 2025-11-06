def bubble_sort(arr, key, reverse=False):
    """
    Sorts a given list using the bubble sort algorithm

    complexity:
    - Overall : O(n^2)
    - BC - when the list is already sorted; Θ(n)
    - WC = Θ(n^2) - worst case scenario
            - when the list is reversed sorted

    ∑_(i=0)^(n-1) ∑_(j=0)^(n-i-1) 1= ∑_(i=0)^(n-1)〖n-i〗= n+n-1+n-2+…+1 = n(n+1)/2 € Θ(n^2)

    :param arr: A list of elements to be sorted.
    :param key: A callable used to extract a comparison key from each list element.
        This can be a lambda function, a method, or any callable object.
    :param reverse: A boolean indicating whether to sort the list in descending order.
        Defaults to False, which means ascending order.
    :return:
        The sorted list based on the provided key and reverse parameters.
    """
    for i in range(len(arr)):
        for j in range(0, len(arr) - i - 1):
            if (key(arr[j]) < key(arr[j + 1])) if reverse else (key(arr[j]) > key(arr[j + 1])):
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def shell_sort(arr, n, key, reverse=False):
    """
    Sorts the input list using the shell sort algorithm.

    Complexity:
    Best Case: Θ(n log n) - when the list is already sorted.
    Worst Case: Θ(n^2) - when the list is reverse sorted.

    :param reverse: Boolean indicating whether to sort in descending order.
             Defaults to False, which means ascending order.
    :param arr: List of elements to be sorted.
    :param n: Integer representing the length of the list.
    :param key: Function used to extract a comparison key from each element in the list.
    :return: The sorted list.
    """
    gap = n//2
    while gap > 0:
        j = gap
        while j < n:
            i = j - gap
            while i >= 0:
                if (key(arr[i + gap]) > key(arr[i]) and not reverse) or (key(arr[i + gap]) < key(arr[i]) and reverse):
                    break
                else:
                    arr[i+gap], arr[i] = arr[i], arr[i+gap]
                i -= gap
            j += 1
        gap //= 2
    return arr
