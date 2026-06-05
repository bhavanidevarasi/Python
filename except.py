try:
    name = int(input())
except ValueError as e:
    print(e)
else:
    print(name)
finally:
    print("Exception Exicuted!!!")