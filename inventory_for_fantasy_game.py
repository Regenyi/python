inv = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}  

def display_inventory(inventory):
    for items, values in inventory.items():
        print(items, values)  
    print("Inventory: \n        Total number of items: ") 

display_inventory(inv) 