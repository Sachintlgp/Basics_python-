try:
    x=int(input("Enter First Number:"))
    y=int(input("Enter Second Number:"))
    print(x/y)
except ZeroDivisionError:
    print("Can't Divide wih Zero")
except ValueError:
    print("Please provide int vlaue only")


age=int(input("Enter Age:"))
if age <18:
    raise TooYoungException("Not Eligible")
elif age >18:
    raise TooOldException("Eligible")
else:
    print("You will get email!!!")
    
        
