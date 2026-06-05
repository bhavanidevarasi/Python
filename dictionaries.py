a = {"name":"bhavs", "age" :20}
b = dict(roll=27)
print(a)
print(b)
print(a["name"])
print(a.get("age"))
a["rollno"] = 27
a["name"]="harry"
# [print (key, val) for key, val in a.items()] -- dict comprehensions
# using for loop
print("printing both keys and values only")
for key, val in a.items():
    print(key, val)

# printing pnly keys
print("printing keys only")
for key in a:
    print(key)

# printing only vales:
print("printing values only")
for val in a.values():
    print(val)

