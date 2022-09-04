from pathlib import Path
import os

print(Path.home())
projFolder = Path.home() / 'Documents/Projects'
folders = ['Pictures', 'Documentation', 'Notes', 'Lessons Learned']
folderName = input("What would you like to name your new Project folder: ")

for folder in folders:
    os.makedirs(projFolder/folderName/folder)

print("The folder \"" + folderName + "\" has been created!")
