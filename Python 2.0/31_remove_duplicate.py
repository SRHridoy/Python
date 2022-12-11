from difflib import unified_diff


numbers = [2, 2, 4, 6, 3, 4, 6, 1]
uniqes = []
for number in numbers:
    if number not in uniqes:
        uniqes.append(number)
print(uniqes)