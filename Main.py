"""
Tic Tac Toe by Leon Hunter
"""

# Firstly we need to create a board. I found a handy line from google that uses a list to create options of 1-9
# rather than 0-8

board = [' ' for x in range(10)]


# Secondly we need to create the board to play from, keeping this quite simple so its easier to work with going forward.

def display_board(board):
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('-----------')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('-----------')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])


# next I need to create a function to input a letter in the board.
def insert_letter(letter, place):
    board[place] = letter


# so board position must equal to where the letter goes

# before any move we need to check if there is a win condition so I need to create some checks for each possible win
def check_columns_win(pl, le):
    return pl[1] == le and pl[4] == le and pl[7] == le or pl[2] == le and pl[5] == le and pl[8] == le \
           or pl[3] == le and pl[6] == le and pl[9] == le


# checks each row for a win pl means place and le means letter
def check_rows_win(pl, le):
    return pl[1] == le and pl[2] == le and pl[3] == le or pl[4] == le and pl[5] == le and pl[6] == le \
           or pl[7] == le and pl[8] == le and pl[9] == le


# checks each diagonal for win pl means place and le means letter
def check_cross_win(pl, le):
    return pl[1] == le and pl[5] == le and pl[9] == le or pl[7] == le and pl[5] == le and pl[3] == le


# next we need to take user input and create a move. Human player will always be Xs for this game.
def human_move():
    # so while true the loop will run for the player.
    run = True
    while run:
        # we then get input from user stored in a variable called choice.
        choice = input("Please select a move using 1-9 (1 being top left)")
        # we need to make sure that the choice is correct and matches.
        try:
            #if the input is integer when then check if the integer is between 0 and 10
            choice = int(choice)
            if 10 > choice or choice > 0:




# to carry on with the human move we need to check another function first. This will be is the chosen space free?

def check_space_is_free(place):
