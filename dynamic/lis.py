arr = [3,1,4,1,5,9,2,6,5,4,5,3,9,7,9]

dp = [0]*len(arr)
prev = {}


for i in range(1, len(dp)):
    max_ = dp[i]
    k = None
    
    for j in range(0,i):
        if arr[j] < arr[i] and dp[j] > max_: # <- check for the smallest element
            max_ = dp[j]
            k = j
    
    dp[i] = max_ + 1
    prev[i] = k

print(dp)
print(prev)