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
- the '?' means that the preceding pattern is optional with ZERO OR ONE instances
- the '*' means that the preceding pattern is matching 0 OR MORE - the group that precedes the star can occur any number of times in the text
- the '+' means "match ONE or MORE". Unlike the star, the preceding group must appear at least ONCE.
- braces {} will match repetition. You can specify a range by using a minimum and maximum (ex. {3, 5})

### Greedy and Non-greedy Matching
- regular expressions are *greedy* by defualt, meaning in ambiguous situations they will match the longest string possible.
- The *non-greedy*(lazy) verison of the braces, which matches the shortest string possible, has the closing brace followed by a question mark. 
- see *greed.py*

## Shorthand Character Classes

- \d: any numberic digit from 0 to 9
- \D: any character that is *not* a numberic digit from 0-9
- \w: any letter, numeric digit, or the underscore character
- \W: any character *not* a numeric digit, letter, or underscore
- \s: any space, tab, or newline
- \S: Any character that is *not* a space, tab, or newline

## Making Your Own Character Class
- use square brackets to match a set of characters when the defaults are too broad. (p. 173)
- inside square brackets, you do not need to escape the "., *, ?, or ()" characters with a backslash.
- the caret character (^) after the open bracket creates a negative character class which will match characters not in the character class.

## Wildcard
- the . (dot) character is a wildcard, which will match any character except for a newline
- Match everything with (.*)
- match newline by passing re.DOTALL as the second argument to re.compile()


## Case-Insensitive
- pass re.IGNORECASE or re.I as the second argument to re.compile() to ingore case.

## Substitute Strings with sub()
- sub() method for Regex objects will substitute new text in place of the specified patterns.
- sub() takes two arguments, the first is the string to replace all matches, and the second is for the string to search.
- sub() returns a string with the substitutions applied.

