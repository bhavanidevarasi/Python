
def decorator(func):
    def ughhh():
       # print("Before Decorator")
        return func()
    return ughhh
@decorator
def greet():
   # print("Hii how are you!!")
   return 'how are you!!'
print(greet())

def decorator(fun1):
    def wrap1():
        print("Before")
        fun1()
        print("after")
    return wrap1
def greets():
    print("HELLOOOO")
greets = decorator(greets) # instead of this we use @decorator
greets()

#basic decorator
def decorator(abs):
    def nam():
        print("function is starting...")
        abs()
        print("Function completed!")
    return nam
@decorator
def name():
    print("Hello!!")
name()

#using return values
def decorator(ret):
    def neww():
       # return "*** " + ret() + " ***"
        return "* " * 3 + ret() + " *" * 3
    return neww
@decorator
def Hey():
    return 'heyyy'
print(Hey().upper())#returning text upper case

#multiply the returned number
def decorator(mul):
    def wraps():
        return mul()*2
    return wraps
@decorator
def multi():
    return 10
print(multi())

#count funccction calls
def decorator(calls):
    count =0
    def wraped():
        nonlocal count
        count +=1
        print(f"function called {count} times")
        calls()
    return wraped
@decorator
def call():
    pass
call()
call()
call()
call()

#using args 
def decorator(funct):
    def wrape(*args):
        return funct(*args)
    return wrape
@decorator
def say(name,ugg):
    print("Hii",name,ugg)
say("bhavs","heyy")