import numpy as np

ROW_COUNT = 6
COLUMN_COUNT = 7


def create_board():  # This is the create board function
    # This line creates an array of zeros, 6 rows and 7 columns
    board = np.zeros((ROW_COUNT, COLUMN_COUNT))
    return board


def drop_piece():
    pass


def is_valid_location(board, col):
    # Return true if the uppermost row is equal to zero (its free)
    return board[5][col] == 0


def get_next_open_row(board, col):
    for r in range(ROW_COUNT)


board = create_board()  # Creates the board
print(board)
game_over = False
turn = 0

while not game_over:
    # Ask for player 1 input
    if turn == 0:
        col = int(input("Player 1 Make your Selection (0-6): "))
        turn += 1

    # Ask for player 2 input
    else:
        col = int(input("Player 2 Make your Selection (0-6): "))
        turn += 1
        turn = turn % 2
        # I would have subtracted 1 instead of doing modular
