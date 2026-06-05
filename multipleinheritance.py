# when there are mone than one parent class it is calleed multiple inheritance
# it derives all the methods from the both the parent class
# without any arguments or variables
""""
class Bike:
    def type(self):
        print("The bike is royal enfield 350")
class Car:
    def types(self):
        print("The car is ford mustang")
class Both(Bike, Car):
    pass
obj = Both()
obj.type()
obj.types()
"""
class Bike:
    def bike(self, Bikename):
        self.Bikename=Bikename
class Car:
   def car(self, Carname):
       self.Carname=Carname
class Both(Bike, Car):
    def names(self):
        print(self.Bikename, self.Carname)
obj = Both()
obj.bike("RoyalEnfield")
obj.car("Ford Mustang")
obj.names()

