import argparse
'''
parser = argparse.ArgumentParser(description = "Displaying name and age of a person")
parser.add_argument("name", nargs ="?" ,default = "bhavs")
parser.add_argument("--age",type=int,required = True)
parser.add_argument("Cars", choices=["Mercedes","McLaren","Buggati","Miata"])
parser.add_argument("--debug",action="store_true")
args = parser.parse_args()
print(args.name)
print(args.age)
'''
# Creating a list and doing their summation
'''
parse = argparse.ArgumentParser()
parse.add_argument("nums",nargs = "+",type = int)
arg = parse.parse_args()
summ = 0
for num in arg.nums:
    summ += num
print(summ)
#using sum method
print(sum(arg.nums)) 
'''
#doing simple calculations
'''
parser = argparse.ArgumentParser()
parser.add_argument("a",type = int)
parser.add_argument("b",type = int)
args = parser.parse_args()
def add(a,b):
    return a + b
def sub(a,b):
    return a - b
def mul(a,b):
    return a * b
def div(a,b):
    return a // b
print(add(args.a,args.b))
print(sub(args.a,args.b))
print(mul(args.a,args.b))
print(div(args.a,args.b))
'''
#Student Detail Program
parser = argparse.ArgumentParser()
parser.add_argument("--name",nargs = '+', type = str)
parser.add_argument("--rollno", nargs = "+",type=int,required = True)
parser.add_argument("--marks",type = int,nargs="+")
args = parser.parse_args()
for na,ro,ma in zip(args.name,args.rollno,args.marks):
    print(na, ro, ma)
for nam in args.name:
    print(nam,end = " ")