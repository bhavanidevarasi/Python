#importing just the wanted method
from Calc import add
print(add(5,2))

#import everything in module
from Calc import*
print(add(2,3))

#import with aliases
import Calc as c
print(c.add(2,3))