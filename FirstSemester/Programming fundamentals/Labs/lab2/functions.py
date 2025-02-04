import datetime


def check_prime(number):    # 1, 5
    """
    Verify if a number is prime.
    :param number: an integer value
    :return: True if the number is prime, False otherwise
    """
    if number <= 1:
        return False
    if number == 2 or number == 3:
        return True
    if number % 2 == 0 or number % 3 == 0:
        return False
    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6
    return True


def next_prime(number):    # 1, 5
    """
    Search the next prime number after n.
    :param number: an integer value
    :return: next - the next prime number after n
    """
    next_number = number + 1
    while not check_prime(next_number):
        next_number += 1
    return next_number


def verifica_gemene(number):    # 5
    """
    Verify if two prime numbers are twins
    :param number: an integer value
    :return:list of the next two twin numbers after the given number
    """
    p = next_prime(number)
    q = next_prime(p)
    while q - p != 2:
        p = q
        q = next_prime(p)
    if q - p == 2:
        return [p, q]


def an_bisect(year):    # 2, 3
    """
    Check if a year is a leap year
    :param year: an integer value, the specific year
    :return: true if the year is a leap year, false otherwise
    """
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def zile_in_luna(month, year, lista):    # 2
    """
    Search how many days are in a month
    :param month: an integer value, the specific month
    :param year: an integer value, the specific year
    :param lista: lista cu nr de zile pt fiecare luna
    :return: m - numarul de zile din luna month
    """
    if month == 2 and an_bisect(year):
        return 29
    return lista[month - 1]


def varsta(day, month, year):    # 2
    """
    Determine the person's age in days
    :param day: an integer value, day of birth
    :param month: an integer value, month of birth
    :param year: an integer value, year of birth
    :return: nr_zile - an integer value, the number of days
    """
    lista = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    current_time = datetime.datetime.now()
    current_day = current_time.day
    current_month = current_time.month
    current_year = current_time.year
    nr_zile = 0

    if year == current_year:
        if month == current_month:
            nr_zile = current_day - day
        else:
            nr_zile += zile_in_luna(month, year, lista) - day
            for m in range(month + 1, current_month):
                nr_zile += zile_in_luna(m, year, lista)
            nr_zile += current_day
    else:
        nr_zile += zile_in_luna(month, year, lista) - day
        for m in range(month + 1, 13):
            nr_zile += zile_in_luna(m, year, lista)
        for y in range(year + 1, current_year):
            nr_zile += 366 if an_bisect(y) else 365
        for m in range(1, current_month):
            nr_zile += zile_in_luna(m, current_year, lista)
        nr_zile += current_day

    return nr_zile


def det_data(day_number, year):    # 3
    """
    Determine the calendar date by knowing the order number of the day of the year
    :param day_number: an integer value
    :param year: an integer value
    :return: list of numbers
    """
    lista = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if an_bisect(year):
        lista[1] = 29

    month = 0
    while day_number > lista[month]:
        day_number -= lista[month]
        month += 1

    return [year, month + 1, day_number]


