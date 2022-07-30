# Take a list and separate with ', ' with the last value having 'and' in front
spam = ['apples', 'bananas', 'tofu', 'cats']

for item in spam:
    if item == spam[-1]:
        print('and ' + item)
    else:
        print(item, end=', ')