n = int(input())


outer_space = n // 2
inner_space = -1

for i in range(1, n+1):
    print('\t'*outer_space, end="")
    
    if inner_space == -1:
        print("*\t", end="")
    else:
        print("*\t", end="")
        print("\t"*inner_space, end="")
        print("*\t", end="")
    
    if i <= n // 2:
        outer_space -= 1
        inner_space += 2
    else:
        outer_space += 1
        inner_space -= 2
    
    print("")