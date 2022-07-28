import time, sys
indent = 0 
indentIncreasing = True # determines if indent increases or decreases

try:
    while True:
        print(' ' * indent, end='')
        print("1111111111")
        time.sleep(.02) # sleep for 1/10th of a second

        if indentIncreasing:
            indent = indent + 1
            if indent == 6:
                indentIncreasing = False
        else:
            indent = indent - 1
            if indent == 0:
                indentIncreasing = True
except KeyboardInterrupt:
    sys.exit()