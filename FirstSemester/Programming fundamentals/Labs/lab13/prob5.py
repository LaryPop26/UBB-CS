"""
Pronosport – bilet cu n meciuri
    solutie candidat:
        x = (x0, … , xk) ; xi € {1,2,’X’}

    conditie consistenta:
        x = (x0, … , xk) – consistent - ∀  j≤2 ,j = nr total de ‘1’, xk ≠ ‘X’

    conditie solutie:
        x = (x0, … , xk) e solutie cand e consistent si k = n
"""

def menu():
    print("Generați bilete la PRONOSPORT pentru un bilet cu N meciuri. Pronosticurile pentru un meci pot fi 1,X,2. \n"
          "Generați toate variantele astfel încât: pronosticul de la ultimul meci nu poate fi X și "
          "există un maxim de două meciuri cu pronosticul 1.")
    print("Modalitatea de rezolvare:")
    print("1. Iterativ")
    print("2. Recursiv")
    print("0. Iesire")

# iterativ
def pronosport_iterativ(n: int):
    if n <= 0:
        return []

    stiva = [([], 0)]
    bilete = []

    while stiva:
        bilet_curent, count_1 = stiva.pop()

        if len(bilet_curent) == n:
            bilete.append(bilet_curent)
            continue

        variante = ['1', 'X', '2'] if len(bilet_curent) < n - 1 else ['1', '2']

        for optiune in variante:
            if optiune == '1' and count_1 + 1 > 2:
                continue
            stiva.append((bilet_curent + [optiune], count_1 + (1 if optiune == '1' else 0)))

    return bilete

# recursiv
def pronosport_recursiv(n: int, bilet_curent=None, count_1=0):
    if n <= 0:
        return []

    if bilet_curent is None:
        bilet_curent = []

    if len(bilet_curent) == n:
        return [bilet_curent]

    variante = ['1', 'X', '2'] if len(bilet_curent) < n - 1 else ['1', '2']

    bilete = []
    for optiune in variante:
        if optiune == '1' and count_1 + 1 > 2:
            continue

        bilet_nou = bilet_curent + [optiune]
        # print(bilet_nou)
        bilete += pronosport_recursiv(n, bilet_nou, count_1 + (1 if optiune == '1' else 0))
    return bilete

def print_lst(lst):
    if len(lst) == 0:
        print("0 valori obtinute!")
    for el in lst:
        print(el)

def run5():
    while True:
        menu()
        optiune = int(input("\n>>> "))
        n = int(input("Introdu numarul de bilete: n = "))
        match optiune:
            case 1:
                bilete = pronosport_iterativ(n)
                print(f"Exista {len(bilete)} bilete PRONOSPORT pentru n = {n}:")
                print_lst(bilete)

            case 2:
                bilete = pronosport_recursiv(n)
                print(f"Exista {len(bilete)} bilete PRONOSPORT pentru n = {n}:")
                print_lst(bilete)

            case 0:
                break
            case _:
                print("Optiune invalida!")

run5()
