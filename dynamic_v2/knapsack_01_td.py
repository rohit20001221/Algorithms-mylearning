def solve(wt, pt, max_wt):
    n = len(wt)
    w = max_wt
    
    dp = []
    
    for i in range(n+1):
        arr = [-1]*(w+1)
        dp.append(arr)
    
    for row in dp:
        print(row)
    
    for row in range(n+1):
        for col in range(w+1):
            if row == 0 or col == 0:
                dp[row][col] = 0
            else:
                max_wt_ = col
                print(col)
                if wt[row-1] > max_wt_:
                    dp[row][col] = dp[row-1][col]
                else:
                    dp[row][col] = max(
                        pt[row-1] + dp[row-1][max_wt_-wt[row-1]],
                        dp[row-1][max_wt_]
                    )
    
    for row in dp:
        print(row)
    

wt =  [ 1, 2, 3, 8, 7, 4 ]
pt = [ 20, 5, 10, 40, 15, 25 ]
max_wt = 10

solve(wt, pt, max_wt)
    