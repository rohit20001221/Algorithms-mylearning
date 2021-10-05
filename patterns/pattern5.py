import math

n = int(input())

space = n // 2
star  = 1

for i in range(1, n+1):
    
    print(' '*space + '*'*star)
    
    if i <= n / 2:
        space -= 1
        star  += 2
    else:
        space += 1
        star -= 2
        
