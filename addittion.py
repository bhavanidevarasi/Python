#importing just the wanted method
from Calc import add
print(add(5,2))

#import everything in module
from Calc import*
print(add(2,3))

#import with aliases
import Calc as c
print(c.add(2,3))
n = int(input())
fact =1
for i in range(1,n+1):
    fact *= i
print(fact)
count = 0
if n <=1:
    print('not prime')
else:
    for i in range(1,n+1):
        if n % i ==0:
            count +=1
    if count == 2:
        print('prime')
    else:
        print('not prime')
str = input()
reverse = str[::-1]
if str == reverse:
    print('palindrome')
else:
    print('not palindrome')
ls = [1,2,3,1,2,3,4,5,6]
unique =[]
'''
s = set(ls)
print(s)
if i in s:
    s.discard(i)
print(ls)

for i in ls:
    if i not in unique:
        unique.append(i)
print(unique)
'''
l = [unique.append(i) for i in ls if i not in unique]
print(l)
sum =0
for i in range(10):
    sum += i
print(sum)
p = 'python'
for ch in p:
    print(ch,end='')