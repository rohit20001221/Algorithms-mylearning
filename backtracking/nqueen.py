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

# using backtracking template for N-Queen


def is_valid_state(state, n):
    # if all queens are placed on the board then the state is valid
    if len(state) == n:
        return True

def get_candidates(state, n):
    
    # return the candidates (col indices) where queens cant attack each other
    
    # initially the state is empty so return all possible column indices for the state
    if not state:
        return range(n)
    
    # find the next position in the state to poulate
    position = len(state)
    candidates = set(range(n))
    
    # prune down candidates that place the queen into attacks
    for row, col in enumerate(state):
        # discard the col index if occupied
        candidates.discard(col)
        # discard the diagonal indices
        dist = row - position
        candidates.discard(col + dist)
        candidates.discard(col - dist)
    
    return candidates

def search(state, solutions, n):
    if is_valid_state(state, n):
        solutions.append(state.copy())
        return
    
    for candidate in get_candidates(state, n):
        state.append(candidate)
        search(state, solutions, n)
        state.pop()
    
def solve(n):
    solutions = []
    state = []
    search(state, solutions, n)
    return solutions

def print_board(state):
    board = []
    
    for col in state:
        # form the row
        row = ['.']*len(state)
        # update the column
        row[col] = 'Q'
        # append the row to board
        board.append(row)
    
    for row in board:
        print("".join(row))

results = solve(4)

for num, result in enumerate(results):
    print(f"solution: {num + 1}")
    print_board(result)
    print("")
