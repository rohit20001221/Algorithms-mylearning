from functools import lru_cache

@lru_cache(maxsize=None)
def gridTraveler(n, m):
    
    if n == 1 and m == 1:
        return 1
    
    if n == 0 or m == 0:
        return 0
    
    return gridTraveler(n-1, m) + gridTraveler(n, m-1)

print(gridTraveler(3,5))