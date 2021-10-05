from functools import lru_cache

@lru_cache(maxsize=None)
def optimalTree(p, q, i, j, m):
    if j < i:
        return 0
    
    if i == j:
        m[f'{i}{j}'] = i
        return p[i] + q[j]
    
    MIN = 2 ** 10
    W = sum(p[i:j+1] + q[i:j+1])
    minK = None
    
    for r in range(i, j+1):
        cost = optimalTree(p, q, i, r-1, m) + optimalTree(p, q, r+1, j, m) + W
        
        if cost < MIN:
            minK = r
            MIN = cost

    m[f'{i}{j}'] = minK   
    return MIN


p = [0, 3, 3, 1, 1]
q = [2, 3, 1, 1, 1]
m = {}

print(optimalTree(p, q, 0, 4, m))
print(m)
