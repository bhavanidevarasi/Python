# when a class inherits from a single class it is called single inheritance
class Bhavs:
    def __init__(self,name):
        self.name=name
    def names(self):
        print("My name is ", self.name)
class Frnd(Bhavs):
    def __init__(self, frndname, name):
        super().__init__(name)
        self.frndname=frndname
    def frnd(self):
        print("My Frnds name is", self.frndname)
obj = Frnd("bhavs","astha")
#obj.name("bhavs")
#obj.frnd("astha",obj.name)
obj.names()
obj.frnd()
