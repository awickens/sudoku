# Main file which implements the backtracking algorithm in python

def get_board():
    ''' 
        Returns the board to solve for as a list of lists.
        Any unfilled spaces are automatically filled as a zero in the board.
    '''
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

    return board

def valid(board, num, pos):
    ''' 
        Returns true if the input (num) is valid, false otherwise
    '''

    # Check row
    for i in range(len(board[0])):
        if board[pos[0]][i] == num and pos[1] != i:
            return False

    # Check column
    for i in range(len(board)):
        if board[i][pos[1]] == num and pos[0] != i:
            return False
    
    # Checking the box
    xbox = pos[1] // 3
    ybox = pos[0] // 3

    for i in range(ybox*3, ybox*3 + 3):
        for j in range(xbox*3, xbox*3 + 3):
            if board[i][j] == num and (i,j) != pos:
                return False

    return True

def print_board(board):
    '''
        Prints the given board in the terminal.

        Inputs
        ------------------
        board : list
            list of lists denoting the sudoku board to solve for.

        Returns
        -------------------
            Printed board in the terminal.
    '''
    
    # Iterate over the length of the board in the form [row, col]
    for i in range(len(board)):
        # If we hit a area divisible by 3 then we can print a row divider to better separate the board
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - -")

        # Now do the same for the columns
        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print("|", end="")

            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")

def find_empty(board):
    '''
    Finds an empty position in the board.
    '''
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i,j) #(row, column)

    return None

def solve(board):
    '''
        Solves the sudoku board recursively.
    '''
    find = find_empty(board)

    if not find:
        return True
    else:
        row,col = find
    
    for i in range(1,10):
        if valid(board, i, (row,col)):
            board[row][col] = i

            if solve(board):
                return True
            
            board[row][col] = 0

    return False


if __name__ == "__main__":
    board = get_board();
    print_board(board)
    print("-----------------")
    solve(board)
    print_board(board)



