n = int(input("n = "))

if n > 1:
    for i in range(2, (n//2)+1):
        if n % i == 0:
            print("Number", n, "is not prime")
            break
    else:
        print("Number", n, "is prim")
else:
    print("Number", n, "is not prime")
