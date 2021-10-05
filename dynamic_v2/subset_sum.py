def dp(nums, target, idx, m):    
    if target == 0:
        return True
    
    if idx == 0:
        return False
    
    if m[idx][target] != -1:
        return m[idx][target]
    else:
        if nums[idx-1] <= target:
            m[idx][target] = dp(nums, target-nums[idx-1], idx-1, m) or dp(nums, target, idx-1, m)
        else:
            m[idx][target] = dp(nums, target, idx-1, m)

    return m[idx][target]

def solve(nums, target):
    n = len(nums)
    m = target
    
    mm = []
    
    for _ in range(n+1):
        arr = [-1]*(m+1)
        mm.append(arr)
    
    # for row in mm:
    #     print(row)
    
    result = dp(nums, target, len(nums), mm)
    
    # for row in mm:
    #     print(row)
    
    return result

print(solve([2,3,7,8,10], 11))
