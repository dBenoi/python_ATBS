import re

ha = 'HaHaHaHaHa'

greedyHaRegex = re.compile(r'(Ha){3,5}')
mo1 = greedyHaRegex.search(ha)
print(mo1.group())

nonGreedyHaRegex = re.compile(r'(Ha){3,5}?')
mo2 = nonGreedyHaRegex.search(ha)
mo2.group()
print(mo2.group())