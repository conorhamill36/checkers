#Program to simulate a game of checkers.
#Initially between two simulated players making random choices (prioritising capturing opponents pieces), and then moving on to user input.
#conor.hamill@ed.ac.uk

#Importing modules
import pandas as pd
import numpy as np
import random
import time
import checkers_functions as ch_func
import checkers_decorators as ch_dec

#Decorator that simply prints the name of the function before and after executing
def func_name(func):
    def wrapper(*args, **kwargs):
        # print("\nFunction being called is {}\n".format(func.__name__))
        value = func(*args, **kwargs)
        # print("\nFunction that was called was {}\n".format(func.__name__))
        return value
    return wrapper

#Function sets up board like a traditional game of checkers
@ch_dec.dramatic_pause
@func_name
def set_up_board():
    print("Setting up board as traditional game of checkers")
    #Adding x pieces by making np array of x pieces
    x_array = np.empty([8], dtype=str)
    print(x_array)
    for i in range(len(x_array)):
        if i % 2 !=0:
            x_array[i]=('x')
        else:
            x_array[i]=('')

    x_section = np.stack((x_array, np.roll(x_array, 1), x_array))
    print('\n\n{}\n\n'.format(x_section))

    #Adding two blank rows
    blank_section = np.full([2,8], '')
    print('\n\n{}\n\n'.format(blank_section))


    #Adding o pieces
    o_array = np.empty([8], dtype=str)
    print(o_array)
    for i in range(len(o_array)):
        if i % 2 !=0:
            o_array[i]=('o')
        else:
            o_array[i]=('')

    o_section = np.stack((np.roll(o_array, 1), o_array, np.roll(o_array, 1)))
    print('\n\n{}\n\n'.format(o_section))

    #Joining sections together
    board_array = np.concatenate((x_section, blank_section, o_section), axis=0)
    print('\n\n{}\n\n'.format(board_array))

    board_df = pd.DataFrame(board_array)

    print('\n\n{}\n\n'.format(board_df))
    print("Board has been set up")
    return board_df


#Function executes a single turn for a player, returning the new board set up
@ch_dec.dramatic_pause
@func_name
def take_turn(player_name, board_df):

    #Function captures an enemy piece
    @func_name
    def capture_piece():
        return 0


    #Function moves a piece to an empty space
    @func_name
    def move_piece(board_df, x, y, piece):
        print("Moving piece from {}, {}".format(x, y))
        print("Checking spaces in front")
        #Need to include exceptions
        #For piece x, can move "below" and one square left or right
        if piece == 'x':
            try:
                board_df[x-1][y+1]
            except:
                print("Piece at the left edge of the board")
                if board_df[x+1][y+1] == '':
                    board_df[x+1][y+1] = piece
                    board_df[x][y] = ''
            else:
                try:
                    board_df[x+1][y+1]
                except:
                    print("Piece at the right edge of the board")
                    if board_df[x-1][y+1] == '':
                        board_df[x-1][y+1] = piece
                        board_df[x][y] = ''
                else:
                    print("Piece is not at either edge of the board, random choice between left and right")
                    if(random.randrange(1) == 0):
                        board_df[x-1][y+1] = piece
                        board_df[x][y] = ''
                    else:
                        board_df[x+1][y+1] = piece
                        board_df[x][y] = ''
        #For piece o, can move pieces "above" and one square left or right
        if piece == 'o':
            try:
                board_df[x-1][y-1]
            except:
                print("Piece at the left edge of the board")
                if board_df[x+1][y-1] == '':
                    board_df[x+1][y-1] = piece
                    board_df[x][y] = ''

            else:
                try:
                    board_df[x+1][y-1]
                except:
                    print("Piece at the right edge of the board")
                    if board_df[x-1][y-1] == '':
                        board_df[x-1][y-1] = piece
                        board_df[x][y] = ''
                else:
                    print("Piece is not at either edge of the board, random choice between left and right")
                    if(random.randrange(1) == 0):
                        board_df[x-1][y-1] = piece
                        board_df[x][y] = ''
                    else:
                        board_df[x+1][y-1] = piece
                        board_df[x][y] = ''
        return board_df



    print("{} is taking a turn".format(player_name))
    if (player_name.find('1') != -1):
        print('Is player 1')
        piece = 'x'
    else:
        print('Is player 2')
        piece = 'o'

    loc_array = ch_func.find_pieces(board_df, piece)
    print(type(loc_array[0][0]))

    #Check if any pieces can be eaten
    capt_array = ch_func.can_be_eaten(board_df, loc_array, piece)

    if not capt_array:
        print("No capturable pieces found")
    else:
        print("Capturable pieces found at {}".format(capt_array))
        print(board_df)

    #Check which pieces can move in to an empty space
    move_blank_array = ch_func.can_move_to_blank(board_df, loc_array, piece)

    if not move_blank_array:
        print("Not able to move to any empty spaces")
    else:
        print("Pieces at {} can move to empty spaces".format(move_blank_array))
        print(board_df)
        print("Executing function to move piece")
        #Picking piece at random
        random_piece = random.randrange(len(move_blank_array))
        print("Length of array is {}, random piece is {}".format(len(move_blank_array), random_piece))
        #time.sleep(3)
        board_df = move_piece(board_df, move_blank_array[random_piece][0], move_blank_array[random_piece][1], piece)

    print(board_df)
    print("{} has finished their turn".format(player_name))
    return board_df





def main():
    print("Hello World")



    #Setting up board
    board_df = set_up_board()


    #Players take a turn, either capturing or moving
    # player_name = 'Player 1'
    # board_df = take_turn(player_name, board_df)
    # player_name = 'Player 2'
    # board_df = take_turn(player_name, board_df)
    # player_name = 'Player 1'
    # board_df = take_turn(player_name, board_df)
    print(board_df)
    for i in range(6):
        if(i%2 == 0):
            player_name = 'Player 1'
            board_df = take_turn(player_name, board_df)
        if(i%2 == 1):
            player_name = 'Player 2'
            board_df = take_turn(player_name, board_df)
    #ch_func.print_goodbye() #testing importing functions




main()
