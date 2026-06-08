class AgeError(Exception):
    pass
age  = 10
try:
    if age <=18:
        raise AgeError("Age must be greater than 18")
except AgeError as e:
    print(e)