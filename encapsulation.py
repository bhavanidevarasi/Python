class Details:
    def __init__(self,name,age,num):
        self.name=name
        self._age=age#protected --accessed through subclass or other meths isdie class
        self.__num=num#private
    def numms(self):#can be accesses using method
        print(f"the age is {self._age} and number is {self.__num}")
    def get_num(self):
        return self.__num
class Number(Details):
    def numm(self, nu):
        print("the number is ", nu)#cant access thr private attributes directly
        print("the age is : ", self._age)
    def ages(self):
        print("the age is : " ,self._age)
A = Details("bhavs",21,7897887)
print(A.name)
A.name = "haryy"
print(A.name)
A.numms()
N = Number("ron",22,9898989)
N.numm(A.get_num())
N.ages()

