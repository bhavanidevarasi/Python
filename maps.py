def even(n):
    if n % 2==0:
        return n
n = [i for i in range(10)]
maps=map(even,n)
print(list(maps))
fruits = ["mango",'banana','apple']
m = map(lambda s:s[0],fruits)
print(list(m))