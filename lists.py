from itertools import chain
'''
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

length = int(input())
lis = [] 
for i in range(length):
    lis.append(int(input()))
print(lis)
print(len(lis))
sum = 0
for i in lis:
    sum += i
print(sum)
total =0
for i in range(len(lis)):
    total += lis[i]
print(total)
lis.sort()
print(lis[-1])
print(lis[0])
evecount =0
oddcount =0
#res =[val for val in list count += 1 if val % 2 ==0]
for i in lis:
    if i % 2 ==0:
        evecount += 1
    else:
        oddcount +=1
print('The even count is :', evecount)
print('The odd count is :', oddcount)
ele = int(input("Enter the element to be found :"))
for i in lis:
    if ele == i:
        print("found")
print(lis[::-1])
li = lis
print(li)
li1 = []
for i in lis:
    li1.append(i)
print(li1)
avg = total / len(lis)
print(avg)
print(set(lis))
a =[1,2,3]
b = [1,4,5]
c= list(chain(a,b))
print(c)
cars = ['Bently','porsche','Ferrari']
print(max(cars,key=len))
longest = cars[0]
for i in cars:
    if len(i) > len(longest):
        longest = i
print(longest)
'''
#removing all occurences of elements in list
list = [10,20,40,4]
largest =list[0]
second_largest= list[0]
for i in list:
    if i > largest:
        largest = i
for i in list:
    if i > largest and i > second_largest:
        second_largest =i
print(largest)
print(second_largest)
smallest = list[0]
for i in list:
    if i < smallest:
        smallest =i
print(smallest)
list.sort()
print(list[0], "smallest")
print(list[-1], 'largest')
n = int(input("enter the nth number : "))
list.sort()
print(list[n-1])
vowels = ['a','e','i','o','u']
str = 'bhavani'
count = 0
for ch in str:
    if ch in vowels:
        count += 1
print(count)
fact =1
for i in range(1,6):
    fact *= i
print(fact)