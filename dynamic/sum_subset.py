nums = [2,2,2,1]
target = 5

def solve(nums, target):
    return solve_subset(nums, target, len(nums) - 1, 0)

def solve_subset(nums, target, index, sum):
    if index == -1:
        return False
    if sum == target:
        return True
    
    # include the element
    s1 = solve_subset(nums, target, index - 1, sum + nums[index])
    # exclude the element
    s2 = solve_subset(nums, target, index - 1, sum)
    
    return s1 or s2

mm = {}
def solve_v1(nums, target, m):
    if(target == 0):
        return True
    
    if target < 0:
        return False
    
    for num in nums:
        remainder = target - num
        if remainder in m:
            return m[remainder]
        else:
            if solve_v1(nums, remainder, m):
                m[remainder] = True
                return m[remainder]
    
    return False



print(solve_v1(nums, target, mm))