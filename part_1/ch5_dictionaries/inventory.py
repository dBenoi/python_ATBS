# inventory of items
stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def printInventory(inventory):
    print("Inventory: ")
    itemTotal = 0
    for k, v in inventory.items():
        print(k.title() + ': ' + str(v))
        itemTotal += v
    print("Total items: " + str(itemTotal))

#printInventory(stuff)

def addToInventory(inventory, addedItems):
    # your code goes here
    for item in addedItems:
        if item in inventory.keys():
            inventory[item] += 1
            
        else:
            inventory[item] = 1
    return inventory

inv = {'gold coin': 42, 'rope': 1} # initial inventory
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby'] #loot retrieved from dragon
inv = addToInventory(inv, dragonLoot)
print(inv)
printInventory(inv)