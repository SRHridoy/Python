dic = {
    "Hridoy" : "Programmer",
    "Nova" : "Housewife"
}

print(dic["Hridoy"])

dic1 = {
    344: "Hridoy",
    56: "Shubam",
    677: "Zakir",
    98: "Nova"
}

print(dic1[344])

""" ----------PYTHON DICTIONARIES----------- """

'''Dictionaries are ordered collection of data items. They store multiple items in a single variable. Dictionary items are key-value pairs that are separated by commas and enclosed within curly brackets {}.'''

info = {'name':'Karan', 'age':19, 'eligible':True}
print(info)


""" ----------ACCESSING SINGLE VALUES---------- """

'''Values in a dictionary can be accessed using keys. We can access dictionary values by mentioning keys either in square brackets or by using get method.'''

info = {'name':'Karan', 'age':19, 'eligible':True}
print(info['name'])#if doesn't exit throw an error...
print(info.get('eligible'))#if doesn't exit print none...

""" ----------ACCESSING MULTIPLE VALUES---------- """

'''We can print all the values in the dictionary using values() meth'''

info = {'name':'Karan', 'age':19, 'eligible':True}
print(info.values())

""" ----------ACCESSING KEYS---------- """

'''We can print all the keys in the dictionary using keys() method'''

info = {'name':'Karan', 'age':19, 'eligible':True}
print(info.keys())

#or
for key in info.keys():
    print(info[key])


for key in info.keys():
    print(f"The value corresponding to the key {key} is {info[key]}")

""" ----------ACCESSING KEY-VALUE PAIRS---------- """

'''We can print all the key-value pairs in the dictionary using items() method.'''

info = {'name':'Karan', 'age':19, 'eligible':True}
print(info.items())

for key, value in info.items():
    print(f"The value corresponding to the key {key} is {value}")