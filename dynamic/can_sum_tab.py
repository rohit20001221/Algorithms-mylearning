def canSum(target, nums):
    
    table = [False]*(target + 1)
    table[0] = True
    
    for val in range(len(table)):
        for num in nums:
            if val - num >= 0:
                table[val] = table[val-num]
    
    return table[target]

print(canSum(7, [5,3,4]))