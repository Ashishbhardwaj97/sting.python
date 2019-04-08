def add(a,b):
    print(a+b)
    
def sub(a,b):
    print(a-b)

def mul(a,b):
    print(a*b)

def div(a,b):
    print(a/b)
    
def power(a,b):
    print(a**b)
            
            
print("enter 1 to add")
print("enter 2 to subtract")
print("enter 3 to multiply")
print("enter 4 to division")
print("enter 5 for x to the power of y")

c = int(input("enter the no. to perform action: "))

a= int(input("enter value of a: "))
b= int(input("enter value of b: "))

if c==1:
    add(a,b)

if c==2:
    sub(a,b)

if c==3:
    mul(a,b)

if c==4:
    div(a,b)

if c==5:
    power(a,b)
    
else:
    print("Invalid Input")


