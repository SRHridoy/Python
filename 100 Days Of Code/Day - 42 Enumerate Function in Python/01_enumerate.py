marks = [12, 56, 32, 98, 12, 45, 1, 4]
""" ----------Here we use index variable for get index and update it---------- """

# index = 0
# for mark in marks:
#     print(mark)
#     if(index == 3):
#         print("Hridoy, Awesome!")
#     index += 1
""" ----------Instead of this we can use ENUMERATE---------- """

for index, mark in enumerate(marks):
    print(mark)
    if(index == 3):
        print("Hridoy, Awesome!")

# Loop over a list and print the index and value of each element
fruits = ['apple', 'banana', 'mango']
for index, fruit in enumerate(fruits):
    print(index, fruit)

# Loop over a list and print the index (starting at 1) and value of each element
fruits = ['apple', 'banana', 'mango']
for index, fruit in enumerate(fruits, start=1):
    print(index, fruit)