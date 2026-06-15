
import argparse
'''
class Car:
    def __init__(self,speed,units):
        self.speed=speed
        self.units=units
    def __str__(self):
        return f"Car with the maximum speed of {self.speed} {self.units}"
class Boat:
    def __init__(self,speedb):
        self.speed=speedb
    def __str__(self):
        return f"Boat with the maximum speed of {self.speed} knots"
parser=argparse.ArgumentParser()
parser.add_argument("speed",type=int)
parser.add_argument("units")
parser.add_argument("speedb",type=int)
args=parser.parse_args()
c = Car(args.speed,args.units)
print(c)
b = Boat(args.speedb)
print(b)

class Student:
    def Details(self):
        self.name= 'name'
        self.age= self.age
        self.roll = self.roll
        return self.name,self.age,self.roll
c = Student()
c.name="bhavs"
c.age=21
c.roll=27
print(c.name,c.age,c.roll)
print(c.Details())
class Car:
    brand : str
    model : int
    #def __init__(self,brand,model):
        #self.brand=brand
        #self.model=model
    def display(self):
        print("The Car name is :",self.brand)
        print("The car model is :",self.model)
#s = Car("Buggati",2026)
s = Car()
s.brand='buggati'
s.model=2026
s.display()

class Rectangle:
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def area(self):
        return self.length*self.width
r = Rectangle(12,3)
print(r.area())
class Book:
    def __init__(self,title,author,price):
        self.title=title
        self.author=author
        self.price=price
    def details(self):
        print("The book title is ",self.title)
        print("The author of the book is ",self.author)
        print("The price of the book is ",self.price)
parser=argparse.ArgumentParser()
parser.add_argument('title',type=str)
parser.add_argument('author',type=str)
parser.add_argument('price',type=int)
args=parser.parse_args()
b = Book(args.title,args.author,args.price)
print(b.details())

class Laptop:
    brand = input()
    ram = int(input())
    price = int(input())
    def Deets(self):
        print("The laptop brand :",self.brand)
        print("RAM of the laptop :",self.ram)
        print("The price of the laptop :",self.price)
l = Laptop()
l.Deets()

class BankAccount:
    def __init__(self,balance):
        self.balance=balance
    def deposit(self,deposited):
        self.deposited=deposited
        print("The amount deposited :",self.deposited)
    def withdraw(self,withdrawl):
        self.withdrawl=withdrawl
        print("The amount to withdraw :",self.withdrawl)
    def check_balance(self):
        self.balance=self.balance+self.deposited-self.withdrawl
        print("THe amount of balance :",self.balance)
bala = int(input("Enter the Balance Amount: "))
ba = BankAccount(bala)
deposited=int(input("Enter the amount to deposit :"))
withdrawl = int(input("Enter the amount of withdrawl :"))
ba.deposit(deposited)
ba.withdraw(withdrawl)
ba.check_balance()
'''
class Student:
    school_name = input("Enter the school name : ")
    def __init__(self,name,roll_no):
        self.name=name
        self.roll_no=roll_no
    def __str__(self):
        return f"Name: {self.name}, Roll No: {self.roll_no}"
st = Student('bhavs',27)
print(Student.school_name)
print(st)

class Employee:
    count =0
    def __init__(self):
        Employee.count += 1
    def meth(self):
        for i in range(Employee.count):
            print("This is the ",i, " employee")
e1 = Employee()
e2 = Employee()
e3 = Employee()
e1.meth()