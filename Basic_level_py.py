print("Welcome to Python Tutorials")#comment after a statement

'''welcome to Python Tutorials''' #triple quoted multie line string is also treater as a comment


name="Ram"
print(name)#display single variable
age=20
print(name, age)#display multiple variables
print("Name :",name, "Age :",age)#Display formatted output

a = 10
b = 20
c = 30

print(a,b,c,sep='-')#used sep parameter

print("Begauru",end="*") #used end parameter


a=15
b=25


print("Value of a is %d and value of b is %d"%(a,b)) #value format specifier got replaced with value of data type

name="Mary"
age =22

print("Hello {} your age is {}".format(name,age))#using .format operator

print("Hello {1} your age is {0}".format(age,name))#

print("Hello {0} your age is {1}".format(name,age))

print("Hello {name} your age is {age}".format(name="Mary",age=22))

name="Mary"
print(f"Hi {name},how are you ?.")# using f string operator

a=10
b=20
print(f"Addition of a and b is {a+b}")# f string get evaluated

name="Tushar"
age =23
print(f"Hello, My name is {name} and I'm {age} year old.")

name = "Sachin" #String
Age =26 #integer
Status = True #Boolean

x=100
id(x)#this gives address of x in memory.
print(id(x))
print(type(x)) #this gives the type of x in memory.

y=123.45
print(type(y))#float type

y=int(123.45) #Data onversion float to int
print(y)
print(type(y))

z=123
print(float(z))#Data conversion int to float
print(type(z))

z="20"
print(str("z")) #Data conversion into string
print(type(z))

z="123.45"
print(str("z"))# Data conversion from float to string
print(type(z))

'''Details explanation of string Data type'''
city ="Bengaluru"
print(city[0])#Accessing from positive index

print(city[-9])#Accessing from Negative Index

city[2:8]#Slice operator,it divide string into multiple pieces
print(city[2:8])

city.upper()
print(city.upper())#convert a string into upper case

print(city.lower())# conver a string into lower case

print(len(city))# gives the length of string



