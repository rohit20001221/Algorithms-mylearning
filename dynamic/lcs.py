s1 = 'abcd'
s2 = 'aebd'

dp = []

for i in range(len(s2)+1):
    arr = [0]*(len(s1)+1)
    dp.append(arr)

s1 += '_'
s2 += '_'

result = ''

for row in reversed(range(len(dp))):
    for col in reversed(range(len(dp[0]))):
        
        if row == len(dp) - 1 or col == len(dp) - 1:
            dp[row][col] = 0
        else:
            if s2[row] != s1[col]:
                dp[row][col] = max(
                    dp[row+1][col],
                    dp[row][col+1],
                )
            else:
                dp[row][col] = dp[row+1][col+1] + 1


for row in dp:
    print(row)