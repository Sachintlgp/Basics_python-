#while loop - If we want to execute a group of statements iteratively untill some condition false.

i=1 #it will iterate from 1
while i <=10: #it will excicute till 10
    print(i)
    i=i+1 #it will excicute add 1 for each number
    

    
#infinite Loops here always condition is true
#i=0 #it will iterate from o
#while True:
    #i=i+1
    #print("Hello",i) #To stop infinite loop commond Ctrl+C

    
#Nested Loops:
   #loop inside another loop.

for i in range(4):
    for j in range(4):
        print("i=",i,"j=",j)

#Break
for i in range(10):
    if i==7:
        print("Processing is enough..Pls break")
        break
    print(i)
print("We are done with loop execution")

#Continue: To skip current iteration and continue next
for i in range(10):
    if i%2==0:
        continue #to skip the current iteration, it will provide odd number now
    print(i)

cart=[10,20,30,40,50]
for item in cart:
    if item >=500:
        print("We cannot process this order")
        break #break will not exicuted now
    print(item)
else:print("Congrats...all items processed successfully")

cart=[10,200,300,400,50]
for item in cart:
    if item>=500:
        print("We cannot process this order")
        break #break will get executed
    print(item)
else:
    print("Congrats...all items processed successfully")

#Pass
if True:
    pass

#assert statement:
city ="Bangaluru"
assert city=="Mumbai","city should be 'Bangaluru'" #assert false

greet="Hello"
assert greet=="Hello"#assert true no error will come
assert greet=="GoodBye" #assert false,assertion error is raised
