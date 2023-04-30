# Chessboard Size
dimen = 9



def isSafe(x, y, board): # A function to check if i,j are valid indexes for N*N chessboard

    if (x >= 0 and y >= 0 and x < dimen and y < dimen and board[x][y] == -1):
        return True
    return False


def printSolution(dimen, board):
    '''
        A utility function to print Chessboard matrix
    '''
    for i in range(dimen):
        for j in range(dimen):
            print(board[i][j], end=' ')
        print()


def solveKT(dimen):
    '''
        This function solves the Knight Tour problem using
        Backtracking. This function mainly uses solveKTUtil()
        to solve the problem. It returns false if no complete
        tour is possible, otherwise return true and prints the
        tour.
        Please note that there may be more than one solutions,
        this function prints one of the feasible solutions.
    '''

    # Initialization of Board matrix
    board = [[-1 for i in range(dimen)] for i in range(dimen)]

    # move_x and move_y define next move of Knight.
    # move_x is for next value of x coordinate
    # move_y is for next value of y coordinate
    move_x = [2, 1, -1, -2, -2, -1, 1, 2]
    move_y = [1, 2, 2, 1, -1, -2, -2, -1]

    # Since the Knight is initially at the first block
    board[0][0] = 0

    # Step counter for knight's position
    pos = 1

    # Checking if solution exists or not
    if (not solveKTUtil(dimen, board, 0, 0, move_x, move_y, pos)):
        print("Solution does not exist")
    else:
        printSolution(n, board)


def solveKTUtil(dimen, board, curr_x, curr_y, move_x, move_y, pos):
    '''
        A recursive utility function to solve Knight Tour
        problem
    '''

    if (pos == dimen ** 2):
        return True

    # Try all next moves from the current coordinate x, y
    for i in range(8):
        new_x = curr_x + move_x[i]
        new_y = curr_y + move_y[i]
        if (isSafe(new_x, new_y, board)):
            board[new_x][new_y] = pos
            if (solveKTUtil(dimen, board, new_x, new_y, move_x, move_y, pos + 1)):
                return True

            # Backtracking
            board[new_x][new_y] = -1
    return False

solveKT(dimen)