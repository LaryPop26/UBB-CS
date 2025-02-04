
def read_list():
    # number_of_elements = int(input("Enter the number of elements: "))
    # print("Enter the elements: ")
    elements = input().split()
    lst = [int(element) for element in elements]
    # if len(lst) != number_of_elements:
    #    print(f"Warning: You entered {len(lst)} elements instead of {number_of_elements}.")
    if not lst:
        return "List cannot be empty!"
    return lst


def cmmdc(a, b):    # 3
    # Euclid algorithm
    while b:
        a, b = b, a % b
    return a


def is_prime(a):    # 4,7
    if a == 2 or a == 3:
        return True
    if a < 2 or a % 2 == 0 or a % 3 == 0:
        return False
    i = 3
    while i * i <= a:
        if a % i == 0:
            return False
        i += 2
    return True


def distinct_common_digits(a, b, command):    # 14,16
    digits_a = [0] * 10
    digits_b = [0] * 10

    a, b = abs(a), abs(b)

    while a != 0:
        digits_a[a % 10] = 1
        a //= 10

    while b != 0:
        digits_b[b % 10] = 1
        b //= 10

    if command == "14":
        nr = 0
        for i in range(10):
            if digits_a[i] and digits_b[i]:
                nr += 1
        return nr >= 2

    elif command == "16":
        for i in range(10):
            if digits_a[i] != digits_b[i]:
                return False
        return True


def verify_prop(a, b, command):
    if command == "1":      # 1
        return a < b
    if command == "3":      # 3
        return cmmdc(a, b) == 1
    if command == "5":      # 5
        return a == b
    if command == "7":      # 7
        return is_prime(abs(a-b))
    if command == "10" or command == "12":    # 10,12
        return a*b < 0
    if command == "14" or command == "16":
        return distinct_common_digits(a, b, command)


def verify_prop2(a, command):
    if command == "4":    # 4
        return is_prime(a)
    if command == "8":    # 8
        return 0 <= a <= 10


def verify_prop3(a, b, c, command):
    if command == "9":    # 9
        return a == b or a == c or b == c


def maxlen(lst, command):
    length = 0
    lenmax = 0
    ind = -1

    for i in range(len(lst) - 1):
        if verify_prop(lst[i], lst[i + 1], command):
            length += 1
        else:
            length = 0

        if length >= lenmax:
            lenmax = length
            ind = i+1

    if lenmax == 0:
        return [lst[0]]

    return lst[ind - lenmax:ind + 1]


def maxlen2(lst, command):
    length = 0
    lenmax = 0
    ind = -1

    for i in range(len(lst)):
        if verify_prop2(lst[i], command):
            length += 1
        else:
            length = 0

        if length >= lenmax:
            lenmax = length
            ind = i+1

    if lenmax == 0:
        return [lst[0]]

    return lst[ind - lenmax:ind]


def maxlen3(lst, command):
    length = 0
    lenmax = 0
    start_ind = -1
    end_ind = -1

    for i in range(len(lst)-2):
        if verify_prop3(lst[i], lst[i+1], lst[i+2], command):
            if length == 0:
                start_ind = i
            length += 1
        else:
            length = 0
        if length >= lenmax:
            lenmax = length
            end_ind = i + 2

    if lenmax < 3:
        return [lst[0]]

    return lst[start_ind:end_ind + 1]


def maxlen4(lst, command):
    length = 2
    lenmax = -1
    ind = 0

    for i in range(len(lst)-2):
        if verify_prop(lst[i+1]-lst[i], lst[i+2]-lst[i+1], command):
            length += 1
        else:
            length = 2
        if length >= lenmax:
            lenmax = length
            ind = i+3

    if lenmax < 3:
        return [lst[0]]

    return lst[ind - lenmax:ind]


def three_distinct_values(lst):    # 2
    start = 0
    max_len = 0
    max_start = 0
    freq = {}
    for end in range(len(lst)):
        if lst[end] in freq:
            freq[lst[end]] += 1
        else:
            freq[lst[end]] = 1
        while len(freq) > 3:
            freq[lst[start]] -= 1
            if freq[lst[start]] == 0:
                del freq[lst[start]]
            start += 1

        if end - start + 1 >= max_len:
            max_len = end - start + 1
            max_start = start

    return lst[max_start:max_start + max_len]


def all_distinct(lst):    # 6
    length = 0
    lenmax = 0
    aux = []
    result = []
    for i in range(len(lst)):
        if lst[i] in aux:
            while aux[0] != lst[i]:
                del aux[0]
                length -= 1
            del aux[0]
            aux.append(lst[i])
        else:
            length += 1
            aux.append(lst[i])
        if length >= lenmax:
            lenmax = length
            result = aux.copy()
    return result


