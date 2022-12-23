tup = (1, 2, 342,2 ,4,"green",True)#Unchangable......
#print(type(tup), tup)
#tup=(1,)
#tup[0] = 9;----->not changable...
print(type(tup),tup)
print(len(tup))
print(tup[0])
print(tup[-1])
print(tup[2])
print(tup[3])
print(tup[4])
print(tup[5])
#print(tup[6])

if 342 in tup:
    print("Yes, 342 is present in this tuple")
tup2 = tup[1:4]
print(tup2)


