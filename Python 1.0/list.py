marks = [95, 98, 97, "Nova"]
print(marks[-1])
print(marks[3])
print(marks[1:3])

for score in marks:
    print(score)

marks.append("Hridoy")
print(marks)

marks.insert(0,"Avonyodirh")
print(marks)

print("Nova" in marks)

print(len(marks))

i = 0
while i < len(marks):
    print(marks[i])
    i = i + 1
    
marks.clear()
print(marks)


