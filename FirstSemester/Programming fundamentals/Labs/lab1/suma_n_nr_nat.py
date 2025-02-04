n = int(input("n = "))

if n < 0:
    print("Give a natural number!")
else:
    s = 0
    for i in range(n):
        x = int(input())
        s += x
    print("Sum is:", s)

"""
s = 0 
l = []
for i in range(n):
    x = int(input())
    l.append(x)
for el in l:
    s += el
print("Sum is: ", s)

"""