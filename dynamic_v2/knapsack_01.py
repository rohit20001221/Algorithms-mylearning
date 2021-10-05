def dp(wt, pt, max_wt, idx, m):
    
    if idx <= 0 or wt == 0:
        return 0
    
    if wt[idx-1] <= max_wt:
        if m[max_wt][idx-1] != -1:
            return m[max_wt][idx-1]
        else:
            m[max_wt][idx-1] = max(
                pt[idx-1] + dp(wt, pt, max_wt-wt[idx-1], idx-1, m),
                dp(wt, pt, max_wt, idx-1, m)
            )
    else:
        # dont include the item
        m[max_wt][idx-1] =  dp(wt, pt, max_wt, idx-1, m)
        
    return m[max_wt][idx-1]

def solve(wt, pt, max_wt):
    m = [[-1]*(len(wt)+1)]*(max_wt+1)
    return dp(wt, pt, max_wt, len(wt), m)

if __name__ == '__main__':
    wt =  [ 1, 2, 3, 8, 7, 4 ]
    pt = [ 20, 5, 10, 40, 15, 25 ]
    max_wt = 10
    print(solve(wt, pt, max_wt))