def goldbach(n):    # 4
    """
    Checks if n = p1 + p2,where p1 and p2 are prime numbers
    There is a solution for any even integer greater than 2
    :param n: nr intreg
    :return: p1 si p2 daca se verifica proprietatea
    """
    result = []
    for i in range(2, n//2+1):
        if check_prime(i) and check_prime(n-i):
            result.append([i, n-i])
    return result


def fibonacci(n):    # 6
    """
    Calculate the terms of the Fibonacci sequence in turn
    :param n: natural numbeer ,
    :return: f_next, an integer value, the number in the series that verifies the property
    """
    f0, f1 = 1, 1

    while True:
        f_next = f0 + f1
        if f_next > n:
            return f_next
        f0, f1 = f1, f_next


def produs_factori_proprii(n):    # 7
    """
    Calculate the product of the proper factors of n
    :param n: an integer value
    :return: p - an integer value, the product
    """
    p = 1
    if n <= 1:
        return 1
    ok = False
    for i in range(2, n):
        if n % i == 0:
            p *= i
            ok = True
    return p if ok else 1


def frequency(n):    # 8, 10
    """
    Determine the frequency of each digit in n
    :param n: an integer value
    :return: cifre - list of frequency
    """
    cifre = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    while n > 0:
        cifre[n % 10] += 1
        n = n//10
    return cifre


def maxim_din_n(n):     # 8
    """
    The maximum number is formed with the digits given by going through the frequency list
    :param n: an integer value
    :return: m - an integer value
    """
    cifre = frequency(n)
    m = 0
    for i in range(9, -1, -1):
        while cifre[i] > 0:
            m = m * 10 + i
            cifre[i] -= 1
    return m


def minim_din_n(n):    # 10
    """
    The minimum number is formed with the digits given by going through the frequency list
    :param n: an integer value
    :return: m - an integer value
    """
    cifre = frequency(n)
    minim = 0
    for i in range(1, len(cifre)):
        while cifre[i] > 0:
            minim = minim * 10 + i
            cifre[i] -= 1
    return minim


def verifica_prop(n1, n2):    # 11
    """
    Check if the 2 numbers contain the same digits
    :param n1: an integer value
    :param n2: an integer value
    :return: true, if the condition is true, false otherwise
    """
    cifre1 = frequency(n1)
    cifre2 = frequency(n2)
    for i in range(0, len(cifre1)):
        for j in range(0, len(cifre2)):
            if i == j:
                if cifre1[i] == 0 and not cifre2[j] == 0:
                    return False
                if cifre2[j] == 0 and not cifre1[i] == 0:
                    return False
    return True


def det_palindrom(n):   # 9
    """
    Calculate the palindrome of the number n
    :param n: an integer value
    :return: invers - an integer value, the palindrome
    """
    copie = n
    invers = 0
    while copie > 0:
        invers = invers * 10 + copie % 10
        copie = copie//10
    return invers


def count_prime(n):    # 12
    """
    Search for the nth one in the required string
    :param n:an integer value
    :return:an integer value
    """
    if n == 1:
        return 1
    count = 1
    current_number = 2

    while count < n:
        if check_prime(current_number):
            count += 1
            if count == n:
                return current_number
        else:
            num = current_number
            d = 2
            while num > 1:
                if num % d == 0:
                    while num % d == 0:
                        count += 1
                        if count == n:
                            return d
                        while num % d == 0:
                            num //= d
                d += 1
                if d * d > num:
                    if num > 1:
                        count += 1
                        if count == n:
                            return num
                    break
        current_number += 1


def det_factori(num):    # 13 NU E GATA
    """
    Find all the prime factors of a number
    In this case, the returned list will have all terms multiplied so that their number is equal to the divisor
    :param num:an integer value
    :return: factoriprimi - list of all prime factors of number num
    """
    factoriprimi = []
    if num % 2 == 0:
        factoriprimi.append(2)
        factoriprimi.append(2)
    while num % 2 == 0:
        num = num // 2

    for i in range(3, num, 2):
        if num % i == 0:
            while num % i == 0:
                num = num // i
            j = i
            while j > 0:
                factoriprimi.append(i)
                j -= 1

    if num > 2:
        num1 = num
        while num1 > 0:
            factoriprimi.append(num)
            num1 -= 1
    return factoriprimi


def count_second(n):    # 13
    """
    Search for the nth one in the required string
    :param n:an integer value
    :return:an integer value
    """
    count = 0
    current_number = 1
    while True:
        if current_number == 1:
            count += 1
            if count == n:
                return current_number
        else:
            if check_prime(current_number):
                count += 1
                if count == n:
                    return current_number
            else:
                factori = det_factori(current_number)
                for f in factori:
                    count += 1
                    if count == n:
                        return f
        current_number += 1


def suma_divizori(num):    # 14
    """
    Calculates the sum of the divisors of the number num
    :param num: an integer value
    :return: sum - an integer value, sum of the divisors
    """
    s = 0
    for i in range(1, num):
        if num % i == 0:
            s += i
    return s


def bigger_perfect_nr(num):    # 14
    """
    Search the next perfect number after the given one
    A number is perfect if he is equal with the sum of his divisors
    :param num: an integer value
    :return: current - an integer value , the search one if the property is true
    """
    current = num + 1
    while True:
        if suma_divizori(current) == current:
            return current
        current += 1


def smaller_perfect_nr(num):    # 16
    """
    Search the previous perfect number before the given one
    A number is perfect if he is equal with the sum of his divisors
    :param num: an integer value
    :return: current - an integer value , the search one if the property is true
    """
    current = num - 1
    while True:
        if suma_divizori(current) == current:
            return current
        current -= 1


def previous_prime(number):    # 15
    """
    Search the previous prime number before n.
    :param number: an integer value
    :return: i - the previous prime number before n
    """
    for i in range(number-1, 2, -1):
        if check_prime(i):
            return i
    return -1
