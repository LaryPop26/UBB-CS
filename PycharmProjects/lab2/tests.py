from functions import *


def test_check_prime():
    assert check_prime(5) == 1
    assert check_prime(9) == 0
    assert check_prime(24) == 0
    assert check_prime(47) == 1


def test_next_prime():
    assert next_prime(9) == 11
    assert next_prime(20) == 23
    assert next_prime(31) == 37


def test_an_bisect():
    assert an_bisect(1999) == 0
    assert an_bisect(2004) == 1


def test_zile_in_luna():
    lista = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    assert zile_in_luna(3, 2010, lista) == 31
    assert zile_in_luna(2, 2004, lista) == 29


def test_varsta():
    assert varsta(26, 7, 2004) == 7316
    assert varsta(5, 8, 2024) == 1


def test_det_data():
    assert det_data(76, 2023) == [2023, 3, 17]


def test_goldbach():
    assert goldbach(8) == [[3, 5]]
    assert goldbach(26) == [[3, 23], [7, 19], [13, 13]]


def test_verifica_gemene():
    assert verifica_gemene(10) == [11, 13]
    assert verifica_gemene(500) == [521, 523]
    assert verifica_gemene(807) == [809, 811]


def test_fibonacci():    # 6
    assert fibonacci(6) == 8
    assert fibonacci(1) == 2
    assert fibonacci(10) == 13
    print("Teste finalizate cu succes!")


def test_produs_factori_proprii():    # 7
    assert produs_factori_proprii(16) == 64
    assert produs_factori_proprii(10) == 10
    print("Teste finalizate cu succes!")


def test_frequency():
    assert frequency(3658) == [0, 0, 0, 1, 0, 1, 1, 0, 1, 0]
    assert frequency(335118445) == [0, 2, 0, 2, 2, 2, 0, 0, 1, 0]


def test_maxim_din_n():
    assert maxim_din_n(3658) == 8653
    assert maxim_din_n(335118445) == 855443311


def test_minim_din_n():
    assert minim_din_n(3658) == 3568
    assert minim_din_n(335118445) == 113344558


def test_verifica_prop():
    assert verifica_prop(2113, 323121) == 1
    assert verifica_prop(2153, 112112) == 0


def test_palindrom():    # 9
    assert det_palindrom(237) == 732
    assert det_palindrom(70) == 7
    print("Teste finalizate cu succes!")


def test_count_prime():
    assert count_prime(1) == 1
    assert count_prime(2) == 2
    assert count_prime(3) == 3
    assert count_prime(4) == 2
    assert count_prime(12) == 5


def test_det_factori():
    assert det_factori(4) == [2, 2]
    assert det_factori(6) == [2, 2, 3, 3, 3]


def test_count_second():
    assert count_second(1) == 1
    assert count_second(2) == 2
    assert count_second(3) == 3
    assert count_second(15) == 3


def test_suma_divizori():
    assert suma_divizori(6) == 6
    assert suma_divizori(9) == 4


def test_bigger_nr_perfect():
    assert bigger_perfect_nr(5) == 6
    assert bigger_perfect_nr(14) == 28


def test_smaller_perfect_nr():
    assert smaller_perfect_nr(7) == 6
    assert smaller_perfect_nr(500) == 496


def test_previous_prime():
    assert previous_prime(9) == 7
    assert previous_prime(20) == 19
    assert previous_prime(31) == 29


def test_1():    # 1
    test_check_prime()
    test_next_prime()
    print("Teste finalizate cu succes!")


def test_2():    # 2
    test_an_bisect()
    test_zile_in_luna()
    test_varsta()
    print("Teste finalizate cu succes!")


def test_3():    # 3
    test_an_bisect()
    test_det_data()
    print("Teste finalizate cu succes!")


def test_4():    # 4
    test_check_prime()
    test_goldbach()
    print("Teste finalizate cu succes!")


def test_5():    # 5
    test_check_prime()
    test_next_prime()
    test_verifica_gemene()
    print("Teste finalizate cu succes!")


def test_8():    # 8
    test_frequency()
    test_maxim_din_n()
    print("Teste finalizate cu succes!")


def test_10():    # 10
    test_frequency()
    test_minim_din_n()
    print("Teste finalizate cu succes!")


def test_11():    # 11
    test_frequency()
    test_verifica_prop()
    print("Teste finalizate cu succes!")


def test_12():    # 12
    test_check_prime()
    test_count_prime()
    print("Teste finalizate cu succes!")


def test_13():    # 13
    test_check_prime()
    test_det_factori()
    test_count_second()
    print("Teste finalizate cu succes!")


def test_14():    # 14
    test_suma_divizori()
    test_bigger_nr_perfect()
    print("Teste finalizate cu succes!")


def test_15():
    test_check_prime()
    test_previous_prime()
    print("Teste finalizate cu succes!")


def test_16():    # 16
    test_suma_divizori()
    test_smaller_perfect_nr()
    print("Teste finalizate cu succes!")
