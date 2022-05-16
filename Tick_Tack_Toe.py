from array import array
from os import system
import random
import getch

# user inputs size of the board
def input_size() :
    system('clear')
    print('\nWelcome to Tic-Tac-Toe!')
    print('\nPlease Enter a Board Size from 3 to 9: ', end = ' ')
    size = getch.getche()
    while (size.isnumeric() == False) or (int(size) < 3) or (int(size) > 9) :
        system('clear')
        print('\nWelcome to Tic-Tac-Toe!')
        print('\nError: Board size invalid', end = '')
        print('\nPlease Enter a Board Size from 3 to 9: ', end = ' ')
        size = getch.getche()
    return size

# prints the board every time a move is made
def board(b) :
    system('clear')
    print('\nWelcome to Tic-Tac-Toe!')
    print('\nYou will be player X.  The computer will be O')
    print('You win by connecting ' + str(len(b)) + ' X\'s in a row. ', end = ' ')
    print('You lose if the computer connects ' + str(len(b)) + ' O\'s in a row')
    print('X\'s and O\'s can be connected vertically, horizontally, or diagonally\n')

    print('+', end = '')
    for x in b :
        print('-', end = '')
    print('+')

    i = 0
    for x in b :
        j = 0
        print('|', end = '')
        for y in b[i] :
            print(b[i][j], end = '')
            j = j+1
        i = i+1
        print('|')
    
    print('+', end = '')
    for x in b :
        print('-', end = '')
    print('+')

# code for user to input a move
def user(b) :
    print('\nPlease enter a location (ex: 0,0):', end = ' ')
    move = input()
    [i, j] = [move[0], move[2]]

    while (len(move) != 3) or (move[1] != ',') \
        or (i.isnumeric() == False or j.isnumeric() == False) \
        or (int(i) < 0 or int(i) > len(b)-1) \
        or (int(j) < 0 or int(j) > len(b)-1) \
        or b[int(i)][int(j)] != ' ' :

        board(b)
        print('\nERROR: Input is invalid')
        print('Please enter a location (ex: 0,0):', end = ' ')
        move = input()
        [i, j] = [move[0], move[2]]

    board(b)
    print('\nPlease enter a location (ex: 0,0): ' + str(move) + '\n')
    b[int(i)][int(j)] = 'X'
    board(b)
    return b

# random move of bot
def enemy(b) :
    i = random.randint(0,len(b)-1)
    j = random.randint(0,len(b)-1)
    while b[int(i)][int(j)] != ' ' :
        i = random.randint(0,len(b)-1)
        j = random.randint(0,len(b)-1)
    b[i][j] = 'O'
    board(b)
    return b

def check_win(b) :
    # check for row win or loss
    flag_X = True
    flag_O = True
    i = 0
    for x in b :
        j = 0
        for y in b[i] :
            if b[i][j] != 'X' :
                flag_X = False
            if b[i][j] != 'O' :
                flag_O = False
            j = j+1
        if flag_X == True :
            print('\nYou Win')
            return True
        elif flag_O == True :
            print('\nYou Lose')
            return True
        flag_X = True
        flag_O = True
        i = i+1

    # check for column win or loss
    flag_X = True
    flag_O = True
    i = 0
    for x in b :
        j = 0
        for y in b[i] :
            if b[j][i] != 'X' :
                flag_X = False
            if b[j][i] != 'O' :
                flag_O = False
            j = j+1
        if flag_X == True :
            print('\nYou Win')
            return True
        elif flag_O == True :
            print('\nYou Lose')
            return True
        flag_X = True
        flag_O = True
        i = i+1

    # check for main diagonal win or loss
    i = 0
    flag_X = True
    flag_O = True
    for x in b :
        if b[i][i] != 'X' :
            flag_X = False
        if b[i][i] != 'O' :
            flag_O = False
        i = i+1
    if flag_X == True :
        print('\nYou Win')
        return True
    elif flag_O == True :
        print('\nYou Lose')
        return True

    # check for secondary diagonal win or loss
    i = 0
    j = len(b)-1-i
    flag_X = True
    flag_O = True
    for x in b :
        if b[i][j] != 'X' :
            flag_X = False
        if b[i][j] != 'O' :
            flag_O = False
        i = i+1
        j = j-1
    if flag_X == True :
        print('\nYou Win')
        return True
    elif flag_O == True :
        print('\nYou Lose')
        return True
    
    # check for tie game
    full = True
    i = 0
    for x in b :
        j = 0
        for y in b[i] :
            if b[i][j] == ' ' :
               full = False
               break
            j = j+1
        i = i+1
    if full == True :
        print('\nTie Game')
        return True

    return False


size = input_size()
b = [ [' ']*int(size) for i in range(int(size))]
board(b)
end = False
while end == False :
    b = user(b)
    end = check_win(b)
    if(end == True) :
        break
    b = enemy(b)
    end = check_win(b)
    if(end == True) :
        break


# note: make option for 2 player as well as 1 player against computer?