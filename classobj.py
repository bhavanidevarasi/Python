#JUST CLASS WITH SIMPLE CONSTRUCTOR
""""
class Dog:
    species = "DoberMan"
    def __init__(self, name, age, color):
        self.name = name
        self.age=age
        self.color=color
dog1 = Dog("buddy", 5,"brown")
print(dog1.name)
print(dog1.age)
#to take input from the user
name=input("Enter the name: ")
age=int(input("Enter the age: "))
color=input("Enter the color: ")
obj=Dog(name,age,color)
print(obj.name, obj.age, obj.color)
"""
#CLASS WITH METHODS
""""
class Details:
    def public(self, name, age):
        self.name=name
        self.age=age
    def private(self, address, phoneno):
        self.address=address
        self.phoneno=phoneno
obj1 = Details()
name=input("Enter the name: ")
age=int(input("Enter the age: "))
address=input("Enter the address: ")
phoneno=input("Enter the phoneno: ")
obj1.public(name,age)
obj1.private(address,phoneno)
print(obj1.name, obj1.age, obj1.address, obj1.phoneno)
"""
#CLASS WITH MULTIPLE TYPE FUNCTION METHODS
class Breakfast:
    def __init__(self, name, type):
        self.name=name
        self.type=type
    def rating(self,ratingg):
        self.ratingg=ratingg
        return ratingg #USING RETURN INSIDE THE METHOD
    def taste(self,tasey):
        self.tasey=tasey #USING PRINT INSIDE THE METHOD
        print(self.tasey)
bg=Breakfast("upma","veg")
print(bg.rating(3))
bg.taste("good")
print(bg.name,bg.type)
