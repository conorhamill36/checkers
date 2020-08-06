#Program to simulate a game of checkers.
#Initially between two simulated players making random choices (prioritising capturing opponents pieces), and then moving on to user input.

#Importing modules
import pandas as pd
import numpy as np

#Decorator that simply prints the name of the function before and after executing
def func_name(func):
    def wrapper(*args, **kwargs):
        # print("\nFunction being called is {}\n".format(func.__name__))
        value = func(*args, **kwargs)
        # print("\nFunction that was called was {}\n".format(func.__name__))
        return value
    return wrapper


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
    return board_df


#Function executes a single turn for a player, returning the new board set up
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

        print("Checking space in front")

        if board_df[x+1][y+1] == '':
            board_df[x+1][y+1] = piece
            board_df[x][y] = ''
        else:
            board_df[x-1][y+1] = piece
            board_df[x][y] = ''

        #print(board_df)

        return board_df

    #Function gets array of pieces that can move to empty spaces
    @func_name
    def can_move_to_blank(board_df, loc_array, piece):

        @func_name
        def can_move_to_blank_boolean(board_df, x, y, piece):


                print("Checking if piece {} at position {}, {} can move".format(piece, x, y))
                #For piece x, can move "below" and one square left or right
                if piece == 'x':
                    try:
                        board_df[x-1][y+1]
                    except:
                        print("Piece at the left edge of the board")
                        if board_df[x+1][y+1] == '':
                            print("Can move to the right")
                            move_blank_bool = 1
                        else:
                            print("Nothing can be captured for piece {} at {}, {}".format(piece, x, y))
                            move_blank_bool = 0
                    else:
                        try:
                            board_df[x+1][y+1]
                        except:
                            print("Piece at the right edge of the board")
                            if board_df[x-1][y+1] == '':
                                print("Can move to left")
                                move_blank_bool = 1
                            else:
                                print("Cannot move to blank for piece {} at {}, {}".format(piece, x, y))
                                move_blank_bool = 0
                        else:
                            if board_df[x-1][y+1] == '':
                                print("Can move to left")
                                move_blank_bool = 1

                            elif board_df[x+1][y+1] == '':
                                print("Can move to the right")
                                move_blank_bool = 1
                            else:
                                print("Cannot move to blank for piece {} at {}, {}".format(piece, x, y))
                                move_blank_bool = 0

                #For piece o, can move pieces "above" and one square left or right
                if piece == 'o':
                    try:
                        board_df[x-1][y-1]
                    except:
                        print("Piece at the left edge of the board")
                        if board_df[x+1][y-1] == '':
                            print("Can move to the right")
                            move_blank_bool = 1
                        else:
                            print("Cannot move to blank for piece {} at {}, {}".format(piece, x, y))
                            move_blank_bool = 0
                    else:
                        try:
                            board_df[x+1][y-1]
                        except:
                            print("Piece at the right edge of the board")
                            if board_df[x-1][y-1] == '':
                                print("Can move to left")
                                move_blank_bool = 1
                            else:
                                print("Cannot move to blank for piece {} at {}, {}".format(piece, x, y))
                                move_blank_bool = 0
                        else:
                            if board_df[x-1][y-1] == '':
                                print("Can move to left")
                                move_blank_bool = 1

                            elif board_df[x+1][y-1] == '':
                                print("Can move to the right")
                                move_blank_bool = 1

                            else:
                                print("Cannot move to blank for piece {} at {}, {}".format(piece, x, y))
                                move_blank_bool = 0

                print("Move blank boolean is {}".format(move_blank_bool))
                return move_blank_bool


        print("Finding what pieces can move to an empty space")

        move_blank_array = []
        for i in range(len(loc_array)):

            # print(loc_array[i])
            print(loc_array[i][0], loc_array[i][1])
            print(board_df[loc_array[i][0]][loc_array[i][1]])
            if can_move_to_blank_boolean(board_df, loc_array[i][0], loc_array[i][1], piece) == 1:
                print("Piece at {}, {} can move to a blank".format(loc_array[i][0], loc_array[i][1]))
                move_blank_array.append(loc_array[i])
            else:
                print("Piece at {}, {} can't move to blank square".format(loc_array[i][0], loc_array[i][1]))
        can_move_to_blank_boolean(board_df, loc_array[i][0], loc_array[i][1], piece)

        print("Array of pieces that could move to blank places was found to be {}".format(move_blank_array))

        return move_blank_array

    #Function gets array of pieces on board
    @func_name
    def find_pieces(board_df, piece):
        print("Finds locations of pieces being used in the game")
        #Trying blunt force iterating method
        print(board_df.head())
        loc_array = []
        for i in range (8):
            for j in range(8):
                # print(board_df[i])
                # print(type(board_df[i]))
                # print(board_df[i].index)
                print(board_df[i][j])
                if(board_df[i][j] == piece):
                    print("Match at {}, {}".format(i, j))
                    loc_array.append((i, j))
                # print(Index(board_df[i]).get_loc('x'))
        print(loc_array)
        return loc_array

    #Function gets array of pieces that can capture another piece
    @func_name
    def can_be_eaten(board_df, loc_array, piece):

        @func_name
        def can_be_eaten_boolean(board_df, x, y, piece):
            #Testing function for (1, 4)
            # x, y, piece = 1, 4, 'x'
            #
            # board_df[x][y] = 'x'


            print("Checking if piece {} at position {}, {} can eat anything".format(piece, x, y))
            #For piece x, can eat pieces "below" and one square left or right
            if piece == 'x':
                try:
                    board_df[x-1][y+1]
                except:
                    print("Piece at the left edge of the board")
                    if board_df[x+1][y+1] == 'o':
                        print("Can capture piece to the right")
                        cap_bool = 1
                    else:
                        print("Nothing can be captured for piece {} at {}, {}".format(piece, x, y))
                        cap_bool = 0
                else:
                    try:
                        board_df[x+1][y+1]
                    except:
                        print("Piece at the right edge of the board")
                        if board_df[x-1][y+1] == 'o':
                            print("Can capture piece to left")
                            cap_bool = 1
                        else:
                            print("Nothing can be captured for piece {} at {}, {}".format(piece, x, y))
                            cap_bool = 0
                    else:
                        if board_df[x-1][y+1] == 'o':
                            print("Can capture piece to left")
                            cap_bool = 1

                        elif board_df[x+1][y+1] == 'o':
                            print("Can capture piece to the right")
                            cap_bool = 1
                        else:
                            print("Nothing can be captured for piece {} at {}, {}".format(piece, x, y))
                            cap_bool = 0

            #For piece o, can eat pieces "above" and one square left or right
            if piece == 'o':
                try:
                    board_df[x-1][y-1]
                except:
                    print("Piece at the left edge of the board")
                    if board_df[x+1][y-1] == 'x':
                        print("Can capture piece to the right")
                        cap_bool = 1
                    else:
                        print("Nothing can be captured for piece {} at {}, {}".format(piece, x, y))
                        cap_bool = 0
                else:
                    try:
                        board_df[x+1][y-1]
                    except:
                        print("Piece at the right edge of the board")
                        if board_df[x-1][y-1] == 'x':
                            print("Can capture piece to left")
                            cap_bool = 1
                        else:
                            print("Nothing can be captured for piece {} at {}, {}".format(piece, x, y))
                            cap_bool = 0
                    else:
                        if board_df[x-1][y-1] == 'x':
                            print("Can capture piece to left")
                            cap_bool = 1

                        elif board_df[x+1][y-1] == 'x':
                            print("Can capture piece to the right")
                            cap_bool = 1

                        else:
                            print("Nothing can be captured for piece {} at {}, {}".format(piece, x, y))
                            cap_bool = 0

            print("Capture boolean is {}".format(cap_bool))
            return cap_bool

        print("Finding what pieces can be eaten")

        capt_array = []

        for i in range(len(loc_array)):

            # print(loc_array[i])
            print(loc_array[i][0], loc_array[i][1])
            print(board_df[loc_array[i][0]][loc_array[i][1]])
            if can_be_eaten_boolean(board_df, loc_array[i][0], loc_array[i][1], piece) == 1:
                print("Piece at {}, {} can capture".format(loc_array[i][0], loc_array[i][1]))
                capt_array.append(loc_array[i])
            else:
                print("Piece at {}, {} can't capture anything".format(loc_array[i][0], loc_array[i][1]))
        can_be_eaten_boolean(board_df, loc_array[i][0], loc_array[i][1], piece)

        print("Array of pieces that could capture was found to be {}".format(capt_array))

        return capt_array

    print("{} is taking a turn".format(player_name))
    if (player_name.find('1') != -1):
        print('Is player 1')
        piece = 'x'
    else:
        print('Is player 2')
        piece = 'o'

    loc_array = find_pieces(board_df, piece)
    print(type(loc_array[0][0]))

    #Check if any pieces can be eaten
    capt_array = can_be_eaten(board_df, loc_array, piece)

    if not capt_array:
        print("No capturable pieces found")
    else:
        print("Capturable pieces found at {}".format(capt_array))
        print(board_df)

    #Check which pieces can move in to an empty space
    move_blank_array = can_move_to_blank(board_df, loc_array, piece)

    if not move_blank_array:
        print("Not able to move to any empty spaces")
    else:
        print("Pieces at {} can move to empty spaces".format(move_blank_array))
        print(board_df)
        print("Executing function to move piece")
        board_df = move_piece(board_df, move_blank_array[0][0], move_blank_array[0][1], piece)





    # print(board_df.get_loc(piece))
    # print(board_df[board_df == piece].notnull())



    #If not, then move a piece at random

    print("{} has finished their turn".format(player_name))
    return board_df





def main():
    print("Hello World")



    #Setting up board
    board_df = set_up_board()


    #Players take a turn, either capturing or moving
    player_name = 'Player 1'
    board_df = take_turn(player_name, board_df)
    player_name = 'Player 2'
    board_df = take_turn(player_name, board_df)
    player_name = 'Player 1'
    board_df = take_turn(player_name, board_df)
    print(board_df)

main()
