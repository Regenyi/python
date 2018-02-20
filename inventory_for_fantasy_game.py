inv = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}  
dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

def display_inventory(inventory):
    for items, values in inventory.items():
        print(items, values)  
    print("Inventory: \n        Total number of items: ") 

#display_inventory(inv) 

def sum_array(arr):
    if arr != 0:
        return(sum(arr) - min(arr) - max(arr)) 
    else:
        return None 

print(sum_array([ 3, 5, 7, 8, 2]))