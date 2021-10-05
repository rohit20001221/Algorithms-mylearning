def validate_parenthesis(s):
    
    stack = []
    
    for i in s:
        # condition for empty stack and (
        if len(stack) == 0 or i == '(':
            stack.append(i)
            continue
        
        # condition for poping the stack
        if i == ')' and stack[-1] == '(':
            stack.pop()
            
    return len(stack) == 0

def backtrack_helper(n, s, solutions):
    if len(s) == n:
        # validate the parenthesis and then append
        if validate_parenthesis(s):
            solutions.append(s)
        
        return
    
    # add (
    backtrack_helper(n, s + '(', solutions)
    # add )
    backtrack_helper(n, s + ')', solutions)

def backtrack(n):
    solutions = []
    backtrack_helper(2*n, '', solutions)
    return solutions

print(backtrack(4))