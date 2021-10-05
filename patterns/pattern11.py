n = int(input())

num = 1

for i in range(n):
    for j in range(n):
        if j <= i:
            print(str(num) + "\t", end="")
            num += 1
        else:
            print("\t", end="")
    print("")