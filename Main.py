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
            # if the input is integer when then check if the integer is between 0 and 10
            choice = int(choice)
            if 10 > choice or choice > 0:
                # so we then check if the space is free using the below function. if it is then we can pull out of
                # the loop and run = false
                if check_space_is_free(choice):
                    run = False
                else:
                    # message to handle if space is full
                    print('Space is full, please chose another move')
            else:
                # message to handle if number not in range eg '100'
                print('Please select a number within the range')
        except:
            # last catch to make sure the user input a integer and not a word or any other symbols
            print('Please type a number')


# to carry on with the human move we need to check another function first. This will be is the chosen space free?
def check_space_is_free(place):
    # checks the board and if the "place" is empty ' ' then we return space is free.
    return board[place] == ' '


def get_board_copy(board):
    # Make a copy of the board list and return it.
    board_copy = []
    for i in board:
        board_copy.append(i)
    return board_copy


# we need to create the AI move next.
def ai_move():
    # free_moves = [x for x, letter in enumerate(board) if letter == ' ' and x != 0]
    # move = 0

    # let ai letter always be O
    ai_letter = 'O'

    # for range 1-9
    for i in range(1, 10):
        # creates a copy of the board before printing to then make checks
        board_copy = get_board_copy(board)
        # checks free spaces
        if check_space_is_free(board_copy, i):
            # sets temporary letter in all free spaces
            insert_letter(board_copy, ai_letter, i)

        if check_columns_win or check_rows_win or check_cross_win(board_copy, ai_letter):
            return i
print(display_board)
