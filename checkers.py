#Program to simulate a game of checkers.
#Initially between two simulated players making random choices (prioritising capturing opponents pieces), and then moving on to user input.
#conor.hamill@ed.ac.uk

#Importing modules
import pandas as pd
import numpy as np
import random
import time
import sys
import checkers_functions as ch_func
import cbh_decorators as ch_dec


#Function sets up board like a traditional game of checkers
@ch_dec.dramatic_pause
@ch_dec.func_name
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
@ch_dec.func_name
def take_turn(player_name, board_df, passing_to_next_player_flag):

    #Function captures an enemy piece
    @ch_dec.func_name
    def capture_piece(board_df, x, y, piece):
        print("Piece from {}, {} is capturing".format(x, y))
        print("Checking spaces in front")
        #For piece x, can capture "below" and two squares left or right
        if piece == 'x':
            try:
                board_df[x-2][y+2]
            except:
                print("Piece at the left edge of the board")
                if board_df[x+1][y+1] == 'o' and board_df[x+2][y+2] == '':

                    board_df = ch_func.execute_capture(x, y, \
                    x+1, y+1, \
                    x+2, y+2, \
                    piece, board_df)

                    # print("Piece at {}, is capturing piece at {} and landing at \
                    # {}".format(board_df[x][y], board_df[x+1][y+1], board_df[x+2][y+2]))
                    # board_df[x][y] = ''
                    # board_df[x+1][y+1] = ''
                    # board_df[x+2][y+2] = piece
            else:
                try:
                    board_df[x+2][y+2]
                except:
                    print("Piece at the right edge of the board")
                    if board_df[x-1][y+1] == 'o' and board_df[x-2][y+2] == '':
                        board_df = ch_func.execute_capture(x, y, \
                        x-1, y+1, \
                        x-2, y+2, \
                        piece, board_df)

                        # print("Piece at {}, is capturing piece at {} and landing at \
                        # {}".format(board_df[x][y], board_df[x-1][y+1], board_df[x-2][y+2])
                        # board_df[x][y] = ''
                        # board_df[x-1][y+1] = ''
                        # board_df[x-2][y+2] = piece
                else:
                    print("Piece is not at either edge of the board, random choice between left and right")
                    if(random.randrange(1) == 0 and board_df[x-1][y+1] == 'o' and board_df[x-2][y+2] == ''):
                        board_df = ch_func.execute_capture(x, y, \
                        x-1, y+1, \
                        x-2, y+2, \
                        piece, board_df)


                        # print("Trying capturing to the left")
                        # board_df[x][y] = ''
                        # board_df[x-1][y+1] = ''
                        # board_df[x-2][y+2] = piece
                    else:
                        if(board_df[x+1][y+1] == 'o' and board_df[x+2][y+2] == ''):

                            board_df = ch_func.execute_capture(x, y, \
                            x+1, y+1, \
                            x+2, y+2, \
                            piece, board_df)

                            # print("Trying capturing to the right")
                            # board_df[x+2][y+2] = piece
                            # board_df[x][y] = ''
                            # board_df[x+1][y+1] = ''

        #For piece o, can capture pieces "above" and two squares left or right
        if piece == 'o':
            try:
                board_df[x-2][y-2]
            except:
                print("Piece at the left edge of the board")
                if board_df[x+1][y-1] == 'x' and board_df[x+2][y-2] == '':
                    board_df = ch_func.execute_capture(x, y, \
                    x+1, y-1, \
                    x+2, y-2, \
                    piece, board_df)

                    # board_df[x+2][y-2] = piece
                    # board_df[x][y] = board_df[x+1][y-1] = ''

            else:
                try:
                    board_df[x+2][y-2]
                except:
                    print("Piece at the right edge of the board")
                    if board_df[x-1][y-1] == 'x' and board_df[x-2][y-2] == '':
                        board_df = ch_func.execute_capture(x, y, \
                        x-1, y-1, \
                        x-2, y-2, \
                        piece, board_df)

                        # board_df[x-2][y-2] = piece
                        # board_df[x][y] = board_df[x-1][y-1] = ''
                else:
                    print("Piece is not at either edge of the board, random choice between left and right")
                    if(random.randrange(1) == 0 and board_df[x-1][y-1] == 'x' and board_df[x-2][y-2] == ''):
                        board_df = ch_func.execute_capture(x, y, \
                        x-1, y-1, \
                        x-2, y-2, \
                        piece, board_df)

                        # print("Trying to capture to the left")
                        # board_df[x-2][y-2] = piece
                        # board_df[x][y] = ''
                        # board_df[x-1][y-1] = ''
                    else:
                        print("Trying to capture to the right")
                        if(board_df[x+1][y-1] == 'x' and board_df[x+2][y-2] == ''):

                            board_df = ch_func.execute_capture(x, y, \
                            x+1, y-1, \
                            x+2, y-2, \
                            piece, board_df)

                            # board_df[x+2][y-2] = piece
                            # board_df[x][y] = ''
                            # board_df[x+1][y-1] = ''
        print("At end of function {}, board is of type {}".format("capture_piece()", type(board_df)))
        return board_df


    #Function moves a piece to an empty space
    @ch_dec.func_name
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
                    if(board_df[x][y] == piece and board_df[x-1][y+1] == ''):
                        board_df[x-1][y+1] = piece
                        board_df[x][y] = ''

                    elif(board_df[x][y] == piece and board_df[x+1][y+1] == ''):
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
                    if(board_df[x][y] == piece and board_df[x-1][y-1] == ''):
                        print("Moving up and to the left")
                        board_df[x-1][y-1] = piece
                        board_df[x][y] = ''
                    elif(board_df[x][y] == piece and board_df[x+1][y-1] == ''):
                        print("Moving up and to the right")
                        board_df[x+1][y-1] = piece
                        board_df[x][y] = ''
        print("At end of move piece function, returning board")
        return board_df



    print("{} is taking a turn".format(player_name))
    if (player_name.find('1') != -1):
        print('Is player 1')
        piece = 'x'
    else:
        print('Is player 2')
        piece = 'o'

    #Locate all the pieces for a player
    loc_array = ch_func.find_pieces(board_df, piece)
    # print(type(loc_array[0][0]))

    #Check if any pieces can be eaten
    capt_array = ch_func.can_be_eaten(board_df, loc_array, piece)

    #Check which pieces can move in to an empty space
    move_blank_array = ch_func.can_move_to_blank(board_df, loc_array, piece)

    #Player will first capture a piece over moving to a blank space
    if not capt_array:
        print("No capturable pieces found by {}".format(player_name))
        if not move_blank_array:
            print("Not able to move to any empty spaces either. Passing to next player.")
            # print(passing_to_next_player_flag)
            try:
                passing_to_next_player_flag
            except NameError:
                print("Exception to passing_to_next_player_flag being called")
                passing_to_next_player_flag = 0
                return board_df, passing_to_next_player_flag
            else:
                if(passing_to_next_player_flag == None):
                    passing_to_next_player_flag = 0
                    print("passing_to_next_player_flag found as None, setting to ".format(passing_to_next_player_flag))

                print("passing_to_next_player_flag is {}".format(passing_to_next_player_flag))
                if(passing_to_next_player_flag == 1):
                    print("No one can move! It's a draw!")
                    print(board_df)
                    sys.exit()
                passing_to_next_player_flag = 1
                print("passing_to_next_player_flag has been set to {}".format(passing_to_next_player_flag))
                return board_df, passing_to_next_player_flag

        else:
            print("Pieces at {} can move to empty spaces".format(move_blank_array))
            print(board_df)
            print("Executing function to move piece")
            #Picking piece at random
            random_piece = random.randrange(len(move_blank_array))
            print("Length of array is {}, random piece is {}".format(len(move_blank_array), random_piece))
            #time.sleep(3)
            board_df = move_piece(board_df, move_blank_array[random_piece][0], move_blank_array[random_piece][1], piece)
            passing_to_next_player_flag = 0
    else:
        print("Pieces that could capture found at {}".format(capt_array))
        print(board_df)
        print("Executing function to capture piece")
        #Picking piece at random
        random_piece = random.randrange(len(capt_array))
        board_df = capture_piece(board_df, capt_array[random_piece][0], capt_array[random_piece][1], piece)
        print("At end of {}, board is of type {}".format("take_turn", type(board_df)))
        passing_to_next_player_flag = 0

    print(board_df)
    print("{} has finished their turn\n\n\n".format(player_name))
    return board_df, passing_to_next_player_flag





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
    #Opening file to output game history for debugging
    history_file = open('history_file.txt', 'w')
    passing_to_next_player_flag = 0
    for i in range(300):
        if(i%2 == 0):
            player_name = 'Player 1'
            board_df, passing_to_next_player_flag = take_turn(player_name, board_df, passing_to_next_player_flag)
        if(i%2 == 1):
            player_name = 'Player 2'
            board_df, passing_to_next_player_flag = take_turn(player_name, board_df, passing_to_next_player_flag)


        print("Writing to history file")
        history_file.write("{} has finished turn:\n{}\n\n\n\n".format(player_name, board_df))

        #Counting number of each type of piece in the dataframe
        x_count = o_count = 0
        x_count_flag = o_count_flag = 0

        for j in range(len(board_df)):
            if board_df[j].str.contains('x', regex=False).any():
                print("Some x found in row {}".format(j))
                x_count_flag = 1

        for j in range(len(board_df)):
            if board_df[j].str.contains('o', regex=False).any():
                print("Some o found in row {}".format(j))
                print(board_df[j])
                o_count_flag = 1

        if(x_count_flag == 0):
            print("x_count_flag is zero, player 2 wins!")
            print(board_df)
            sys.exit()

        if(o_count_flag == 0):
            print("o_count_flag is zero, player 1 wins!")
            print(board_df)
            sys.exit()

        # x_count = board_df.value_counts('x')
        # o_count = board_df.value_counts('o')
        # print("x_count: {}, o_count: {}".format(x_count, o_count))
        print("End of turn number {}\nx_count_flag={}, o_count_flag={}\
        ".format(i, x_count_flag, o_count_flag))
        print(board_df)
        print("Finishing turn number {}\n\n\n\n\n".format(i))
        print("-------------------------------------\n\n\n\n\n\n\n")


    history_file.close()



main()
