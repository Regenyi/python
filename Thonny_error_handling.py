types = {"amount": int}
##    {"name", str),
##    ("year", int),
##    ("month", int),
##    ("day", int),

##    ("type", bool),
##    ("manufacturer", str),
##    ("email", str),
##    ("game_title", str),


def get_inputs2(list_labels, title):
    print(title)
    inputs = []
    for label in list_labels: # label beazonositás 7
        print(types[label])
        not_valid = None
        while not_valid is None:
            query = input(label)
 
            #for label, p_type in types:
            try:
                valid_value = types[label](query) # itt azt a p_type-t vedd, ami a labelhez tartozik
            except ValueError as ve:
                print(ve)
            else:      
                not_valid = valid_value
    inputs.append(valid_value)
    return inputs

print(get_inputs2(["amount"], "Please, add the id: "))