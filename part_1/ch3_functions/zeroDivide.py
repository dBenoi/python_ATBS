def divide(divideBy):
    try:
        return 42 / divideBy
    except:
        print("Error: Invalid Argument")

print(divide(7))
print(divide(2))
print(divide(0))
print(divide(15))