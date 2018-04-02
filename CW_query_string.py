#https://www.codewars.com/kata/do-you-know-how-to-make-query-string/train/python

def to_query_string2(data):
    result = []
    result2 = []
    for k,v in data.items():
        for value in str(v):
            result.append([value, k])
    print(result)
    result = dict((y, x) for y, x in result)
    for k,v in result.items():
        result2.append("".join(str(v)+"="+str(k)+"&")) 
    result = "".join(result2)
#    print(result) 
    print(result[:-1]) 

def to_query_string(data):
    result = []
    result2 = []
    second = False
    for key in data: 
        value = data[key]   
        if len(str(value)) > 1:
            second = True
    if second is True:
        for k,v in data.items():
            for value in str(v):
                result.append([value, k])
        result = dict((y, x) for y, x in result)
        for k,v in result.items():
            result2.append("".join(str(v)+"="+str(k)+"&")) 
        result = "".join(result2)
        print(result[:-1])
    else: 
        for k,v in data.items():
            result2.append("".join(str(k)+"="+str(v)+"&")) 
        result = "".join(result2)
        print(result) 

#to_query_string({ "bar": 2, "foo": 1 })
#bar=2&foo=1

#to_query_string({ "a": "Z", "b": "Y", "c": "X", "d": "W", "e": "V", "f": "U", "g": "T" })
#  "a=Z&b=Y&c=X&d=W&e=V&f=U&g=T"

to_query_string({ "bar": [2, 4], "foo": [1, 3] })
# "bar=2&bar=4&foo=1&foo=3"


#henry
def to_query_string(data):
    lista = sorted(list(data.items()))
    listb = sorted([])
    for item in lista:
        for value in item:
            if type(value) is list:
                for i in range(len(value)):
                    listb.append(item[0] + "=" + str(value[i]))
        if type(item[1]) is not list:
                    listb.append(item[0] + "=" + str(item[1]))
    return "&".join(listb)

#oli
def to_query_string(data):
    query_string = []
    for key, value in sorted(data.items()):
        if isinstance(value, list):
            for i in range(len(value)):
                query_string.append(key + "=" + str(value[i]))
        else:
            query_string.append(key + "=" + str(value))
    return "&".join(query_string)