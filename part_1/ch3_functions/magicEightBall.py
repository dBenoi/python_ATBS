import random
from time import sleep

def getAnswer(randomNumber):
    if randomNumber == 1:
        return "It is certain"
    elif randomNumber == 2:
        return "It is decidedly so"
    elif randomNumber == 3:
        return "Yes"
    elif randomNumber == 4:
        return "Reply hazy, try again"
    elif randomNumber == 5:
        return "Ask again later"
    elif randomNumber == 6:
        return "Concentrate and ask again"
    elif randomNumber == 7:
        return "My reply is no"
    elif randomNumber == 8:
        return "Outlook not so good"
    elif randomNumber == 9:
        return "Very doubtful"

r = random.randint(1, 9)
fortune = getAnswer(r)
dots = '...'

def askEight():
    print("What is your question for the magic 8-ball?")
    input()
    for dot in dots:
        print(dot, end="", flush=True)
        sleep(.7)
    print("\n" + fortune)

askEight()