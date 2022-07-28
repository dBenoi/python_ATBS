from sys import exit
startingPoint = True

while startingPoint == True:
    print("Please choose a number")
    try:
        inputNumber = int(input())
        # correct to positive if integer is negative
        if inputNumber < 0:
            inputNumber *= -1
        else:
            startingPoint = False
    except ValueError:
        # if inputNumber is not an integer, display error message
        print("\nThat wasn't a number, please learn to follow directions.")
        continue

def collatz(number):
    if number % 2 == 0:
        print(str(number) + " // 2")
        return number // 2
    else:
        print("3 * " + str(number) + " + 1")
        return (3 * number) + 1

def repeatTo1(number):
    while True:
        if number != 1:
            number = collatz(number)
            print(number)
        else:
            exit()

repeatTo1(inputNumber)