def maxProduct(n):
    
    if n < 4:
        return n
    
    # if n == 4:
    #     return 4
    
    res = []
    
    for i in range(1,n):
        if n - i >= 0:
            res.append(i*maxProduct(n-i))
    
    return max(res, default=0)

print(maxProduct(4))