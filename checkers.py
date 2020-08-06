#Program to simulate a game of checkers.
#Initially between two simulated players making random choices (prioritising capturing opponents pieces), and then moving on to user input.

#Importing modules
import pandas as pd
import numpy as np

#Decorator that simply prints the name of the function before and after executing
def func_name(func):
    def wrapper(*args, **kwargs):
        print("\nFunction being called is {}\n".format(func.__name__))
        value = func(*args, **kwargs)
        print("\nFunction that was called was {}\n".format(func.__name__))
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



@func_name
def take_turn(player_name, board_df):

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

    @func_name
    def can_be_eaten(board_df, loc_array, piece):

        def can_be_eaten_boolen(board_df, x, y, piece):
            #Testing function for (4, 5)
            x, y, piece = 1, 4, 'x'

            board_df[x][y] = 'x'


            print("Checking if piece {} at position {}, {} can eat anything".format(piece, x, y))
            #For piece x, can eat pieces "below" and one square left or right
            print(board_df)
            print(board_df[x-1][y+1])


            if piece == 'x':
                try:
                    board_df[x-1][y+1]
                except:
                    print("Piece at the left edge of the board")
                    if board_df[x+1][y+1] == 'o':
                        print("Can capture piece to the right")
                    else:
                        print("Nothing can be captured for piece {} at {}, {}".format(piece, x, y))
                else:
                    try:
                        board_df[x+1][y+1]
                    except:
                        print("Piece at the right edge of the board")
                        if board_df[x-1][y+1] == 'o':
                            print("Can capture piece to left")
                        else:
                            print("Nothing can be captured for piece {} at {}, {}".format(piece, x, y))
                    else:
                        if board_df[x-1][y+1] == 'o':
                            print("Can capture piece to left")

                        elif board_df[x+1][y+1] == 'o':
                            print("Can capture piece to the right")
                        else:
                            print("Nothing can be captured for piece {} at {}, {}".format(piece, x, y))

            #For piece o, can eat pieces "above" and one square left or right


            return 0

        print("Finding what pieces can be eaten")

        for i in range(len(loc_array)):

            # print(loc_array[i])
            print(loc_array[i][0], loc_array[i][1])
            print(board_df[loc_array[i][0]][loc_array[i][1]])

        can_be_eaten_boolen(board_df, loc_array[i][0], loc_array[i][1], piece)

        return 0

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
    can_be_eaten(board_df, loc_array, piece)



    # print(board_df.get_loc(piece))
    # print(board_df[board_df == piece].notnull())



    #If not, then move a piece at random

    return 0





def main():
    print("Hello World")



    #Setting up board
    board_df = set_up_board()


    #Players take a turn, either capturing or moving
    player_name = 'Player 1 '
    take_turn(player_name, board_df)


main()
