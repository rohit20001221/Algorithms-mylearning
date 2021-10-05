def howSum(target, nums, m={}):
    if target == 0: return []
    if target < 0: return None
    
    for num in nums:
        remainder = target - num
        
        if remainder in m:
            return m[remainder]
        else:
            result = howSum(remainder, nums)
            if result != None:
                m[remainder] = result + [num]
                return m[remainder]
    
    return None

mm = {}
print(howSum(8, [4,1,2], mm))
print(mm)