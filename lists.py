
# list creating using []
import itertools
a = [1,2,3]
for i in a:
    print(i, end = " ")
print(type(a))
# list ceating using
b = list((26, 27, "bhavs", 6.0))
for i , val in enumerate(b):
    print(i,val)
# creating list with repeated elements
c = [7] * 4
i = 0
while i < len(c):
    print(c[i], end = " ")
    i += 1
print()
d = ["apple", "banana", "mango"]
for i in d:
    print(i, end =" ")
print()
#using zip functions
num = [1,2,3]
val = ["one","two"]
for a , b in itertools.zip_longest(num,val, fillvalue="three"):
    print(a,b)
#taking input from user
length = int(input("Enter the length of the list:"))
list1 = [0]*length
for i in range(length):
    list1[i] = int(input())
print(list1)
#using append
list2 = []
for i in range(length):
    list2.append(int(input()))
print(list2)
# list operations 
lis = [1, 2, 3, 4, 5, 6, 'bhavs', 'indigo', 'bikes']
lis.append("kim")
print(lis)
lis.insert(6,"astha")
print(lis)
lis.extend([7,8,9])
print(lis)
lis[3]= 40
lis.remove(2)
lis.pop()
print(lis)
del lis[0]
print(lis)
#using slicing
print(lis[:4])
print(lis[0::2])