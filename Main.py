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
def check_win(pl, le):
    return ((bo[7] == le and bo[8] == le and bo[9] == le) or # across the top
    (bo[4] == le and bo[5] == le and bo[6] == le) or # across the middle
    (bo[1] == le and bo[2] == le and bo[3] == le) or # across the bottom
    (bo[7] == le and bo[4] == le and bo[1] == le) or # down the left side
    (bo[8] == le and bo[5] == le and bo[2] == le) or # down the middle
    (bo[9] == le and bo[6] == le and bo[3] == le) or # down the right side
    (bo[7] == le and bo[5] == le and bo[3] == le) or # diagonal
    (bo[9] == le and bo[5] == le and bo[1] == le)) # diagonal


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


# to carry on with the human move we need to check another function first. This will the chosen space be free?
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
    possibleMoves = [x for x, letter in enumerate(board) if letter == ' ' and x != 0] # Create a list of possible moves
    move = 0
    
    #Check for possible winning move to take or to block opponents winning move
    for let in ['O','X']:
        for i in possibleMoves:
            get_board_copy = board[:]
            get_board_copy[i] = let
            if check_win(boardCopy, let):
                move = i
                return move


    #Try to take one of the corners as this is the strongest move for the AI
    cornersOpen = []
    for i in possibleMoves:
        if i in [1,3,7,9]:
            cornersOpen.append(i)
    if len(cornersOpen) > 0:
        move = selectRandom(cornersOpen)
        return move
    
    #Try to take the center
    if 5 in possibleMoves:
        move = 5
        return move

    #Take any edge
    edgesOpen = []
    for i in possibleMoves:
        if i in [2,4,6,8]:
            edgesOpen.append(i)
    
    if len(edgesOpen) > 0:
        move = random_move(edgesOpen)

    return move

# next we create a function to allow random selection for the AI. this imports random function file as well.
def random_move(li):
    import random
    ln = len(li)
    r = random.randrange(0, ln)
    return li[r]

# checks if board is full before move to determine if move available and if game is tied
def check_board_full(board):
    #checks to see how many blank spaces there are. if there is any it returns false for board being full
    if board.count(' ') > 1:
        return False
    else:
        return True

# this is where the functions are put together to get the actual game.
def main():
    print('Lets Play Xs and Os')
    display_board(board)

    while not(check_board_full(board)):
        if not(check_win(board, 'O')):
            human_move()
            display_board(board)
        else:
            print('Sorry, the AI won this time!')
            break

        if not(check_win(board, 'X')):
            move = ai_move()
            if move == 0:
                print('Draw')
            else:
                insert_letter('O', move)
                display_board(board)
        else:
            print('You won! Good Job!')
            break

    if check_board_full(board):
        print('Draw!')


