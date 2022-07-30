# Conway's Game of Life

import random, copy, time
WIDTH = 60
HEIGHT = 20

# Create a list of lists for the cells
nextCells = []
for x in range(WIDTH):
    column = []
    for y in range(HEIGHT):
        if random.randint(0,1) == 0:
            column.append('#')
        else:
            column.append(' ') # add a dead cell
    nextCells.append(column) # list of lists

while True: # main program loop
    print('\n\n\n\n\n') # separate each step with new lines
    currentCells = copy.deepcopy(nextCells)

    # print currentCells
    for y in range(HEIGHT):
        for x in range(WIDTH):
            print(currentCells[x][y], end='') # prints # or ' ' 
        print() # print a new line at the end of the row

    # calculate the next steps cells based on current step
    for x in range(WIDTH):
        for y in range(HEIGHT):
            # get neighboring coordinates
            # % WIDTH ensures that left coord is always between 0 and WIDTH - 1
            leftCoord = (x - 1) % WIDTH
            rightCoord = (x + 1) % WIDTH
            aboveCoord = (y - 1) % HEIGHT
            belowCoord = (y + 1) % HEIGHT

            # Count number of living neighbors:
            numNeighbors = 0
            if currentCells[leftCoord][aboveCoord] == '#':
                numNeighbors += 1 # Top-left neighbor is alive.
            if currentCells[x][aboveCoord] == '#':
                numNeighbors += 1 # Top neighbor is alive.
            if currentCells[rightCoord][aboveCoord] == '#':
                numNeighbors += 1 # Top-right neighbor is alive.
            if currentCells[leftCoord][y] == '#':
                numNeighbors += 1 # Left neighbor is alive.
            if currentCells[rightCoord][y] == '#':
                numNeighbors += 1 # Right neighbor is alive.
            if currentCells[leftCoord][belowCoord] == '#':
                numNeighbors += 1 # Bottom-left neighbor is alive.
            if currentCells[x][belowCoord] == '#':
                numNeighbors += 1 # Bottom neighbor is alive.
            if currentCells[rightCoord][belowCoord] == '#':
                numNeighbors += 1 # Bottom-right neighbor is alive.

    # Set cells based on Conway's Game of Life rules
            if currentCells[x][y] == '#' and (numNeighbors == 2 or numNeighbors == 3):
                # living cells with 2 or 3 neighbors stay alive
                nextCells[x][y] = '#'
            elif currentCells[x][y] == ' ' and numNeighbors == 3:
                # Dead cells with 3 current become alive
                nextCells[x][y] = '#'
            else:
                # everything else dies
                nextCells[x][y] = ' '
    time.sleep(1)