from tests import *


def start():
    while True:
        print("'menu' -> show the app menu")
        option = input("Enter an option: ")
        if option == "menu":
            print("1. Găsiți primul număr prim mai mare decât un număr dat")
            print("2. Se da data nașterii (zi/luna/an), determinați vârsta persoanei in zile")
            print("3. Determina o data calendaristica (sub forma an, luna, zi)")
            print("4. Ipoteza lui Goldbach")
            print("5. Numere prime gemene")
            print("6. Fibonacci")
            print("7. Produsul factorilor proprii ai numarului n")
            print("8. Numar maxim format cu cifrele numarului n")
            print("9. Palindrom")
            print("10. Numar minim format cu cifrele numarului n")
            print("11. Verificare cifre a 2 numere n1 si n2")
            print("12. Elementul n al sirului 1,2,3,2,5,2,3,7,2,3,2,5,...")
            print("13. Elementul n al sirului 1,2,3,2,2,5,2,2,3,3,3,...")
            print("14. Cel mai mic numar perfect mai mare decat un numar dat")
            print("15. Cel mai mare numar prim mai mic decat un numar dat")
            print("16. Cel mai mare numar perfect mai mic decat un numar dat")
            print("'exit' -> exit app")
        if option == "1":
            command = input("Introducere date/teste:(y/t/n): ")
            if command == "y":
                n = int(input("n = "))
                urm_nr_prim = next_prime(n)
                print(f"Cel mai mic numar prim mai mare decat cel dat este {urm_nr_prim}")
            elif command == "t":
                test_1()
            elif command == "n":
                pass
            else:
                print("Optiune invalida! Revenire la meniul principal")

        if option == "2":
            command = input("Introducere date/teste:(y/t/n): ")
            if command == "y":
                zi = int(input("zi: "))
                luna = int(input("luna: "))
                an = int(input("an: "))

                varsta_in_zile = varsta(zi, luna, an)
                print(f"Varsta persoanei este: {varsta_in_zile} zile")
            elif command == "t":
                test_2()
            elif command == "n":
                pass
            else:
                print("Optiune invalida! Revenire la meniul principal")

        if option == "3":
            command = input("Introducere date/teste:(y/t/n): ")
            if command == "y":
                an = int(input("an: "))
                nr_zi = int(input("nr_ordine_zi: "))
                data = det_data(nr_zi, an)
                print(f"Data e: {data[0]}-{data[1]:02}-{data[2]:02}")
            elif command == "t":
                test_3()
            elif command == "n":
                pass
            else:
                print("Optiune invalida! Revenire la meniul principal")

        if option == "4":
            command = input("Introducere date/teste:(y/t/n): ")
            if command == "y":
                n = int(input("Introdu numarul: "))
                result = goldbach(n)
                print(result)
            elif command == "t":
                test_4()
            elif command == "n":
                pass
            else:
                print("Optiune invalida! Revenire la meniul principal")

        if option == "5":
            command = input("Introducere date/teste:(y/t/n): ")
            if command == "y":
                n = int(input("Introdu un numar: "))
                result = verifica_gemene(n)
                print(f"Numerele gemene sunt: {result[0]} si {result[1]}")
            elif command == "t":
                test_5()
            elif command == "n":
                pass
            else:
                print("Optiune invalida! Revenire la meniul principal")

        if option == "6":
            command = input("Introducere date/teste:(y/t/n): ")
            if command == "y":
                x = int(input("n = "))
                result = fibonacci(x)
                print(f"Cel mai mic numar din sirul lui Fibonacci mai mare decat {x} este {result}")
            elif command == "t":
                test_fibonacci()
            elif command == "n":
                pass
            else:
                print("Optiune invalida! Revenire la meniul principal")

        if option == "7":
            command = input("Introducere date/teste:(y/t/n): ")
            if command == "y":
                x = int(input("Introdu un numar: "))
                produs = produs_factori_proprii(x)
                print(f"Produsul factorilor proprii ai numarului {x} este {produs}")
            elif command == "t":
                test_produs_factori_proprii()
            elif command == "n":
                pass
            else:
                print("Optiune invalida! Revenire la meniul principal")

        if option == "8":
            command = input("Introducere date/teste:(y/t/n): ")
            if command == "y":
                x = int(input("Introdu un numar: "))
                maxim = maxim_din_n(x)
                print(f"Cel mai mare numar format cu cifrele numarului dat este: {maxim}")
            elif command == "t":
                test_8()
            elif command == "n":
                pass
            else:
                print("Optiune invalida! Revenire la meniul principal")

        if option == "9":
            command = input("Introducere date/teste:(y/t/n): ")
            if command == "y":
                x = int(input("Introdu un numar: "))
                result = det_palindrom(x)
                print(f"Palindromul nr {x} este {result}")
            elif command == "t":
                test_palindrom()
            elif command == "n":
                pass
            else:
                print("Optiune invalida! Revenire la meniul principal")

        if option == "10":
            command = input("Introducere date/teste:(y/t/n): ")
            if command == "y":
                x = int(input("Introdu un numar: "))
                m = minim_din_n(x)
                print(f"Cel mai mic numar format cu cifrele numarului dat este: {m}")
            elif command == "t":
                test_10()
            elif command == "n":
                pass
            else:
                print("Optiune invalida! Revenire la meniul principal")

        if option == "11":
            command = input("Introducere date/teste:(y/t/n): ")
            if command == "y":
                x1 = int(input("Introdu un numar: "))
                x2 = int(input("Introdu un numar: "))
                if verifica_prop(x1, x2):
                    print(f"{x1} si {x2} verifica proprietatea P")
                else:
                    print(f"{x1} si {x2} nu verifica proprietatea P")
            elif command == "t":
                test_11()
            elif command == "n":
                pass
            else:
                print("Optiune invalida! Revenire la meniul principal")

        if option == "12":
            command = input("Introducere date/teste:(y/t/n): ")
            if command == "y":
                x = int(input("Introdu un numar: "))
                search = count_prime(x)
                print(f"Elementul cautat din sir este: {search}")
            elif command == "t":
                test_12()
            elif command == "n":
                pass
            else:
                print("Optiune invalida! Revenire la meniul principal")

        if option == "13":
            command = input("Introducere date/teste:(y/t/n): ")
            if command == "y":
                x = int(input("Introdu un numar: "))
                search = count_second(x)
                print(f"Elementul cautat din sir este: {search}")
            elif command == "t":
                test_13()
            elif command == "n":
                pass
            else:
                print("Optiune invalida! Revenire la meniul principal")

        if option == "14":
            command = input("Introducere date/teste:(y/t/n): ")
            if command == "y":
                n = int(input("Introdu un numar: "))
                urm = bigger_perfect_nr(n)
                print(f"Cel mai mic număr perfect mai mare decât {n} este {urm}")
            elif command == "t":
                test_14()
            elif command == "n":
                pass
            else:
                print("Optiune invalida! Revenire la meniul principal")

        if option == "15":
            command = input("Introducere date/teste:(y/t/n): ")
            if command == "y":
                n = int(input("n = "))
                nr_prim_anterior = previous_prime(n)
                if nr_prim_anterior == -1:
                    print("nu exista!")
                else:
                    print(f"Cel mai mic numar prim mai mic decat cel dat este {nr_prim_anterior}")
            elif command == "t":
                test_15()
            elif command == "n":
                pass
            else:
                print("Optiune invalida! Revenire la meniul principal")

        if option == "16":
            command = input("Introducere date/teste:(y/t/n): ")
            if command == "y":
                n = int(input("Introdu un numar:"))
                prev = smaller_perfect_nr(n)
                print(f"Cel mai mare număr perfect mai mic decât {n} este {prev}")
            elif command == "t":
                test_16()
            elif command == "n":
                pass
            else:
                print("Optiune invalida! Revenire la meniul principal")

        if option == "exit":
            break


if __name__ == '__main__':
    start()
