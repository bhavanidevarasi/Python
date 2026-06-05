from collections import namedtuple
Student = namedtuple('Student', ["name","age"])
S = Student("bhavs","21")
#accessing using index
print(S[0])
print(S[1])
# accessing using keyname
print(S.name)
print(S.age)
# accessing using getattr()
print(getattr(S, 'name'))
