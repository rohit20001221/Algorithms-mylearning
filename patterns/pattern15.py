n = int(input())

outer_space = n // 2
inner_space = 1

val = 1
cval = 1

for i in range(1, n+1):
    print("\t"*outer_space, end="")
    
    for j in range(0, inner_space):
        print(f"{cval}\t",end="")
        
        if j < inner_space // 2:
            cval += 1
        else:
            cval -= 1
    
    if i <= n // 2:
        outer_space -= 1
        inner_space += 2
        val += 1
    else:
        outer_space += 1
        inner_space -= 2
        val -= 1
    
    cval = val
    
    print("")