n = int(input())

nsp = 2 * n - 3
nst = 1


for i in range(1, n+1):
    
    val = 1
        
    for j in range(nst):
        print(f"{val}\t", end="")
        val += 1
    
    for j in range(nsp):
        print("\t", end="")
    
    if i == n:
        nst -= 1
        val -= 1
    
    for j in range(nst):
        val -= 1
        print(f"{val}\t", end="")
    
    print("")

    nst += 1
    nsp -= 2