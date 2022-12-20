l = [11, 45, 1, 2, 4, 6, 1, 1]
print(l)
# l.append(7)
# l.sort()
# print(l)
# l.sort(reverse=True)
# print(l)
# l.reverse()
# print(l)
# print(l.index(1))
#print(l.count(1))

#----->not recommended because m is a reference of l and l also changed if m changed...
# m = l
# m[0] = 0
# print(m)
# print(l)
#-------->we can copy like this:
# m = l.copy()
# m[0] = 0
# print(l)
# print(m)

# l.insert(1, 899)
# print(l)

m = [900, 1000, 1100]
k = l+m
print(k)
# l.extend(m)
print(l)




