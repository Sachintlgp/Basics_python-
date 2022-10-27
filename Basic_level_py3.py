#set Function/Method:

s=set() #using this function we can create empty set
print(s)
print(type(s)) #data type we can see

s={1,2,3,4,5,6,7,1,2,3,4,5,6,7,9,5,4,3}
print(s) #duplicate data elements are not allowed


s=set([1,2,3,4,5,6,7,1,74,62,42,1,24,53,8,16])
print(s) #insertion order is not preserved


#adding element to set
#add():This function take only one argument

s={1,2,3,4,5,6,7,8,9}
s.add(111)
print(s)

#Update function
l=[1,2,3]
t=[111,222,333]
s={888,999,777}
s1=set()
s1.update(l,t,s)
print(s1)

#Copy function
#This function is used to create copy of set

s={1,2,3,4,5,6,7}
s1=s.copy()
print(s1)
print(s)

#Remove Elements
#pop: To remove the elements
s={1,2,3,4,5,6,7}
s.pop()#removing the first element
print(s)

s.remove(7) #removing the specified element
print(s)

#clear to remove all element
s.clear()
print(s)

#Del to delete complete set
del s

#Union: This is way to join element in two sets
s={1,2,3}
s1={4,5,6}
s.union(s1)
print(s.union(s1))


#Intersection : this method will return a new set that only contain the item that are present in both sets
s1={1,2,3,4,5,6,7,8,9,10}
s2={11,12,1,2,3,13,14,8,9,15,16,17}
s1.intersection(s2)
print(s1.intersection(s2))

#Intersection update : This function will keep only the items that are present in both sets
s1={1,2,3,4,5,6,7,8,9,10}
s2={1,2,3,8,9,11,12,13,14,15,16,17}
s1.intersection_update(s2)
print(s1.intersection_update(s2))

#Difference of two sets
s1={1,2,3,4,5,6,7,9,8,11,43,67}
s2={12,13,1,3,4,5,21,78,54}

print(s1.difference(s2))

print(s2-s1)

#String Concatenation Operator
print("Hello "+"World")

#"Hello"+ int # it gives the error becuase second operator not in format

#String Repetition Operator
print("Hello" * 2)


