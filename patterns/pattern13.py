n = int(input())

num = 1

for i in range(n+1):
    for j in range(n+1):
        if j <= i:
            if j == 0 or (i == j):
                print("1\t", end="")
                num = i
            else:
                print(str(num) + "\t", end="")
                num = int(num * (i - j) / ( j + 1)) # <- this is formula for calculating next digit
    print("")
