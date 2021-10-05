def solve(nums, target):
    dp = []
    
    n = len(nums)
    m = target
    
    for i in range(n+1):
        arr = [False]*(m+1)
        dp.append(arr)
    
    for row in range(len(dp)):
        for col in range(len(dp[row])):
            
            if row == 0:
                dp[row][col] = False
            
            if col == 0:
                dp[row][col] = True
            
            if row != 0 and col != 0:
                if nums[row-1] <= col:
                    dp[row][col] = dp[row-1][col] or dp[row-1][col - nums[row-1]]
                else:
                    dp[row][col] = dp[row-1][col]
            
    for row in dp:
        print(row)
    
    return dp[n][m]  

print(solve([2,3,7,8,10], 11))
