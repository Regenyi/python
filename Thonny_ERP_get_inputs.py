years = ["2014", "2015", "2016", "2017", "2018"]

def get_inputs(list_labels, title): 
    inputs = []
    print(title)
    for label in list_labels:
        while True:
            inputs.append(input(label))
            if label == "year ":
                if inputs[0] not in years:  # a kurva nagy probléma, hogy itt még minden sztring lesz 
                    print("wrong type!")
                else:
                    break
            elif label == "Please enter a number: ":
                break
            else:
                print("wrong format")
    return inputs

get_inputs(["year "], "For which year?: ")