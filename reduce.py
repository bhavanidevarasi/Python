from functools import reduce
a = ['i','like','cars']
res = reduce(lambda x,y : x + " " + y,a)
print(res)
a1 =[i for i in range(5)]
red = reduce( lambda x,y:x+y,a1)
print(red)
a2 =[1,2,3,4]
def mul(m,a2):
    return m*a2
print(reduce(mul,a2))
def div(n,a2):
    return n/a2
print(reduce(div,a2))