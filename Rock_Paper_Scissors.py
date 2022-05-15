from os import system
import random

# Header at top of program
def top() :
    system('clear')
    print('Welcome to Rock-Paper-Scissors!\n')
    print('Enter "0" for Rock')
    print('Enter "1 for Paper')
    print('Enter "2" for Scissors')

# Code for user to enter a move
def enter() :
    play = input('\nPlease Enter a Number: ')
    while (play != '0') and (play != '1') and (play != '2') :
        top()
        print('\nError: Input is not valid')
        play = input('Please Enter a Number: ')

    top()
    print('\nPlease Enter a Number: ' + str(play))

    if play == '0' :
        print('\nYou entered: Rock')
    elif play == '1' :
        print('\nYou entered: Paper')
    elif play == '2' :
        print('\nYou entered: Scissors')
    else :
        print('ERROR')
    return play

# Code for enemy responding move
def bot_move() :
    bot = random.randint(0,2)
    print('Enemy Plays:', end = ' ')
    if bot == 0:
        print('Rock')
    elif bot == 1:
        print('Paper')
    elif bot == 2:
        print('Scissors')
    else :
        print('ERROR')
    return bot

# Returns Win, Loss, or Tie
def win_conditions(play, bot) :
    condition = 'ERROR'
    if (int(play) + 1) % 3 == bot :
        condition = 'Loss'
    elif (int(play) + 2) % 3 == bot :
        condition = 'Win'
    elif (int(play)) % 3 == bot :
        condition = 'Tie'
    return condition

# Main code
top()
play = enter()
bot = bot_move()
print('Game Outcome: ' + win_conditions(play, bot))
print('\nEnd of Game')