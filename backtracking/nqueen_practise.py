"""
example : 
    .Q..
    ...Q
    Q...
    ..Q.

    repr of answer is -> [1,3,0,2] -> keep track of column for each row

example :
    ..Q.
    Q...
    ...Q
    .Q..
    
    repr of answer is -> [2,0,3,1] -> keep track of column for each row
"""


def generate_candidates(state, n):
    # if empty state i.e state = [] the return all positions
    if not state:
        return range(n)
    
    # find the next position
    position = len(state)
    candidates = set(range(n))
    
    for row, col in enumerate(state):
        candidates.discard(col)
        dist = row - position
        candidates.discard(col + dist)
        candidates.discard(col - dist)
    
    return candidates

def back_track_helper(state, solutions, n):
    # if valid state return solution
    if len(state) == n:
        solutions.append(state)
        return

    for candidate in generate_candidates(state, n):
        state.append(candidate)
        back_track_helper(state.copy(), solutions, n)
        state.pop()

def back_track(n):
    state = []
    solutions = []
    back_track_helper(state, solutions, n)
    return solutions

print(back_track(4))

    