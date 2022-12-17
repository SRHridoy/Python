def geometricMean(a,b):
    mean = pow((a*b),1/2)
    print(mean)

def isGreater(a,b):
    if(a>b):
        print("First number is greater")
    else:
        print("Second number is greater or equal")

def isLesser(a,b):
    pass#just ignore...

a = 9
b = 4
""" if(a>b):
    print("First number is greater")
else:
    print("Second number is greater or equal") """
isGreater(a, b)
# geomean = pow((a*b),1/2)
# print(geomean)
geometricMean(a, b)


c = 8
d = 8
""" if(c>d):
    print("First number is greater")
else:
    print("Second number is greater or equal") """
isGreater(c,d)
# geomean1 = pow((c*d),1/2)
# print(geomean1)
geometricMean(c,d)