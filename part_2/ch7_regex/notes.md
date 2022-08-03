# Regex
---
*Regular expressions* allow you to specify a pattern of text to search for.

\d stands for 'digit' character - any single numerical from 0-9
phone number: \d\d\d-\d\d\d-\d\d\d\d

adding a 3 in braces '{3}' will match the previous pattern 3 times. 
phone number: \d{3}-\d{3}-\d{4}

## Creating Regex Objects
- all regex functions in python are in the 're' module.
- use **import re** for regex functions
- passing a string representing your regular expression to re.compile() returns a regex pattern object(rejObj)(see phone.py)
- use regObj.search() to search the string
- will return none if pattern not found
- will return Match object, which will have a group() method that will return the actual matched text.