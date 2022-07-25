# Simple number guessing game
from random import randint

number = randint(1, 20)
amountOfGuesses = 0

print("I'm thinking of a number between 1 and 20. Can you guess what it is?")
guessed = int(input())
amountOfGuesses += 1

while True:
    if guessed == number:
        print("You got it! Good job!")
        break
    elif guessed < number:
        print("You're guess is too low.")
        print("Guess again.")
        guessed = int(input())
        amountOfGuesses += 1
        continue
    elif guessed > number:
        print("Your guess is too high.")
        print("Guess again.")
        guessed = int(input())
        amountOfGuesses += 1
        continue

print("You guessed the number in " + str(amountOfGuesses) + " tries!")