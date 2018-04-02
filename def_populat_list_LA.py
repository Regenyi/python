def populate_list(inventory):
    # creating the empty list
    output_list = []
    # iterating through the 'inventory'
    for item, amount in inventory.items():
        # setting the index to the value of the key-value pair (the 'amount')
        i = amount
        # iterate until the index is higher than 0
        while i > 0:
            # append to the list
            output_list.append(item)
            # decrease the index
            i -= 1
    # sort the list
    output_list = sorted(output_list)
    print(output_list)
    # return the list    
    return output_list

inv2 = {'dagger': 3, 'gold coin': 1, "battleaxe": 2} 
populate_list(inv2)
#export_inventory(inv2)