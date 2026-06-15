from dataclasses import dataclass, field
'''
@dataclass
class Details:
    name : str
    age : int
    roll : int
s1 = Details("bhavs",21,27)
s2 = Details("bhavs",22,23)
print(s1.name==s2.name)
print(s1)
print(s2)
'''
@dataclass
class Cars:
    name : str
    year : int = field(default = 2026)
s = Cars("Ferrari")
x = Cars("Mclaren")
print(s)
print(x)

@dataclass
class Student:
    name:str
    marks : int = field(default_factory=list)
name = input("Enter the Student name : ")
n=5
marks = []
for i in range(n):
    marks += [int(input())]
s1=Student(name,marks)
s1.marks.append(90)
print(s1)
'''
s2name = input()
s2=Student(s2name)
print(s1)
print(s1.marks)
print(s2.marks)
'''