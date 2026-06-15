#simple method over-riding runtime polymorphism
'''
class X:
    def greet(self):
        return "hello"
class Y:
    def greet(self):
        print("ha")
        return "namaste"
class Z:
    def greet(self):
        return "olaa"
class A:
    def greet(self):
        return "konnichiwa"
lis = [X(),Y(),Z(),A()]
for i in lis:
    print(i.greet())
a = A()
print(a.greet())
'''
#polymorphism using duck-typing --runtime polymorphism -- method overriding
'''
class X:
    def use(self):
        return "hello"
class Y:
    def use(self):
       # print("ha")
        return "namaste"
class Z:
    def use(self):
        return "olaa"
class A:
    def use(self):
        return "konnichiwa"
def per(too):
    print(too.use())
per(A())
per(Z())
per(Y())
'''
#calculating salary using method overriding
class Fulltime:
    def salary(self):
        print("2ooo")
class Parttime:
    def salary(self,hrs,rate):
        sal = hrs * rate
        print(sal)
p = Parttime()
p.salary(2,300)
f = Fulltime()
f.salary()

class Animal:
    def sound(self):
        print("it sounds")
class Cat():
    def sound(self):
        print("it sounds meow")
ca = Cat()
ca.sound()
an = Animal()
an.sound()