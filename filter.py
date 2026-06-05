def even(n):
    return n % 2 ==0
n = [i for i in range(10)]
ex = filter(even,n)
li = list(ex)
ex1 = list(filter(lambda n : n%3==0, n))
print(list(li))
print(ex1)
