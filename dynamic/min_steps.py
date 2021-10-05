def minSteps(n):
    dp = [0]*n
    
    for i in range(1,len(dp)):
        if i % 2 != 0:
            dp[i] = dp[i-1] + 1
        else:
            dp[i] = min(dp[i-i//2:i]) + 1
    
    return dp[n-1]

n = int(input())
print(minSteps(n))