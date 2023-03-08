# Dimensions of chess board
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
# Printing the board
board = ""

def print_board(dimensions,board):
    print(order_string)
    print("P P P P P P P P")
    for i in range(dimensions):
        board = board + "0 "
    for i in range(dimensions - 4):
        print(board)
    print("P P P P P P P P")
    print(order_string)

print_board(dimensions,board)


