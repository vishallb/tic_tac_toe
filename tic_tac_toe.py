# importing random library
import random

# displaying the board
def display_board(board):
    print('\n'*100)
    print('     |     |     |')
    print(' ', board[1],' |  ',board[2],'|  ', board[3],'|')
    print('-----|-----|-----|--')
    print(' ', board[4],' |  ',board[5],'|  ', board[6],'|')
    print('-----|-----|-----|--')
    print(' ', board[7],' |  ',board[8],'|  ', board[9],'|')
    print('     |     |     |')

# taking a player input as X or O and assigning it
def player_input():
    '''
    OUTPUT = (Player 1 marker, Player 2 marker)
    '''

    marker = ' '
    
    while marker not in ['X', 'O']:
        marker = input("Player 1: Choose X or O: ").upper()

        if marker not in ['X', 'O']:
            print("Sorry, it's an invalid choice.")

    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')

# Takes in the board list object, a marker (X or O) and a desired position (1-9)
def place_marker(board, marker, position):
    board[position] = marker

# Takes in a board and a mark (X or O) and checking if that mark has won
def win_check(board, mark):
    '''
    All rows, columns and two diagonals
    should have the same marker for a
    win
    '''

    return ((board[1] == mark and board[2] == mark and board[3] == mark) or #across the top row
            (board[4] == mark and board[5] == mark and board[6] == mark) or #across the middle row
            (board[7] == mark and board[8] == mark and board[9] == mark) or #across the bottom row
            (board[1] == mark and board[4] == mark and board[7] == mark) or #across the first column
            (board[2] == mark and board[5] == mark and board[8] == mark) or #across the second column
            (board[3] == mark and board[6] == mark and board[9] == mark) or #across the third column
            (board[1] == mark and board[5] == mark and board[9] == mark) or #across the diagonal
            (board[3] == mark and board[5] == mark and board[7] == mark))    #across the diagonal

# using random module to randomly decide which player goes first
def choose_first():

    flip = random.randint(0,1)

    if flip == 0:
        return 'Player 1'
    else:
        return 'Player 2'

# A function to check whether a space on the board is freely available - returns a boolean
def space_check(board, position):
    return board[position] == ' '

# To check if the board is full. True if full, False otherwise
def full_board_check(board):

    for i in range(1,10):
        if space_check(board, i):
            return False

    return True # board is full

# asks player next position and uses space_check to check if its a free position. If it is, return positon for later use
def player_choice(board):

    position = 0

    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position = int(input("Choose a position (1-9): "))

    return position

# asks the player if they want to play again and return True if they want to play again
def replay():

    choice = input("Play again? Enter Yes or No: ")

    return choice == 'Yes'

# Running the game
print("Welcome to Tic Tac Toe")

while True:

    the_board = [' '] * 10
    player1_marker, player2_marker = player_input()

    turn = choose_first()
    print(f"{turn} will go first")

    play_game = input("Ready to play? y or n? ")

    if play_game == 'y':
        game_on = True
    else:
        game_on = False

    # game play
    while game_on:
        if turn == 'Player 1':

            #show the board
            display_board(the_board)
            #choose a position
            position = player_choice(the_board)
            #place the marker on the position
            place_marker(the_board, player1_marker, position)    
            #check if they won
            if win_check(the_board, player1_marker):
                display_board(the_board)
                print("Player 1 has won")
                game_on = False
            else:
                if full_board_check(the_board):#check if there's a tie
                    display_board(the_board)
                    print("The game is a tie")
                    game_on = False
                else:
                    turn = 'Player 2'
            

        else:
            #show the board
            display_board(the_board)
            #choose a position
            position = player_choice(the_board)
            #place the marker on the position
            place_marker(the_board, player2_marker, position)    
            #check if they won
            if win_check(the_board, player2_marker):
                display_board(the_board)
                print("Player 2 has won")
                game_on = False
            else:
                if full_board_check(the_board):#check if there's a tie
                    display_board(the_board)
                    print("The game is a tie")
                    game_on = False
                else:
                    turn = 'Player 1'
