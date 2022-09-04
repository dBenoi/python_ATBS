from pathlib import Path
import os

print(Path('spam', 'bacon', 'eggs'))
print(str(Path('spam', 'bacon', 'eggs')))

print(Path('spam') / 'bacon' / 'eggs')
print(Path('spam') / Path('bacon/eggs'))

# Find the home directory

