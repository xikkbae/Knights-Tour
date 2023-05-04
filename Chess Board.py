import os
import time

def warnsdorffs():

    # A 2D array for the board
    y_rows = int(input("How many rows would you want the knight tour to be done on?:"))
    x_columns = int(input("How many columns would you want the knight tour to be done on?:"))
    board = []
    for i in range(y_rows):
        row = []
        for j in range(x_columns):
            row.append(0)
        board.append(row)
    def print_board(): # Function for printing the board
        for row in range(y_rows):
            for column in range(x_columns):
                print(board[row][column], end=" ")
            print("\n")

    def search_possibilities(curr_x, curr_y): # Function to find the possibilities of the knights movement
        # All the possible moves
        x_move = [2, 1, -1, -2, -2, -1, 1, 2]
        y_move = [1, 2, 2, 1, -1, -2, -2, -1]
        possibilities = []
        for i in range(8):
            new_x = curr_x + x_move[i]
            new_y = curr_y + y_move[i]
            if (0 <= new_x < x_columns) and (0 <= new_y < y_rows) and board[new_x][new_y] == 0:
                possibilities.append([new_x, new_y])
        return possibilities

    def solve():
        global start_time
        start_time = time.time()
        counter = 2
        try_solve = 0
        while try_solve == 0:
            try:
                print("Which column would you like to start the tour on?:")
                curr_x = int(input())-1
                print("Which row would you like to start the tour on?:")
                curr_y = int(input())-1
                board[curr_x][curr_y] = 1
                os.system('clear')
                try_solve = 1
            except:
                os.system('clear')
                print("There was an error, please enter an integer from 1-8")
        for i in range(x_columns * y_rows - 1):
            pos = search_possibilities(curr_x, curr_y)
            minimum = pos[0]
            for p in pos:
                if len(search_possibilities(p[0], p[1])) <= len(search_possibilities(minimum[0], minimum[1])):
                    minimum = p
            curr_x = minimum[0]
            curr_y = minimum[1]
            board[curr_x][curr_y] = counter
            counter += 1
            global end_time
            end_time = time.time()
    solve()
    print_board()
    elapsed_time = end_time - start_time
    print(elapsed_time)
warnsdorffs()
