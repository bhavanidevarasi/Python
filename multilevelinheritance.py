#when the parent class have another parent class 
'''
class Version1:
    def __init__(self,ver1name):
        self.ver1name=ver1name
class Version2(Version1):
    def __init__(self,ver2name,ver1name):
        self.ver2name=ver2name
        super().__init__(ver1name)
class Version3(Version2):
    def __init__(self,ver3name,ver2name,ver1name):
        self.ver3name=ver3name
        super().__init__(ver2name,ver1name)
    def Versions(self):
        print("Version 1 : ",self.ver1name)
        print("Version 2 : ",self.ver2name)
        print("Version 3 : ",self.ver3name)
obj = Version3("landphone","buttonphone","smartphone")
obj.Versions()
'''
class Person:
    def __init__(self,name):
        self.name=name
    def per(self):
        print("he is a person!!",self.name)
class Employee(Person):
    def __init__(self,empname,name):
        super().__init__(name)
        self.empname=empname
    def emp(self):
        print("He is an employee",self.empname)
class Manager(Employee):
    def __init__(self,man_name,name,empname,):
        super().__init__(empname,name)
        self.man_name=man_name
    def Details(self):
        return ( 
                 f"Person name : {self.name}\n"
                 f"Employee name : {self.empname}\n"
                 f"Manager name : {self.man_name}"
        )
man = Manager('Manager','Person','Employee')
print(man.Details())