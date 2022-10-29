#function
#Writing function to print message
def wish(): #function
    print("Hello Good Morning") #Message

wish()

def wish(name): #parameter
    print(f"Hello {name} Good Morning")

wish("Tony") #providing values
wish("Maria")

def wish(name):
    print(f"Hello {name} Good Morning")

wish("Tony")
wish("Maria")
return_value=wish("john") #return statement
print(f'Return value is {return_value}')

def add_sub(a,b):#a,b are the parameter 
    add=a+b #addition
    sub=a-b#substraction
    return add,sub #return statement

add,sub=add_sub(67,50) #providing values

print(f"The addition of two numbers is {add}")
print(f"The subtraction of two numbers is {sub}")

#variable length arguments:
#*arg

def sum_fun(*arg): #function, arg is variable length argument
    total=0
    for number in arg:
        total=total+number
    print("The Sum=",total)

sum_fun()
sum_fun(10)
sum_fun(10,20)
sum_fun(10,20,30,40)

def sum_fun(name,*arg):#We can mix variable length arguments with positional arguments
    print(name)
    total=0
    for number in arg:
        total=total+number
    print("The Sum=",total)
sum_fun("z")
sum_fun("A",10)
sum_fun("B",10,20)
sum_fun("C",10,20,30,40)

def number_display(**kwargs):
    for k,v in kwargs.items():
        print(k,"=",v)
number_display(n1=10,n2=20,n3=30)
number_display(roll_no=100,name="Tony", marks=70, subject="Java")

a=10 #global variable
def print_number():
    print(a)
    
def display_number():
    print(a)

print_number() #calling a as number
display_number() #calling a for display function

def print_number():
    a=100 #Local variable
    print(a)
def display_number():
    print(a)# invalid we can't access local variable of other function

print_number()
display_number() #in this it is printing global variable


a=1111
def print_number():
    global a
    a=100 #Im changing value of global variable
    print(a)
def display_number():
    print(a)

print_number()
display_number()


#Lambda Function: Functions without any name
#Write lambda function to sum two numbers"

sum_number=lambda a,b:a+b
print(sum_number(10,20))

#Write lambda function perform square of number
square_number=lambda a:a*a
print(square_number(20))


#Example:Program to filter only even numbers from the list by using filter() function
#without filter function
def isEven(x):
    if x%2==0:
        return True
    else:
        return False
l=[0,5,10,15,20,25,30]
l1=list(filter(isEven,l))
print(l1)

#with lambda function
l=[0,5,10,15,20,25,30]
l1=list(filter(lambda x:x%2==0,l))
print(l1)
l2=list(filter(lambda x:x%2!=0,l))
print(l2)

#Exmple:Double the elements in list

#without lambda function
l=[1,2,3,4,5]
def double_it(x):
    return 2*x
l1=list(map(double_it,l))
print(l1)

#with lamba function
l=[1,2,3,4,5]
l1=list(map(lambda x:2*x,l))
print(l1)

#Mutiple elements in two lists
l1=[1,2,3,4]
l2=[2,3,4,5]
l3=list(map(lambda x,y:x*y,l1,l2))
print(l3)

    
#Sum of all elements in the list
from functools import*
l=[10,20,30,40,50]
result=reduce(lambda x,y:x+y,l)
print(result)

#functions are also objects
def fun_print():
    print("Hello")
print(fun_print)
print(id(fun_print))
print(type(fun_print))


#Module custommath.py
import custommath
x=888
def add(a,b):
    print("The Sum:",a+b)

def product(a,b):
    print("The product:",a*b)
    

