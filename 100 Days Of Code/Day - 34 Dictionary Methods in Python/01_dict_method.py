""" ----------DICTIONARY METHODS---------- """


""" ----------UPDATE()---------- """

'''The update() method updates the value of the key provided to it if the item already exists in the dictionary, else it creates a new key-value pair.'''
ep1 = {122: 45, 123: 89, 567: 69,670: 69}
ep2 = {222: 67, 566: 90}

ep1.update(ep2)
print(ep1)

info = {'name':'Karan', 'age':19, 'eligible':True}
print(info)
info.update({'age':20})
info.update({'DOB':2001})
print(info)

""" ----------REMOVING ITEMS FROM DICTIONARY---------- """


""" ----------CLEAR()---------- """

'''The clear() method removes all the items from the list.'''
info = {'name':'Karan', 'age':19, 'eligible':True}
info.clear()
print(info)


""" ----------EMPTY DICTIONARY---------- """
empt = {}
print(empt)


""" ----------POP()---------- """

'''The pop() method removes the key-value pair whose key is passed as a parameter.'''
info = {'name':'Karan', 'age':19, 'eligible':True}
info.pop('eligible')
print(info)

""" ----------POPITEM()---------- """

'''The popitem() method removes the last key-value pair from the dictionary.'''
info = {'name':'Karan', 'age':19, 'eligible':True, 'DOB':2003}
info.popitem()
print(info)

""" ----------DEL---------- """

'''we can also use the del keyword to remove a dictionary item.'''
info = {'name':'Karan', 'age':19, 'eligible':True, 'DOB':2003}
del info['age']
print(info)

'''If key is not provided, then the del keyword will delete the dictionary entirely.'''
info = {'name':'Karan', 'age':19, 'eligible':True, 'DOB':2003}
del info
print(info)




