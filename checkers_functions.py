#Functions to be used with checkers.py
import checkers_decorators as ch_dec

def print_goodbye():
    print("Goodbye checkers!")
    return 0


#Function takes co-ordinates as inputs and executes a capture of an enemy piece
#@ch_dec.dramatic_pause
@ch_dec.func_name
def execute_capture(start_x, start_y, jump_x, jump_y, end_x, end_y, piece, board_df):
    print("Piece {} at {},{}, is capturing piece at {},{} and landing at \
    {},{}".format(piece, start_x, start_y, jump_x, jump_y, end_x, end_y))


    board_df[start_x][start_y] = ''
    board_df[jump_x][jump_y] = ''

    board_df[end_x][end_y] = piece
    print("After execution of capture, board looks like:\n{}\nand is of type {}".\
    format(board_df, type(board_df)))
    return board_df

#Function gets array of pieces on board
@ch_dec.func_name
@ch_dec.mute_printing
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

#Function gets array of pieces that can move to empty spaces
@ch_dec.func_name
@ch_dec.dramatic_pause
#@ch_dec.mute_printing
def can_move_to_blank(board_df, loc_array, piece):

    #Function returns boolean of whether piece can move in to blank space or not
    @ch_dec.func_name
    def can_move_to_blank_boolean(board_df, x, y, piece):


            print("Checking if piece {} at position {}, {} can move".format(piece, x, y))
            #For piece x, can move "below" and one square left or right
            if piece == 'x':
                if(y == 7):
                    print("Piece is at the bottom of the board, can't move any more")
                    move_blank_bool = 0
                    return move_blank_bool

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
                        print("board_df[x-1][y+1] is {} \nboard_df[x+1][y+1] is {} ".\
                        format(board_df[x-1][y+1], board_df[x+1][y+1]))
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
                if(y == 0):
                    print("Piece is at the top of the board, can't move any more")
                    move_blank_bool = 0
                    return move_blank_bool
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

    # can_move_to_blank_boolean(board_df, loc_array[i][0], loc_array[i][1], piece)

    if not move_blank_array:
        print("No pieces found to move in to blank spaces")
    else:
        print("Array of pieces that could move to blank places was found to be {}".format(move_blank_array))

    return move_blank_array

#Function gets array of pieces that can capture another piece
#@ch_dec.dramatic_pause

@ch_dec.mute_printing
@ch_dec.func_name
def can_be_eaten(board_df, loc_array, piece):

    #Function returns a boolean of whether can eat another piece or not
    #@ch_dec.dramatic_pause
    #@ch_dec.func_name
    def can_be_eaten_boolean(board_df, x, y, piece):
        #Testing function for (1, 4)
        # x, y, piece = 1, 4, 'x'
        #
        # board_df[x][y] = 'x'


        print("Checking if piece {} at position {}, {} can eat anything".format(piece, x, y))
        #For piece x, can eat pieces "below" and one square left or right
        #Also need to check if the space on the other side of the captured piece is empty
        if piece == 'x':
            if(y > 5):
                print("Piece is too far down the board, cannot capture anything")
                cap_bool = 0
                return cap_bool
            print("Trying to capture to left first")
            try:
                board_df[x-2][y+2]
            except:
                print("Piece near left edge of the board, so can't capture to left.\
                \nTrying to capture to the right.")
                if board_df[x+1][y+1] == 'o' and board_df[x+2][y+2] == '':
                    print("Can capture piece to the right")
                    cap_bool = 1
                else:
                    print("Nothing can be captured for piece {} at {}, {}".format(piece, x, y))
                    cap_bool = 0
            else:
                print("Now trying to capture to the right")
                try:
                    board_df[x+2][y+2]
                except:
                    print("Piece near right edge of the board, so can't capture to right.\
                    \nTrying to capture to the left.")
                    if board_df[x-1][y+1] == 'o' and board_df[x-2][y+2] == '':
                        print("Can capture piece to left")
                        cap_bool = 1
                    else:
                        print("Nothing can be captured for piece {} at {}, {}".format(piece, x, y))
                        cap_bool = 0
                else:
                    if board_df[x-1][y+1] == 'o' and board_df[x-2][y+2] == '':
                        print("Can capture piece to left")
                        cap_bool = 1

                    elif board_df[x+1][y+1] == 'o' and board_df[x+2][y+2] == '':
                        print("Can capture piece to the right")
                        cap_bool = 1
                    else:
                        print("Nothing can be captured for piece {} at {}, {}".format(piece, x, y))
                        cap_bool = 0

        #For piece o, can eat pieces "above" and one square left or right
        if piece == 'o':
            if(y < 2):
                print("Piece is too far up the board, cannot capture anything")
                cap_bool = 0
                return cap_bool

            print("Trying to capture left first")
            try: #Testing edge of board to left
                board_df[x-2][y-2]
            except:
                print("Piece at the left edge of the board so can't capture to left.\
                \nTrying to capture to the right.")
                if board_df[x+1][y-1] == 'x' and board_df[x+2][y-2] == '':
                    print("Can capture piece to the right")
                    cap_bool = 1
                else:
                    #Blocked by edge to left, nothing to capture to right
                    print("Nothing can be captured for piece {} at {}, {}".format(piece, x, y))
                    cap_bool = 0
            else:
                print("Now trying to capture to the right")
                try: #Testing edge of board to right
                    board_df[x+2][y-2]
                except:
                    print("Piece at the right edge of the board so can't capture to right.\
                    \nTrying to capture to the left.")
                    if board_df[x-1][y-1] == 'x' and board_df[x-2][y-2] == '':
                        print("Can capture piece to left")
                        cap_bool = 1
                    else:
                        #Blocked by edge to right, nothing to capture to left
                        print("Nothing can be captured for piece {} at {}, {}".format(piece, x, y))
                        cap_bool = 0

                else: #Edge not found on left or right
                    print("Edge not found on left or right")
                    if board_df[x-1][y-1] == 'x' and board_df[x-2][y-2] == '':
                        print("Can capture piece to left")
                        cap_bool = 1

                    elif board_df[x+1][y-1] == 'x' and board_df[x+2][y-2] =='':
                        print("Can capture piece to the right")
                        cap_bool = 1

                    else:
                        #In centre of board, but no available pieces to capture
                        print("Nothing can be captured for piece {} at {}, {}".format(piece, x, y))
                        cap_bool = 0

        print("Capture boolean is {}".format(cap_bool))
        return cap_bool

    print("Finding what pieces can be eaten")

    capt_array = []

    #Going through location array and testing each piece
    for i in range(len(loc_array)):

        # print(loc_array[i])
        print(loc_array[i][0], loc_array[i][1])
        print(board_df[loc_array[i][0]][loc_array[i][1]])
        if can_be_eaten_boolean(board_df, loc_array[i][0], loc_array[i][1], piece) == 1:
            print("Piece at {}, {} can capture".format(loc_array[i][0], loc_array[i][1]))
            capt_array.append(loc_array[i])
        else:
            print("Piece at {}, {} can't capture anything".format(loc_array[i][0], loc_array[i][1]))
    # can_be_eaten_boolean(board_df, loc_array[i][0], loc_array[i][1], piece)

    if not capt_array:
        print("No pieces found to capture")
    else:
        print("Array of pieces that could capture was found to be {}".format(capt_array))

    return capt_array
