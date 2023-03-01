# Dimensions of chess board
dimensions = 8
# Assigning each piece a letter
knight = "N"
rook = "R"
bishop = "B"
king = "K"
Queen = "Q"
Pawn = "P"

# Printing the board
board = ""
def print_board(dimensions,board):
    for i in range(dimensions):
        board = board + "0 "
    for i in range(dimensions):
        print(board)
print_board(dimensions,board)