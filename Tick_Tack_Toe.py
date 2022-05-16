from os import system
import random

# prints the board every time a move is made
def board(b) :
    system('clear')
    print('\nWelcome to Tick-Tac-Toe!\n')

    print('+---+')
    i = 0
    for x in b :
        j = 0
        print('|', end = '')
        for y in b[i] :
            print(b[i][j], end = '')
            j = j+1
        i = i+1
        print('|')
    print('+---+')

# code for user to input a move
def user(b) :
    print('\nPlease enter a location (ex: 0,0):', end = ' ')
    move = input()
    [i, j] = [move[0], move[2]]

    while (len(move) != 3) or (move[1] != ',') \
        or (i.isnumeric() == False or j.isnumeric() == False) \
        or (i != '0' and i != '1' and i != '2') \
        or (j != '0' and j != '1' and j != '2') \
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
    i = random.randint(0,2)
    j = random.randint(0,2)
    while b[int(i)][int(j)] != ' ' :
        i = random.randint(0,2)
        j = random.randint(0,2)
    b[i][j] = 'O'
    board(b)
    return b

def check_win(b) :
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

    # check for row win or loss
    i = 0
    for x in b :
        if (b[i][0] == b[i][1]) and (b[i][0] == b[i][2]) and (b[i][0] != ' ') :
            if(b[i][0] == 'X') :
                print('\nYou Win')
            else :
                print('\nYou Lose')
            return True
        i = i+1

    # check for column win or loss
    j = 0
    for x in b :
        if (b[0][j] == b[1][j]) and (b[0][j] == b[2][j]) and (b[0][j] != ' ') :
            if(b[0][j] == 'X') :
                print('\nYou Win')
            else :
                print('\nYou Lose')
            return True
        j = j+1

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
    j = 2-i
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

    return False


b = [ [' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' '] ]
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