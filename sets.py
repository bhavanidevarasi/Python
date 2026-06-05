s = {"she","likes","bikes"}
print(s)
print(type(s))

# list to set
a = set([1,2,3,4])
print(a)

# frozensets
b = frozenset([5,6,7,8])
print(b)
#union of sets
u=a.union(b)
print(u)
#intersection 
i = a.intersection(b)
print(i)
#difference
d = a.difference(b)
print(d)
u.clear()
print(u)