import random
numberOfStreaks = 0
flipList = []
streak = 0
for experimentNumber in range(10000):
    # Code that creates a list of 100 'heads' or 'tails' values.
    if experimentNumber % 100 == 0:
        print('Experiment Number: ' + str(experimentNumber))
    for i in range(100):
        flipList.append(random.randint(0, 1))
    # Code that checks if there is a streak of 6 heads or tails in a row.
    for i in range(len(flipList)):
        if i == 0:
            pass
        elif flipList[i] == flipList[i - 1]:
            streak +=1
        else:
            streak = 0
        if streak == 6:
            numberOfStreaks += 1
    flipList = []

print('Chance of streak: %s%%' % (numberOfStreaks / 100))
