
#local variables that is inside and belongs to function
def Deets():
    name = input()
    print("The name is : ", name)
Deets()
#print("The names are :",name) -- gives error as name isn't defined outside
#global variables can be accessed anywhere and declared outside functions

name = input()
def Car():
    print("The car name is : ", name)
Car()
print("This" ,name, "is latest model")

# using both local and global var
def Types():
    name = "Aston martin"
    print(" i like",name,"cars")
name= "ferrari"
Types()
print("The new",name,"is worse")