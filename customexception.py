#Normal exception basic
class AgeError(Exception):
    pass
class MarksError(Exception):
    pass
age  = 10
marks =20
try:
    if age <=18:
        raise AgeError("Age must be greater than 18")
    if marks <50:
        raise MarksError("Marks should be grester than 50!!")
except AgeError as e:
    print(e)
except MarksError as e:
    print(e)
# custom exceptions with constructor
class Balance(Exception):
    def __init__(self,balance,withdraw):
        self.balance = balance
        self.withdraw = withdraw
        super().__init__(
        f"  balance : {balance}, withdraw : {withdraw}"
        )
try:
    raise Balance(1000,2000)
except Balance as e:
    print(e)
class passwordlength(Exception):
    pass
password = input()
try:
    if len(password) > 8:
        raise passwordlength("THe password should be less than or equal to 8!!!!!!")
except passwordlength as e:
    print(e)

class salaryError(Exception):
    pass
salary = 0
try:
    if salary == 0:
        raise salaryError("the min salary should be greater than 0")
except salaryError as e:
    print(e)

#exceptions with meethod
class addition(Exception):
    def add(a,b):
        return a//b
a = 2
try:
    b = int(input())
    if b ==0:
        raise addition("Can't divide with zero!!")
    else:
        print(addition.add(a,b))
except addition as e:
    print(e)

class UsernameError(Exception):
    def help(self):
        return "user name must be admin"
class PasswordError(Exception):
    def help(self):
        return "password must be 123434"
try:
    username = "user"
    if username != "admin":
        raise UsernameError()
except UsernameError as e:
    print(e.help())
try:
    password = "user"
    if password != "123434":
        raise PasswordError()
except PasswordError as e:
    print(e.help())
