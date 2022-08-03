

tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose',]]

def printTable(dataForTable):
    colWidth = findLongest(dataForTable)
    #while not i > len(tableData):
    for word in range(len(dataForTable[0])):
        for item in range(len(dataForTable)):
            print(tableData[item][word].rjust(colWidth), end=' ')    
        print()
        
            


    

def findLongest(dataForTable):
    longestString = 0
    i = 0
    for item in dataForTable[i]:
        if len(item) > longestString:
            longestString = len(item)
        else:
            longestString = longestString
        i += 1
    return longestString
    
printTable(tableData)