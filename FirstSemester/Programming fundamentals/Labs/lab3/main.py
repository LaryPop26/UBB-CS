def read_list():
    # number_of_elements = int(input("Enter the number of elements: "))
    # if number_of_elements <= 0:
    #    print(f"Warning: List cannot have {number_of_elements} elements! Try again!")
    # print("Enter the elements: ")
    elements = input().split()
    lst = [int(element) for element in elements]
    # if len(lst) != number_of_elements:
    #    print(f"Warning: You entered {len(lst)} elements instead of {number_of_elements}!")
    if not lst:
        return "List cannot be empty!"
    return lst

def three_distinct_values(lst):    # 2
    """
    Functia cauta cea mai lunga secventa avand maxim 3 valori distince
    :param lst: lista de numere
    :return: lst, lista ce respecta cerinta
    """
    start = 0
    max_len = 0
    max_start = 0
    freq = {}
    for el in range(len(lst)):
        if lst[el] in freq:
            freq[lst[el]] += 1
        else:
            freq[lst[el]] = 1

        while len(freq) > 3:
            freq[lst[start]] -= 1
            if freq[lst[start]] == 0:
                del freq[lst[start]]
            start += 1

        if el - start + 1 >= max_len:
            max_len = el - start + 1
            max_start = start

    return lst[max_start:max_start + max_len]

def cmmdc(a, b):    # 3
    """
    Cauta cel mai mic divizor comun al 2 numere
    :param a: int, primul nr intreg
    :param b: int, al 2-lea nr intreg
    :return: a,int, cmmmdc al celor 2 numere
    """
    # Euclid algorithm
    while b:
        a, b = b, a % b
    return a

def distinct_common_digits(a, b, command):    # 16
    """
    Functia verifica daca 2 numere contin exact aceleasi cifre
    :param a: int, primul nr
    :param b: int, al 2-lea nr intreg
    :return: t/f, valoarea de adevar returnata
    """
    digits_a = [0] * 10
    digits_b = [0] * 10

    a, b = abs(a), abs(b)

    while a != 0:
        digits_a[a % 10] = 1
        a //= 10

    while b != 0:
        digits_b[b % 10] = 1
        b //= 10

    for i in range(10):
        if digits_a[i] != digits_b[i]:
            return False
    return True

def verify_prop(a, b, command):
    if command == "3":      # 3
        return cmmdc(a, b) == 1
    if command == "2":     # 16
        return distinct_common_digits(a, b, command)

def maxlen(lst, command):
    """
    Cauta secventa de lungime maxima cu o anumita proprietate
    :param lst: list, lista de numere
    :param command: int, optiunea din meniu
    :return: lst, lista ceruta
    """
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

def print_menu():
    print("'read' -> read the list")
    print("Afiseaza secventa de lungime maximă cu proprietatea:")
    print("1. contine cel mult trei valori distincte")
    print("2. scrierea lor in baza 10 foloseste aceleasi cifre")
    print("3. oricare doua elemente consecutive sunt relativ prime intre ele")
    print("'exit' -> exit app")

def start_app():
    lista = []
    while True:
        print("'menu' -> show the app menu")
        option = input("Enter a command: ")
        if option == "menu":
            print_menu()
        if option == "read":
            print("Read the list!")
            # lista = read_list()
            # lista = [1, 2, -14, 3, -4, 7, -2, 3, 5, 2, 5, -4, 5, -6, 3]
            # lista = [2, 20, 457, 752, 54235, 3, 135]
            lista = [1, 4, 34, 5675, 3311, 131, 31,  49, 7, 356]
            # lista = [2, 4, 6, 7, 8, 13, 25, 5, 2]
            print(lista)
            print("Saved!")

        elif option == "check":
            print(f"{len(lista)} elements in list")
            print(lista)

        elif option == "1":
            test_valori_distincte()
            print(f"Secventa de lungime maximă ce contine cel mult trei valori distincte este "
                  f"{three_distinct_values(lista)}")

        elif option == "2":
            print(f"Secventa de lungime maximă cu scrierea numerelor in baza 10 foloseste aceleasi cifre este "
                  f"{maxlen(lista, option)}")

        elif option == "3":
            print(f"Secventa de lungime maximă unde oricare doua elemente consecutive sunt relativ prime intre ele "
                  f"{maxlen(lista, option)} ")

        elif option == "exit":
            break

        elif option not in ["1", "2", "menu", "exit", "check"]:
            print("Wrong command! Try again!")

def test_valori_distincte():
    lista = [1, 2, 3, 4, 5]
    assert (three_distinct_values(lista) == [3, 4, 5])
    lista2 = [1, 2, 3, 1, 2, 3, 2, 2]
    assert (three_distinct_values(lista2) == [1, 2, 3, 1, 2, 3, 2, 2])
    lista3 = [1, 1, 2]
    assert (three_distinct_values(lista3) == [1, 1, 2])
    lista4 = [1, 1]
    assert (three_distinct_values(lista4) == [1, 1])
    print("Succes!")


start_app()
