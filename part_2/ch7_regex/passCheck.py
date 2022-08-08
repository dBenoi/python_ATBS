# Password Strength Test
# A good password will have at least 8 characters, contain both uppercase and lowercase characters, and have at least one digit and one special character

import re

passRegex = re.compile(r'''(
    ^(?=.*[a-z].*[a-z])
    (?=.*[A-Z].*[A-Z])
    (?=.*[0-9].*[0-9])
    (?=.*[!@#$%^&*(){}.-])
    .{10,}
    $
    )''', re.VERBOSE)

# Get user password
print('''
Your password should contain at least
10 characters, 2 capitol letters, 2 lowercase 
letter, 2 numbers, and a special character.''')
print("\nWhat password would you like to check?")
password = input()

if passRegex.search(password):
    print("That's a strong password!!")
else:
    print("You need a stronger password!")