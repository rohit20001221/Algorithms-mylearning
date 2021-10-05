def backtrack_helper(cur, M, results, m):
    if M == 0:
        results.append(int(cur))
        return

    for i in range(len(cur)-1):
        s = list(cur)
        s[i], s[i+1] = s[i+1], s[i]
        s = "".join(s)
        M_ = M - 1 
        if '{},{}'.format(s, M_) not in m:
            m['{},{}'.format(s, M_)] = True
            backtrack_helper(s, M-1, results, m)
		
def backtrack(N, M):
    results = []
    m = {}
    backtrack_helper(N, M, results, m)
    return max(results)

N = input()
M = int(input())

print(backtrack(N, M))