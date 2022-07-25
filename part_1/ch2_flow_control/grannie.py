print("What is your name?")
name = input()
print("What is your age?")
age = int(input())

if name == 'Alice' and age < 100 and age > 12:
    print("Good morning Alice!")
elif age < 12:
    print("You're not allice, kiddo.")
elif age > 2000:
    print("Unlike you, Alice is not an undead, immortal vampire.")
elif age > 100:
    print("You are not Alice, grannie.")
else:
    print("Your name is not Alice.")