n = int(input())

stars = n - 2
space = 2

for i in range(1, n+1):
    
    print('*\t'*stars, end="")
    print('\t'*space, end="")
    print('\t*'*stars, end="")
    
    print("")
    
    if i <= n/2:
        stars -= 1
        space += 2
    else:
        stars += 1
        space -= 2
    