def solve(arr):
    s = sum(arr)
    
    if s % 2 != 0:
        return False
    
    target = s // 2
    
    dp = []
    
    n = len(arr)
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
                if arr[row-1] <= col:
                    dp[row][col] = dp[row-1][col] or dp[row-1][col - arr[row-1]]
                else:
                    dp[row][col] = dp[row-1][col]
    
    for row in dp:
        print(row)
    
    return dp[n][m]

print(solve([1,5,11,5]))