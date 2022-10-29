#Control Flow
#Conditional Statement - if, if-elif, if-elif-else
#Transfer Statement - Break, Continue, pass
#Iterative Statement - for , while


#if Statment:
number=100
if number>50: 
    print(f"{number} is greater than 50")
    
number=10
if number >50:
    print(f"{number} is greater than 50")
if number <50:
    print(f"{number} is lesser than 50")

    
    
#if-else statment:
#If condition-1 is true then , action-1 will be executed, otherwise action-2 will be executed.
number=10
if number>5:
    print(f"number {number} is greater than 5")
else:
    print(f"number {number} is less than 5")
    
name="Tata Consaltancy Service"
if name =="Tata Consaltancy Service":
    print(f"Here at {name} your working place")
    print(f"{name} sitauated at Think Compous")
    print(f"{name} is in eletranic city ")
else:
    print("You are in another IT Company")
    print("You are not in Electranic city")
    print("Thank you for your information")

brand=input("Enter Your Favourite Brand:")
if brand=="XY":
    print("It is children's brand")
elif brand=="AB":
    print("This is women's brand")
elif brand=="PQ":
    print("This is men's brand")
else: #else part is always optional
    print("Other brands are not available")

#for loop

s="Bengaluru"
for x in s: #sequence
    print(x)

s=input("Enter some string: ")
i=0 
for x in s:
    print("The character present at  ",i, "index is :",x)
    i=i+1

#Whiile loop
i=1
while i<=10:
    print(i)
    i+=1


    
    
