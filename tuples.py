from collections import deque
length = int(input())
tup=()
for i in range(length):
   tup += (int(input()),) 
print(tup)
a = ["bhavs",1,2,3]
tup1 = tuple(a)
print(tup1)
name = "bhavani"
print(tuple(name))
# tuple unpacking
likes = ("she", "likes", "bikes")
a, b, c = likes
print(a)
print(b)
print(c)
#concatination of tuples
tup2 = tup + tup1
print(tup2)
# unpacking with asterisk (*)--only one must be there else gives errors
t1 = (1,2,3,4,5,6,7)
a, *b, c = t1
print(a)
print(b)
print(c)
# reversing a tuple using reversed method
res = tuple(reversed(tup1))
print(res)
# reversing using slicing
print(tup1[::-1])
# usinf simple for loop
rev = tuple(tup1[i] for i in range(len(tup1)-1,-1,-1))
print(rev)
# using deque it provide reverse() function 
deq = deque(tup1)
deq.reverse()
deqq= tuple(deq)
print(deqq)