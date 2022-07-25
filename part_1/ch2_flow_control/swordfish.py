while True:
    print("What is your name?")
    name = input()
    if name != 'David':
        continue
    
    print("\nHello David, what is the password? (Hint: It's a fish)")
    password = input()
    
    if password == 'swordfish':
            break

print("\nAccess Granted")    