n = int(input("n = "))

if n < 0:
    print("Give a natural number: ")
else:
    s = 0
    for i in range(1, n+1):
        s += i
    print("Sum is: ", s)
"""

if n<0:
    print("Give a natural number: ")
else:
    suma = 0
    while n>0:
        suma += n
        n-=1
    print("Sum is: ",suma)
"""