def max_sum(lst):    # 11
    # Kadane alg
    max_so_far = lst[0]
    max_ending_here = lst[0]
    start = 0
    end = 0
    s = 0
    for i in range(1, len(lst)):
        if lst[i] > max_ending_here + lst[i]:
            max_ending_here = lst[i]
            s = i
        else:
            max_ending_here += lst[i]

        if max_ending_here > max_so_far:
            max_so_far = max_ending_here
            start = s
            end = i

    return lst[start:end + 1]


def max_sum5(lst):    # 13
    s = [lst[0]]
    for i in range(1, len(lst)):
        s.append(s[i - 1] + lst[i])
    # print(s)
    for i in range(len(lst) - 1, -1, -1):
        for j in range(0, len(lst) - i):
            if s[j + i] - s[j] + lst[j] == 5:
                return lst[j:j + i + 1]

    return [lst[0]]


def mountain_seq(lst):    # 15
    length = 0
    lenmax = -1
    ind = 0
    desc = False
    cresc = False
    for i in range(len(lst) - 1):
        if lst[i] < lst[i + 1] and not desc:
            length += 1
            cresc = True
        elif lst[i] < lst[i + 1] and desc:
            length = 1
            desc = False
            cresc = True
        elif lst[i] == lst[i + 1]:
            length = 1
            desc = False
            cresc = False
        elif cresc:
            length += 1
            desc = True
        else:
            length = 0

        if length > lenmax and desc:
            lenmax = length
            ind = i

    if lenmax == -1:
        return [lst[0]]

    return lst[ind - lenmax + 2:ind + 1]


def start_app():
    lista = []
    while True:
        print("'menu' -> show the app menu")
        option = input("Enter a command: ")
        if option == "menu":
            print("Se cauta secventa de lungime maximă cu proprietatea:")
            print("1. x[i] < x[i+1] < ... < x[i+p]")
            print("2. contine cel mult trei valori distincte")
            print("3. oricare doua elemente consecutive sunt relativ prime intre ele")
            print("4. contine doar din numere prime")
            print("5. are toate elementele egale")
            print("6. sunt toate distincte intre ele")
            print("7. oricare doua elemente consecutive difera printr-un numar prim")
            print("8. au toate elementele in intervalul [0, 10] dat")
            print("9. in oricare trei elemente consecutive exista o valoarea care se repeta")
            print("10. diferentele (x[j+1] - x[j]) si (x[j+2] - x[j+1]) au semne contrare, pentru j=i..i+p-2")
            print("11. are suma maxima")
            print("12. are oricare doua elemente consecutive sunt de semne contrare")
            print("13. suma elementelor este egal cu 5")
            print("14. oricare doua elemente consecutive au cel putin 2 cifre distincte comune")
            print("15. reprezinta o secventa sub forma de munte")
            print("16. scrierea lor in baza 10 foloseste aceleasi cifre")
            print("'read' -> read the list")
            print("'exit' -> exit app")
        if option == "read":
            print("Read the list!")
            # lista = read_list()
            # lista = [1, 2, -14, 3, -4, 7, -2, 3, 5, 2, 5, -4, 5, -6, 3]
            # lista = [2, 20, 457, 752, 54235, 3, 135]
            lista = [1, 4, 34, 5675, 6756, 56, 7, 356]
            # lista = [14, 25, 1, 6, 8, 9, 8, 6, 5, 6, 35, 8]
            print(lista)

        if option == "1":
            print(lista)
            print(maxlen(lista, option))

        elif option == "2":
            print(three_distinct_values(lista))

        elif option == "3":
            print(maxlen(lista, option))

        elif option == "4":
            print(maxlen2(lista, option))

        elif option == "5":
            print(maxlen(lista, option))

        elif option == "6":
            print(all_distinct(lista))

        elif option == "7":
            print(maxlen(lista, option))

        elif option == "8":
            print(maxlen2(lista, option))

        elif option == "9":
            print(maxlen3(lista, option))

        elif option == "10":
            print(maxlen4(lista, option))

        elif option == "11":
            print(max_sum(lista))

        elif option == "12":
            print(maxlen(lista, option))

        elif option == "13":
            print(max_sum5(lista))

        elif option == "14":
            print(maxlen(lista, option))

        elif option == "15":
            print(mountain_seq(lista))

        elif option == "16":
            print(maxlen(lista, option))

        elif option == "exit":
            break

        elif option != "menu" and option != "read" and option != "exit" and option not in range(1, 16):
            print("Wrong option!")


if __name__ == "__main__":
    start_app()
