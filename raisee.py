import math
def name():
    n = input()
    if n.isdigit():
        raise ValueError(" n can not be an integer")
    print(n)
try:
    name()
except ValueError as e:
    print(e)
try:
    num = math.exp(1000)
except OverflowError as e:
    print(e)
try:
    age = 12
    assert age>18, "age must be greater than 18"
except AssertionError as e:
    print(e)
try:
    n = 10
    x = n/0
except ZeroDivisionError as e:
    print(e)