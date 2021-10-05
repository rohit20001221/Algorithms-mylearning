"""
    9 x 9 Grid
    -> all numbers must occure excatly once in a row column and 3 x 3 Grid
"""

from itertools import product

SHAPE = 9
GRID = 3
EMPTY = '.'
DIGITS = set([str(num) for num in range(1, SHAPE + 1)])

def get_rows(board):
    for i in range(SHAPE):
        yield board[i]

def get_cols(board):
    for col in range(SHAPE):
        ret = [
            board[row][col] for row in range(SHAPE)
        ]        
        yield ret

def get_grids(board):
    for row in range(0, SHAPE, GRID):
        for col in range(0, SHAPE, GRID):
            grid = [
                board[r][c]
                for r, c in product(range(row, row + GRID), range(col, col+GRID))
            ]
            yield grid

def get_kth_row(board, k):
    return board[k]

def get_kth_col(board, k):
    return [
        board[row][k] for row in range(SHAPE)
    ]

def get_grid_at_row_col(board, row, col):
    row = row // GRID * GRID
    col = col // GRID * GRID
    
    ret = [
        board[r][c]        
        for r, c in product(range(row, row+GRID), range(col, col+GRID))
    ]
    
    return ret

def is_valid_state(board):
    # check if board is valid
    # validate all in rows
    for row in get_rows(board):
        if set(row) != DIGITS:
            return False
    
    # validate all columns
    for col in get_cols(board):
        if set(col) != DIGITS:
            return False
    
    # validate all 3 x 3 grids
    for grid in get_grids(board):
        if set(grid) != DIGITS:
            return False
    
    return True

def get_candidates(board, row, col):
    used_digits = set()
    
    # remove digits used by the same row
    used_digits.update(get_kth_row(board, row))
    # remove digits used by same colums
    used_digits.update(get_kth_col(board, col))
    # remove digits used by same 3 x 3 grid
    used_digits.update(get_grid_at_row_col(board, row, col))
    used_digits -= set([EMPTY])
    
    candidates = DIGITS - used_digits
    return candidates

def search(board):
    if is_valid_state(board):
        return True
    
    for row_idx in range(len(board)):
        for col_idx in range(len(board[row_idx])):
            elm = board[row_idx][col_idx]
            if elm == EMPTY:
                for candidate in get_candidates(board, row_idx, col_idx):
                    board[row_idx][col_idx] = candidate
                    is_solved = search(board)
                    
                    if is_solved:
                        return True
                    else:
                        board[row_idx][col_idx] = EMPTY
                
                # exhausted all candidates
                # but none solves problem
                return False
    
    return True


def solve(board):
    search(board)

if __name__ == '__main__':    
    
    board = [
        ["5","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]
    ]

    solve(board)

    for row in board:
        print(row)
