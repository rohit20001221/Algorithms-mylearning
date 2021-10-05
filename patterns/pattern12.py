n = int(input())

a = 0
b = 1

for i in range(n):
    for j in range(n):
        if j <= i:
            print(str(a) + "\t", end="")
            c = a+b
            a = b
            b = c
        else:
            print("\t", end="")
    print("")