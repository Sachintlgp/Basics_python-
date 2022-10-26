import keyword
keywords=keyword.kwlist
print(keywords)

print(len(keywords)) #Length of keyword


number_list=[] #Empty list created
print(type(number_list))#it show the data type

a=list(range(0,9)) #Range is a function which returns iterable
print(a)

a=[1,2,3]
print(a)

a=[1,2,"Tony",(4,5),3,4,[1,4]] #list is allowed number and character
print(a)


i=list("Bengaluru") #list sequence
print(i)


lil=[1,2,[3,5,333,222],4,999]
for i in lil:#iterate over list using loops
    print(i)

lil.clear() #delete all elements in the list
print(lil)

    
del lil #delete the list


a=[1,2,3,4,5,6,7,8]
print(len(a)) #it gives the lenth of the list

a.count(2)
print(a.count(2))#Gives the count of element in the list

#index gives the return index of specified element in the list.
a=[1,2,3,4,5,3,4]
a.index(3)
print(a.index(3))

#append - Add element at the end
i=[1,2,3,4]
i.append(5) #add the element at the end
print(i)

#Insert - Add the element at the particula index.
i=[1,2,3,4,5,6]
i.insert(0,100) #add 100 in the first place
print(i)

#extend - add the elements present in the given sequence to the list
i=[1,2,3,4]
i1=[100,200,300]
i.extend(i1) #add the two list
print(i)

#pop will remove element of index provided
i.pop(0)#it remove the first index number of the list
print(i)

#clear- remove all elements from the list
i.clear()
print(i)

#delete you can delete your list
del i


#Reverse- reverse the elements of the list
#create a list of prime numbers
prime_number=[2,3,5,7]

#reverse the order of list elements
prime_number.reverse()

print("Reversed list:",prime_number)

#sort
l=[12,45,6,7,43,3,134,6,8,768]
l.sort() #default sorting order for number is ascending
print(l)


#Tuple
t=(10,20,30,40)
print(type(t))

t=(10,20,30,40)
for i in t:# we can iterate over using loops
    print(i)


#delete tuple using del tuple_name
del t

t=20,30,40 #Here parentheses are optional
print(type(t)) 

t =() #empty tuple
print(t)

t=(10,) #by adding comma it will treat as tuple
print(type(t))

t=10,#by adding comma it will treat as tuple
print(type(t))

l=[11,22,33]
print(type(l))

l=tuple(l) #data type casting or converting to tuple
print(type(l))

#Methods on tuple
t=tuple([1,24,4,5,6,7,45,2,36,4,8,9,7,3,4,23,7])
print(t)

print(len(t)) #it gives the length of tuple

t.count(4) #it gives the count of number
print(t.count(4))


t.index(24) #it gives the index number of elements
print(t.index(24))

print(min(t)) #it gives the minimum number of elements

print(max(t)) #it gives the maximum number of elements

#tuple packing
a=10
b=20
c=30
d=40
t=(a,b,c,d)
print(t)

#tuple unpacking
q,x,y,z =t
q
10
x
20
y
30
z
40
print(t)

#Dictionary

d={} # Empty dictionary
print(d)

d=dict() #empty dictionary will create
print(d)

d[100]="Tony" #adding pair in this way
print(d)

d[102]="Mary"
print(d)

for key, value in d.items(): #we can iterate over dictionary using loops.
    print(key,value)

d.clear()#clearing dictionary
print(d)

del d #deleting dictionary

d=dict([[1,2],[3,4],[5,6],[7,8]]) #dictionary created using list of list
print(d)

d=dict([(1,2),(3,4),(5,6),(7,8)]) #dictionary created using list of tuple
print(d)

d=dict(((1,2),(3,4),(5,6),(7,8))) #dictonary created using tuple of tuple
print(d)


print(len(d)) #gives the length of dictionary

print(d.get(7))



