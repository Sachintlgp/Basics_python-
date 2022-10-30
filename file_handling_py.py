'''Attribute of file object'''
f=open("ecom_project.txt","w")
print("File Name :", f.name) #gives the name of file name
print("File Mode :", f.mode) #gives the mode of file
print("Is file Readable :",f.readable()) #Return the boolean value indicates that wheter file is readble or not
print("Is file Writable:",f.writable())#Return the boolean value indicates that wheter file is writable or not
print("Is file closed:",f.closed)#Return the boolean value indicates that wheter file is closed or not
f.close()
print("Is file closed :",f.closed)

'''Writing data to a file'''
f=open("Tata_service.txt","w") #file name
f.write("Tata\n") #writing data
f.write("Consaltancy\n")
f.write("Think_Compous\n")
print("Data Written to the file sucessfully")

#Appending data to a file
f=open("Tata_service.txt","a")
f.write("Think Compous\n")
f.write("Eletranic city\n")
f.write("Bangalore\n")
print("Data written to the file sucessfully")
f.close()

#Writing multiple line to a file
f=open("Tata_service.txt","a")
list=["Python\n","Java\n","HTML\n","Javascript\n"]
f.writelines(list)
print("List of lines written to the file sucessfully")
f.close()

#Reading data from file
f=open("Tata_service.txt","r")
data=f.read()
print(data)
f.close()

'''To read only first 50 characters'''
f=open("Tata_service.txt","r")
data=f.read(50)
print(data)
f.close()

'''To read line by line'''
f=open("Tata_service.txt","r")
lines=f.readlines()
for line in lines:
    print(line,end=" ")
f.close()

#Delet a file
#To delete a file must import os module
import os
os.remove("Demofile.txt")

