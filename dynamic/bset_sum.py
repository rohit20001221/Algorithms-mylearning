import time

def bestSum(target, nums, m):
    if target == 0: return []
    if target < 0: return None
    
    shortestCombination = None
    
    for num in nums:
        remainder = target - num
        
        if remainder in m:
            return m[remainder]
        else:
            remainderCombination = bestSum(remainder, nums, m)

            if remainderCombination != None:
                combination = remainderCombination + [num]
                
                if shortestCombination == None or len(shortestCombination) > len(combination):
                    shortestCombination  = combination
    
        m[target] = shortestCombination
        return m[target]

nums = [1,3]
target = 100
mm = {}

t1 = time.time()
print(bestSum(target, nums, mm))
t2 = time.time()

print(t2 - t1)