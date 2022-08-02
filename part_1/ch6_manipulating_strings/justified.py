separator = ''.rjust(40, '*')
motd = 'This is a warning!!!!\nThese systems are monitored on a\nconstant basis. Any unauthorized\naccess or use of these systems\nwill be punishable by death... or worse'

motdTest = '''
This is a warning!!!!
These systems are monitored on a
constant basis. Any unauthorized
access or use of these systems
will be punishable by death... or worse'''

motdSplit = motd.split('\n')

# iterate through motdSplit and center the text printed
def printMotdCenter():
    for line in motdSplit:
        print(line.center(40))

print(separator)
print('\n')
printMotdCenter()
print('\n')
print(separator)