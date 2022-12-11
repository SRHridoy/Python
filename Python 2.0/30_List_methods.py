numbers = [5, 2, 5, 1, 7, 4]
numbers.append(20)
#numbers.remove(5)
numbers.pop()
#print(numbers.index(5))
print(numbers)
print( 1 in numbers)

print(numbers.count(5))

numbers.sort()
print(numbers)

numbers.reverse()
print(numbers)

numebers2 = numbers.copy()
numbers.append(10)

print(numebers2)