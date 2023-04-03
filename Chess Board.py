'''# Dimensions of chess board
dimensions = 8
# Assigning each piece a letter
knight = "N"
rook = "R"
bishop = "B"
king = "K"
Queen = "Q"
Pawn = "P"
order = ["R", "B", "N", "Q", "K", "N", "B", "R"]
order_string = "R B N Q K N B R"
'''

# A 2D array for the board
board = [[0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0]]

def print_board(): # Function for printing the board
    for row in range(8):
        for column in range(8):
            print(board[row][column], end=" ")
        print("\n")

# X, Y positions
x_pos = 0
y_pos = 0
possibilities = []
def search_possibilities(x_pos,y_pos): # Checking if moves are possible
    # Possible moves for the knight
    x_move = [2, 1, -1, -2, -2, -1, 1, 2]
    y_move = [1, 2, 2, 1, -1, -2, -2, -1]
    possibilities = []

    for i in range(8):
        if x_move[i]+x_pos>=0 and x_move[i]+x_pos<=7 and y_move[i]+y_pos>= 0 and y_move[i]+y_pos<=7:
            possibilities.append([x_move[i]+x_pos,y_move[i]+y_pos])
    return possibilities

def solver():
    pos = search_possibilities(0, 0)









'''board = ""
coord_x = 0
coord_y = 0
x_move = [2, 1, -1, -2, -2, -1, 1, 2]
y_move = [1, 2, 2, 1, -1, -2, -2, -1]
board = [[-1 for i in range(dimensions)]for i in range(dimensions)]
board[0][0] = 0
step=1
'''








'''def solveKTUtil(dimensions, board, curr_x, curr_y, x_move, y_move, step):
    
        A recursive utility function to solve Knight Tour
        problem

    if (step == dimensions ** 2):
        return True

    # Try all next moves from the current coordinate x, y
    for i in range(8):
        new_x = curr_x + move_x[i]
        new_y = curr_y + move_y[i]
        if (isSafe(new_x, new_y, board)):
            board[new_x][new_y] = pos
            if (solveKTUtil(n, board, new_x, new_y, move_x, move_y, pos + 1)):
                return True

            # Backtracking
            board[new_x][new_y] = -1
    return False
'''



# Printing the board
'''def print_board(dimensions,board):
    print(order_string)
    print("P P P P P P P P")
    for i in range(dimensions):
        board = board + "0 "
    for i in range(dimensions - 4):
        print(board)
    print("P P P P P P P P")
    print(order_string)
print_board(dimensions,board)'''


