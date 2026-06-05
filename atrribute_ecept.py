class Bhavs():
    name = "bhavs"
    age = 21
obj = Bhavs()
try:
    obj.number
except AttributeError as e:
    print(e)

