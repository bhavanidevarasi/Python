# when one class have more than two child classes

class Version1:
    def __init__(self,ver1name):
        self.ver1name=ver1name
    def ver1(self):
        print("This is Verison 1")
        print("Version 1 :",self.ver1name)
class Version2(Version1):
    def __init__(self,ver2name,ver1name):
        self.ver2name=ver2name
        super().__init__(ver1name)
    def ver2(self):
        #print("Version 1 :",self.ver1name)
        print("Version 2 :",self.ver2name)
class Version3(Version1):
    def __init__(self,ver3name,ver1name):
        self.ver3name=ver3name
        super().__init__(ver1name)
    def ver3(self):
        # print("Version 1 : ",self.ver1name)
        print("Version 3 : ",self.ver3name)
obj = Version2("buttonphone","landphone")
obj.ver1()
obj.ver2()
obj1 = Version3("smartphone","landphone")
obj1.ver1()
obj1.ver3()

class inherit1:
    def meth1(self):
        print("This is Parent class!!")
class inherit2(inherit1):
    def meth2(self):
        print("This is child class 1!!")
class inherit3(inherit1):
    def meth3(self):
        print("This is child class 2!!")
obj1 = inherit2()
obj1.meth1()
obj1.meth2()
obj2 = inherit3()
obj2.meth1()
obj2.meth3()
