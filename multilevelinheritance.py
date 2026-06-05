#when the parent class have another parent class 
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