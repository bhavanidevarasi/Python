from itertools import chain
m = [[1,2,3],[4,5,6],['bhavs','indigo','bikes']]
# using for loop
for i in m:
    for j in i:
        print(j, end = " ")
print()
# ussing row-by-row
for row in m:
    print(row)
print()
"""
# using range
for i in range(len(m)):
    for j in range(len(m[i])):
        print(m[i],m[j], end = " ")
        print()
"""
li = list(chain(*m))
print(li)
print(m[0])