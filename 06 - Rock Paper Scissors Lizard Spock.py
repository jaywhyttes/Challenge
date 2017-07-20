
import random

def objStr(num):
    if num == 0:
        result = "rock"
    elif num == 1:
        result = "Spock"
    elif num == 2:
        result = "paper"
    elif num == 3:
        result = "lizard"
    elif num == 4:
        result = "scissors"
    return result


def objInt(name):


    if name == "rock":
        result = 0
    elif name == "Spock":
        result = 1
    elif name == "paper":
        result = 2
    elif name == "lizard":
        result = 3
    elif name == "scissors":
        result = 4
    return result


def game():
    accInp = ['rock','spock','paper','lizard','scissors']
    ug = input('Choose one...\n\nRock\nSpock\nPaper\nLizard\nScissors\n> ')
    while True:
        if ug in accInp or ug.capitalize() in accInp:
            ug = ug.lower()
            break
        else:
            ug = input('Incorrect input...')
        
    obj = objInt(ug)
    cg = random.randint(1, 5)

    print ("Player chooses", objStr(obj))
    print ("Computer chooses", objStr(cg))

    if (cg + 1) % 5 == ug or (cg + 2) % 5 == ug:
        print ("Player wins!")
    elif cg == ug:
        print ("Player and computer tie!")
    else:
        print ("Computer wins!")
    print ("")
game()
#game("rock")
#game("Spock")
#game("paper")
#game("lizard")
#game("scissors")
