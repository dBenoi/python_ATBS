name = 'david'
age = 28

# regular interpolation
print('Hello, my name is %s and I am %s years old!' % (name.title(), age))

# f-string
print(f'Hello, my name is {name.title()} and next year I will be {age + 1} years old!')