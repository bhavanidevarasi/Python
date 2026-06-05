"""
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
"""
"""
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
"""
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

