def fib(n):
    table = [0] * (n+1)
    table[1] = 1
    
    
    for i in range(n+1):
        try:
            table[i+1] += table[i]
            table[i+2] += table[i]
        except:
            continue
    
    return table

print(fib(100))
    