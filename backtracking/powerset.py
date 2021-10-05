def backtrack_helper(arr, index, solutions, state):
    
    if index >= len(arr):
        solutions.append(state[:])
        return
        
    # include the index
    backtrack_helper(arr, index + 1, solutions, state + [arr[index]])
    
    # not include the index
    backtrack_helper(arr, index + 1, solutions, state)

def backtrack(arr):
    solutions = []
    backtrack_helper(arr, 0, solutions, [])
    return solutions

def print_array(arr):
    for i in arr:
        print(i)

print_array(backtrack([1,2]))