# types of arguments 

# positional args : maintain same order 


def login(username , password):
    if username == "admin":
        if password == "Rocky123":
            return "login success"
        else:
            return "wrong password"
    else:
        return "invalid username"

print(login("Rocky123" ,"admin"))

# print(login("sairam" ,"Rocky123")) 

# keyword arguments : give the arguments with parameter names 

def login(username , password):
    if username == "admin":
        if password == "Rocky123":
            return "login success"
        else:
            return "wrong password"
    else:
        return "invalid username"

print(login(password="Rocky123" , username="admin"))


# *args --- variable length arguments for multiple values 

def total(*price):
    print(sum(price))

total(100,200,300,400,500)

# default arguments 

def login(password,username="admin"):
    if username == "admin":
        if password == "Rocky123":
            return "login success"
        else:
            return "wrong password"
    else:
        return "invalid username"

print(login("Rocky123","guest"))


# key-value arguments (**kwargs)

def profile(**data):
    print(data)

profile(name="sairam",age=28,jobrole ="trainer")


# parameters ,default, *args , **kwargs

def demo(a ,b=10,*args,**kwargs):
    print(a)
    print(b)
    print(args)
    print(kwargs)

demo(99,100,"sairam",50000,28,"superman", jobrole = "trainer", place="hyd",DOB="23-04-2026")



# Recursion : technique where a function calls itself 

# 5! = 5*4*3*2*1 

def factorial(n):
    if n == 1:
        return 1
    return n*factorial(n-1)

print(factorial(5))



def sum_no(a):
    if a == 0:
        return 0
    return a + sum_no(a-1)

print(sum_no(10))


# higher order functions --> map(), filter() , reduce()
# OOPS
# file handling 
