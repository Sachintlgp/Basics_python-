#Objecct_Oriented_program
class Student: 
    '''This is student class with required data'''

print(Student.__doc__) #Calling doc string


class Student: #class name
    '''Developed by Besant Tech for python demo''' #Doc string
    def __init__(self): #constructor 
        self.name="Mary" # Attribute or proporties 
        self.age=20
        self.marks=80

    def talk(self): #Method , instand method
        print("Hello I am :",self.name)
        print("My age is :", self.age)
        print("My marks are :",self.marks)

student_one=Student() #object
student_one.talk()

class Student:
    def __init__(self,name,rollno,marks): #self is the first parameter inside constructor
        self.name=name
        self.rollno=rollno
        self.marks=marks
    def talk(self): #self is the first parameter inside instance method
        print("Hello my Name is :",self.name)
        print("My Rollno is :",self.rollno)
        print("My marks are :",self.marks)

student_one =Student("Mary",101,90)
student_one.talk()

#Inside constructor by using self variable
class Employee: #class name
    def __init__(self): #constractur and instand variable
        self.eno=100 #instand variable
        self.ename="Tony"
        self.esal=10000

e=Employee() #object
print(e.__dict__)

#Inside Instance method by using self variable:
class Test:
    def __init__(self):
        self.a=10
        self.b=20
    def m1(self): #instant Method
        self.c=30 #instant variable

t=Test()
t.m1()
print(t.__dict__)

#Outside of the class by using object reference variable
class Test:
    def __init__(self):
        self.a=10
        self.b=20
    def m1(self):
        self.c=30

t=Test()
t.m1()
t.d=40
print(t.__dict__)

#Static variable
class Student:
    school_name= "SGVG" #static variable
    def __init__(self):
        self.a=100
    def disp(self):
        a=200
        print("The value of a is: ",self.a)
        print("The value of a is: ",a)

s=Student()
s.disp()
print(s.__dict__)
print(Student.__dict__)


#Local variable
class Test:
    def m1(self):
        a=1000 #local variable
        print(a)
    def m2(self):
        b=2000 #local variable
        print(b)
t=Test()
t.m1()
t.m2()

#Instance Methods
class Student:
    def __init__(self):
        self.a=100
    def disp(self):
        a=200
        print("The value of a is :",self.a)
        print("The value of a is :", a)

s=Student()
s.disp()

#Class Methods
class Animal:
    legs=4
    @classmethod
    def walk (cls,name):
        print("{} walks with {} legs...".format(name,cls.legs))

Animal.walk("Dog")
Animal.walk("Cat")

#Static Methods
class CustomMath:
    @staticmethod
    def add(x,y):
        print("The Sum :",x+y)

    @staticmethod
    def product(x,y):
        print("The Product :",x*y)

    @staticmethod
    def average(x,y):
        print("The average:",(x+y)/2)

CustomMath.add(10,20)
CustomMath.product(10,20)
CustomMath.average(10,20)

class Duck:
    def talk(self):
        print("Quack Quack")
class Dog:
    def talk(self):
        print("Bow Bow")
class Cat:
    def talk(self):
        print("Meow Meow")
def obj_fun(Obj):
    obj.talk()
d=Duck()
d.talk()
dg=Dog()
dg.talk()
c=Cat()
c.talk()

class Student:
    def walk(self):
        print("Student is walking")
s=Student()
s.walk()

class Book:
    def __init__(self,pages):
        self.pages=pages

    def __add__(self,other):
        return self.pages+other.pages

b_one= Book(100)
b_two= Book(200)

b_three = b_one + b_two

print(b_three)








