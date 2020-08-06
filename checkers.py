#Program to simulate a game of checkers.
#Initially between two simulated players making random choices (prioritising capturing opponents pieces), and then moving on to user input.

#Importing modules
import pandas as pd
import numpy as np

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




def take_turn(player_name, board_df):

    def find_pieces():
        print("Finds locations of pieces being used in the game")
        return 0


    print("{} is taking a turn".format(player_name))


    if (player_name.find('1') != -1):
        print('Is player 1')
        piece = 'x'
    else:
        print('Is player 2')
        piece = 'o'

    #Check if any pieces can be eaten
    # print(board_df.get_loc(piece))
    print(board_df[board_df == piece].notnull())

    #Trying blunt force iterating method
    print(board_df.head())
    for i in range (8):
        # print(board_df[i])
        print(type(board_df[i]))
        print(board_df[i].index)
        print(board_df[i][2])
        # print(Index(board_df[i]).get_loc('x'))

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
