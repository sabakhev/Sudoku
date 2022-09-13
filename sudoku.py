# Returns the row and column of a free square on a board
def get_free_square(puzzle):
    for i in range(9):
        for j in range(9):
            if puzzle[i][j] == 0:
                return i, j
    return None, None

# Checks if this guess is valid
def is_valid(guess, puzzle, row, col):
    # First check horizontally and vertically
    for i in range(9):
        if puzzle[row][i] == guess or puzzle[i][col] == guess:
            return False
    
    # Now check the 3x3 square
    cube_row = row // 3
    cube_col = col // 3

    for i in range (cube_row*3, cube_row*3 + 3):
        for j in range (cube_col*3, cube_col*3 + 3): 
            if puzzle[i][j] == guess :
                return False
    # If no False's were returned, it is valid and return true
    return True

def solve_sud(puzzle):

    #First look for free square
    row, col = get_free_square(puzzle)
    
    #base case: No free squares left
    if row == None : return True

    # Checks all of the possible numbers. If we couldn't solve with one number, reset the board and try with
    # another one. If none work, return False. 
    for guess in range (1, 10):
        if is_valid(guess, puzzle, row, col):
            puzzle[row][col] = guess
            if solve_sud(puzzle):
                return True
            puzzle[row][col] = 0
    return False

# Example of a board and it's solution.
board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]
solve_sud(board)
print(board)
