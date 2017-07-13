# play 2 games: higher or lower and heads or tails
import sys
import random

def title():
    #prints title screen with three options
    print('Play which ever you\'d like\n1 - Heads or Tails\n2 - Higher or Lower\n3 - Quit')
    while True:
        #gets user input and decides what to do
        userChoice = str(raw_input('>'))
        if '1' in userChoice:
            headsOrTails()
            break
        if '2' in userChoice:
            higherOrLower()
            break
        if '3' in userChoice:
            sys.exit()
    

def higherOrLower():
    #set up game
    print('Playing Higher or Lower')
    attempts = 10
    maxNum = raw_input('Enter a max number\n>')
    print('Guess the number between 0 and ' + maxNum)
    randomNum = int(random.randint(0,int(maxNum)))
    #a loop that will allow the user to guess 10 times and asks if
    #the user would like to play again, re-runs function if so or runs title function otherwise
    while attempts > 0:
        userGuess = int(raw_input('>'))
        if userGuess == randomNum:
            while True:
                win = str(raw_input('Congratulations - Play again? Y/N\n>').upper())
                if win == 'Y':
                    higherOrLower()
                    break
                if win == 'N':
                    title()
                    break
        if userGuess < randomNum:
            attempts -= 1
            print('higher - chances left (' + str(attempts) + ')')            
        if userGuess > randomNum:
            attempts -= 1
            print('lower - chances left (' + str(attempts) + ')')
            
def headsTailsUser():
    #gets user input and maps possible inputs to a list to use
    userGuess = str(raw_input('Heads or Tails?\n>').upper())
    heads = ['HEADS', 'HEAD', 'H']
    tails = ['TAILS', 'TAIL', 'T']
    #if input does not match provided list ask the user to try again, re-runs this function
    while True:
        if userGuess in heads:
            return 0
        elif userGuess in tails:
            return 1
        if userGuess not in heads and userGuess not in tails:
            print( 'Check response - type heads or tails' )
            headsTailsUser()
            break

def headsOrTails():
    #set up game
    print('Playing Heads or Tails')

    flip = random.randint(0, 1)
    flipOutput = ''
    if flip == 0:
        flipOutput = 'heads'
    else:
        flipOutput = 'tails'
    userGuess = headsTailsUser()
    #condition if user guesses the flip, asks if user would like to play again
    #re-runs function if so or runs title function
    while True:
        if userGuess == flip:
            win = str(raw_input('Congratulations - Play again? Y/N\n>').upper())
            if win == 'Y':
                headsOrTails()
                break
            if win == 'N':
                title()
                break
        else:#notifies the user of the result if the user doesn't guess correctly
            lose = str(raw_input('Sorry, it was {}.\nBetter luck next time - Play again? Y/N\n>'.format(flipOutput)).upper())
            if lose == 'Y':
                headsOrTails()
                break
            if lose == 'N':
                title()
                break
title()
