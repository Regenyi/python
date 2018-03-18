person = {}

properties = [
    ("age", int),
    ("height", float),
    ("weight", float),
]

for property, p_type in properties:
    valid_value = 0

    while valid_value is 0:
        try:
            value = input("Please enter your {}: ".format(property))
            valid_value = p_type(value)
        except ValueError:
            print("Could not convert {} '{}' to type {}. Please try again.".format(property, value, p_type.__name__))

    person[property] = valid_value

# még azt beletenni, hogy jön egy label
# a labelt beazonositani, és hogy az benne van-e az elfogadható listába (pl 1-30)

    