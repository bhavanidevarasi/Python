from vehicle import *
'''
class Name:
    def nam(self,n):
        self.n=n
        #print("Name is: ", n)
class Age:
    def age(self,ag,anyy):
        self.ag=ag
        self.anyy=anyy
       # print(anyy.n,self.ag)
obj1 = Name()
obj1.nam("bhavs")
obj2 = Age()
obj2.age(21,obj1)
#print(obj2.ag,obj2.anyy.n)
print(obj2.anyy.n,obj2.ag)

#BASIC INHERITANCE
class Details:
    def personal(self, name, roll):
        self.name=name
        self.roll=roll
class Education(Details):
    def educ(self, year, section):
        self.year=year
        self.section=section
        print(self.name, "graduates in ", self.year)
obj1 = Education()
obj1.personal("bhavs",27)
obj1.educ(2026, 1)
print(obj1.name, " is in section ", obj1.section, " her roll no is ", obj1.roll)

# INHERITANCE USING SUPER
class Details:
    def __init__(self, name):
        self.name=name
    def nam(self):
        print("Name is ", self.name)
class Education(Details):
    def __init__(self, name, rollno):
        super().__init__(name) #constructor based on mro
        self.rollno=rollno
    def info(self):
        print(self.name," roll no is ",self.rollno)
obj1 = Education("bhavs",27)
obj1.info()

class Employee:
    count = 0
    def __init__(self):
        Employee.count +=1
    def emp(self):
        for i in range(Employee.count):
                print("This is ", i + 1," object")
s1 = Employee()
s2 = Employee()
s3 = Employee()
s1.emp()

#static method
class MathOperations:
    @staticmethod
    def add(a,b):
        return a +b
    def subtract(a,b):
        return a -b
    def multiply(a,b):
        return a * b
print(MathOperations.add(4,3))
print(MathOperations.subtract(4,3))
print(MathOperations.multiply(4,3))

class Evennum:
    @staticmethod
    def even(num):
        #evennum = lambda num : num // 2 == 0
        return "even" if num % 2 ==0 else "not even"
print(Evennum.even(4))

class Animal:
    def __init__(self,name,species):
        self.name=name
        self.species=species
    def deets(self):
        print("The animal name :",self.name)
        print("The animal species :",self.species)
    def sound():
        print("it sounds wierd")
class Dog(Animal):
    def sound(self):
        print("it sounds bow bow")
d = Dog('snoopy','doberman')
Animal.sound()
d.deets()
d.sound()

class Bike(Vehicle):
    pass
bike = Bike()
bike.vehi()
bike.sounds()

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
class Student(Person):
    def __init__(self,name,age,roll_no):
        super().__init__(name,age)
        self.roll_no=roll_no
    def display(self):
        print("Name :",self.name)
        print("Age :",self.age)
        print("Roll No :",self.roll_no)
stu = Student('bhavs',21,27)
stu.display()
'''
class Some:
    def __init__(self,value):
        self.value=value
    def __add__(self,other):
        return self.value + other.value
    #this automatically creates a addition method so when we call the + this will return
s1 =Some(20)
s2 =Some(30)
print(s1.value + s2.value)
