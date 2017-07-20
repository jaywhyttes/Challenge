# The Rock Paper Scissors Lizard Spock game         #
# has two algorithms to determin a win              #
# assign the user choice to a 1-5 number scheme     #
# respective of the games titles name               #
# if the choice is 2 or 3 minus 1 or add 2          #
# if the computers choice is the outcome the        #
# user won, if the user chose 1 or 5 we add 2       #
# or 3 and check the answer for the computers       #
# choice. to get around the 5 + 2/3 being out of    #
# range, we also assign 6 and 7 to the computers    #
# choice respective of 1 and 2, that way if the     #
# user chooses 5 it will add 1 or 2 and come out    #
# 6 or 7, the exception here is 4, where we check   #
# + 1 and - 1                                       #
#####################################################

# we will start by getting the computers input from
# a random int 1-5, then check if it is 1 or 2 and
# if so add 6 or 7 to its list respectively
from random import randint
cg = [randint(1,5)]

if cg == [1]:
    cg.append(7)
if cg == [2]:
    cg.append(8)

# now we need to get the users input and apply some
# rules to it (number is between 1 and 5 and is a int)
while True:
    try:
        ug = int(input('1     -     Rock\n2     -     Spock\n3     -     Lizard\n4     -     Scissors\n5     -     Paper\n> '))
        if ug > 5 or ug < 1:
            ug = int(input('1     -     Rock\n2     -     Spock\n3     -     Lizard\n4     -     Scissors\n5     -     Paper\n> '))
        break
    except ValueError:
        ug = int(input('1     -     Rock\n2     -     Spock\n3     -     Lizard\n4     -     Scissors\n5     -     Paper\n> '))
        ug = int(input('Use Numbers.\n> '))
# now we check if the output of the user with our rules
grpA = [1,5]
grpB = [2,3]
grpC = [4]
if ug == cg:
    print('its a tie')
if ug in grpA:
    for i in cg:
        if i == ug -1 or i == ug + 2:
            print('You won')
        else:
            print('You lost')
if ug in grpB:
    for i in cg:
        if i == ug + 2 or i == ug + 3:
            print('You won')
        else:
            print('You lost')
if ug in grpC:
    for i in cg:
        if i == ug -1 or i == ug + 1:
            print('You won')
        else:
            print('You lost')
print(cg)
