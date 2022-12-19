#List can be changed but tuple can't...
marks = [3, 5, 6, "SRHridoy", True]
# print(marks)
# print(type(marks))
# print(marks[0])
# print(marks[1])
# print(marks[2])
# print(marks[3])
# print(marks[4])
# #print(marks[5])----->Error

# colors = ["Red", "Green", "Blue", "Yellow", "Green"]
# #          [0]      [1]     [2]      [3]      [4]
# print(colors[2])
# print(colors[4])
# print(colors[0])

# colors = ["Red", "Green", "Blue", "Yellow", "Green"]
# #          [-5]    [-4]    [-3]     [-2]      [-1]
# print(colors[-1])#Negative index
# print(colors[len(marks)-3])#Simillar to the upper & This is positive index
# print(colors[-3])
# print(colors[-5])

# if "SRHridoy" in marks:
#     print("Yes")
# else:
#     print("No")

#Same thing applies for strings as well!
#if "SRH " in "SRHridoy":
#   print("Yes")

print(marks)
print(marks[1:-1])
print(marks[1:4:2])
print(marks[:])#---------->means print(marks[0:len(marks)])
