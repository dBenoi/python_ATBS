birthday = {'Alice': 'Apr 1', 'Bob': 'Dec 2', 'Carol': 'Mar 4'}

def enterName():
    print("Enter a name: (blank to quit)")
    name = input()
    return name

def nameInBirthdays(name):
    if name in birthday:
        print(birthday[name] + ' is the birthday of ' + name)
    else:
        print('I do not have birthday information for ' + name)
        print('What is their birthday?')
        bday = input()
        birthday[name] = bday
        print('Birthday database updated')

while True:
    name = enterName()
    if name == '':
        break
    nameInBirthdays(name)
