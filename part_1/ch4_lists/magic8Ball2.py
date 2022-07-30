import random
from time import sleep

def chooseMessage():
    messages = ['It is certain',
                    'It is decidedly so',
                    'Yes definitely',
                    'Reply hazy try again',
                    'Ask again later',
                    'Concentrate and ask again',
                    'My reply is no',
                    'Outlook not so good',
                    'Very doubtful']
    print('\n' + random.choice(messages))

def askQuestion():
    print("Please ask the 8-ball a question.")
    input()

dots = '...'

def waitForAnswer():
    for dot in dots:
        print(dot, end="", flush=True)
        sleep(.7)

def eightBall():
    askQuestion()
    waitForAnswer()
    chooseMessage()

eightBall()