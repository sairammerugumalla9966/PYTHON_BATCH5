# HIGHER ORDER FUNCTIONS 

# function which takes another function as an argument 
# returns another function 


def add(a,b):
    return a+b

def sub(a,b):
    return a-b


def calculate(func,x,y):
    return func(x,y)

print(calculate(add,10,20))
print(calculate(sub,100,20))

print(calculate(lambda a,b : a*b, 5,4))
      

# built in higher order functions (data processing)
# map() ---> map(func,iterable)

num=[1,2,3,4,5]
square = list(map(lambda x : x*x ,num)) 
print(square)


names = ["PrasaD" ,"SaiRam","RocKy"]
upper_case=list(map(str.upper ,names))
print(upper_case)


# filter() -->filter(function , iterable)

nums=[10,15,20,25,33,22,88]
p = list(filter(lambda x: x%2 ==0, nums))
print(p)


n=[-10,15,-20,-25,33,-22,-88]
positive=list(filter(lambda x: x>0 ,n))
print(positive)


# reduce() --->reduce(func, iterable)

from functools import reduce

s=[10,15,20,25,33,22,88]
print(reduce(lambda x,y: x+y , s))






