import re

phoneNumRegex = re.compile(r'(\d{3})-(\d{3}-\d{4})')

mo = phoneNumRegex.findall('My number is 415-555-4242. 342-354-7893')
print(mo)

phoneNum = []
for num in mo:
    phoneNum.append(num[0] + '-' + num[1])

print(phoneNum)
print("Found the following numbers.")
for num in phoneNum:
    print("* " + num)


# areaCode, mainNumber = mo.groups()

#print('Phone number found: ' + mo.group())
#print(areaCode)
#print(mainNumber)