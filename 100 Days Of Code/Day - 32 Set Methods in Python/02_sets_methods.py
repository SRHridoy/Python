""" ----------ISDISJOINT()---------- """

'''The isdisjoint() method checks if items of given set are present in another set. This method returns False if items are present, else it returns True.

'''
cities = {"Tokyo2", "Madrid1", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
print(cities.isdisjoint(cities2))

""" -----------ISSUPERSET()----------"""

'''The issuperset() method checks if all the items of a particular set are present in the original set. It returns True if all the items are present, else it returns False.'''

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Seoul", "Kabul"}
print(cities.issuperset(cities2))
cities3 = {"Tokyo", "Madrid","Delhi"}
print(cities.issuperset(cities3))
print(cities3.issubset(cities))

""" ----------ADD()---------- """

'''If you want to add a single item to the set use the add() method.'''

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities.add("Helsinki")
print(cities)

"""---------UPDATE()----------"""

'''If you want to add more than one item, simply create another set or any other iterable object(list, tuple, dictionary), and use the update() method to add it into the existing set.
'''

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Helsinki", "Warsaw", "Seoul"}
cities.update(cities2)
print(cities)

""" ----------REMOVE()/DISCARD()---------- """
'''We can use remove() and discard() methods to remove items form list.'''

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities.remove("Tokyo")
print(cities)

'''The main difference between remove and discard is that, if we try to delete an item which is not present in set, then remove() raises an error, whereas discard() does not raise any error.'''

# cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# cities.remove("Seoul")
# print(cities)

""" ---------POP()---------- """

'''This method removes the last item of the set but the catch is that we don’t know which item gets popped as sets are unordered. However, you can access the popped item if you assign the pop() method to a variable.'''

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
item = cities.pop()
print(cities)
print(item)

""" ----------DEL---------- """

'''del is not a method, rather it is a keyword which deletes the set entire'''

# cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# del cities
# print(cities)
'''NameError: name 'cities' is not defined We get an error because our entire set has been deleted and there is no variable called cities which contains a set.
'''

""" ----------CLEAR()---------- """
'''This method clears all items in the set and prints an empty set.'''
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities.clear()
print(cities)

""" ----------CHECK IF ITEM EXITS---------- """

'''You can also check if an item exists in the set or not.'''

info = {"Carla", 19, False, 5.9}
if "Carla" in info:
    print("Carla is present.")
else:
    print("Carla is absent.")