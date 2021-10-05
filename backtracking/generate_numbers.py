def backtrack_helper(curnum, i, n, solutions):
    if i == n:
        solutions.append(curnum)
        return
    
    # add the 1 << i
    backtrack_helper(curnum + (1 << i), i + 1, n, solutions)
    # dont add the 1 << i
    backtrack_helper(curnum, i + 1, n, solutions)

def backtrack(n):
    solutions = []
    backtrack_helper(1, 0, 3, solutions)
    return solutions

result = backtrack(3)
result.sort()

print(result)