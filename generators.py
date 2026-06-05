def nums(m):
    for i in range(m):
        yield i
for i in nums(10):
    print(i, end=" ")
