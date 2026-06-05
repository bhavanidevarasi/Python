"""
N , K = map(int,  input().split())
count =0
for i in range(N):
    X = int(input())
    if X % K==0:
        count +=1
print("Count is: ", count)
"""
"""
p1, p2, p3, p4 = map(int, input().split())
count =0
s = [p1,p2,p3,p4]
for i in s:
    if i >= 10:
        count +=1
print(count)
"""
T = int(input())
for i in range(T):
    X, Y, Z = map(int, input().split())
    capacity = 10 * X
    passengers = min(Y, capacity)
    print(passengers * Z)