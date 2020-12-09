"""
Tic Tac Toe by Leon Hunter
"""

# Firstly we need to create a board. I found a handy line from google that uses a list to create options of 1-9
# rather than 0-8

board = [' ' for x in range(10)]


# Secondly we need to create the board to play from, keeping this quite simple so its easier to work with going forward.

def display_board(board):
    print(board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('---------------')
    print(board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('---------------')
    print(board[7] + ' | ' + board[8] + ' | ' + board[9])
