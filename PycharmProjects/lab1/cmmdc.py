a = int(input("a = "))
b = int(input("b = "))

while a != b:
    if a > b:
        a -= b
    else:
        b -= a
print("cmmdc = ", a)
