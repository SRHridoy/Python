names = "Sohanur,Rahman"
print(len(names))
print(names[0:5])#including 0 but not 5
print(names[:5]) 
print(names[1:5])#including 1 but not 5
#print(names[0:-3])#-->print(names[0:len(names)-3])
#print(names[0:len(names)-3])
#print(names[:len(names)-3])
print(names[-1:-3])#(14-1) = 13 : (14 - 3) = 11 doesn't make sense...
print(names[-3:-1])#(14-3) = 11 : (14 -1) = 14 make sense...

for i in names:
    print(i)

#Quick Quiz:
nm = "Harray"
print(nm[-4:-2])#--> This means len(nm) = 6...(6 - 4) = 2 : (6 - 2) = 4...so,nm[-4:-2] means nm[2:4] and  nm[2:4]--> means from 2 to (4-1) = 3...
