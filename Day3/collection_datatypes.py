'''
Docstring for Day5.collection_datatypes

list 
tuple 
set 

dictionary 

indexing is for accessing the data 
type() - knowing the datatype 


'''

# list  : [] , store multiple values of different datatypes , sequence datatype , ordered collection, indexes , mutable(changed) 
name="manasa"
age =28
print(type(name))

# in any sequence index starts from 0 to n-1 (n is the last value ) -- positive indexing 
# negative index values start from -1 to n
b=[10,20,30,40,"sai",90.99]
print(b[0])
print(b[3])

print(b[-1])
print(b[-4])


nums=[78,96,40,56,67]
#append() --->
#insert()
#remove()
#pop()

nums.append(100)
nums.insert(1,88)
nums.remove(40)

print(nums)

print(dir(nums))


names = "sairam", "prasad", "pasha" ,"chiru"
print(names)



nums.pop()
nums.sort() #asc order
nums.reverse() 
print(nums)

# print(dir(nums)) # methods of the datatype 


#tuple : () , order collection , duplictes , immuatable (once this tuple object is created then i can not be changed) , indexes  
# if you want change it will create new objects 

t=(10,20,20,20,30,30,30,30,30)
print(type(t))

print(set(t))

print(t[0]) # data is given based on index value

print(t.count(20))

print(t.index(20)) # getting the index value based on that particular data 

#print(dir(t))



#set : {} , unordered collection of data , not allow duplicate values , indexes not possible  

s={1,2,2,3,78,56,4,4,4,}
print(s)

r={77,88,99,111}

#print(dir(s))

s.add(99)
s.add(100)
s.add(67)
'''


#print(s[0]) # subcriptable : no indexing 

#print(s)

# we also have union , intersection in sets 

p={1,2,2,3,78,56,4,4,4,}
r={77,88,99,111,4}
print(p.union(r))
print()
print(r.intersection(p))


#rint(type(p))

'''

# Dictionary : stores the data in the form of key value pair , keys should be unique ,mutable

d={"id":1,"name":"Ram"}
print(d)
print(type(d))

print(d.keys())
print(d.values())


# range()
# sequence datatype  (strings , list , tuple)
'''
#range(0 to n-1)
range(start, end, step)

start: starting value 
default start value =0

stop : ending value 
default stop value = n-1

step : iteration 
default value = 1
 

i=i+1 


range(1,6)

1 , 5 , 
1,2,3,4,5

'''
