from os import system
import random

def top() :
    system('clear')
    print('Welcome to Rock-Paper-Scissors!\n')
    print('Enter "0" for Rock')
    print('Enter "1 for Paper')
    print('Enter "2" for Scissors')

def enter() :
    play = input('\nPlease Enter a Number: ')
    while (play != '0') and (play != '1') and (play != '2') :
        top()
        print('\nError: Input "' + str(play) + '" is not valid')
        play = input('Please Enter a Number: ')

    top()
    print('\nPlease Enter a Number: ' + str(play))

    if play == '0' :
        print('\nYou entered: Rock')
    elif play == '1' :
        print('\nYou entered: Paper')
    else :
        print('\nYou entered: Scissors')
    return play

def bot_move() :
    bot = random.randint(0,2)
    print('Enemy Plays:', end = ' ')
    if bot == 0:
        print('Rock')
    elif bot == 1:
        print('Paper')
    elif bot == 2:
        print('Scissors')
    return bot

def win_conditions(play, bot) :
    print('Game Outcome:', end = ' ')
    if int(play) == 0 :         # user inputs rock
        if bot == 0 :
            print('Tie')
        elif bot == 1 :
            print('Loss')
        elif bot == 2 :
            print('Win')
    elif int(play) == 1 :       # user inputs paper
        if bot == 0 :
            print('Win')
        elif bot == 1 :
            print('Tie')
        elif bot == 2 :
            print('Loss')
    elif int(play) == 2 :       # user inputs scissors
        if bot == 0 :
            print('Loss')
        elif bot == 1 :
            print('Win')
        elif bot == 2 :
            print('Tie')


top()
play = enter()
bot = bot_move()
win_conditions(play, bot)
print('\nEnd of Game')