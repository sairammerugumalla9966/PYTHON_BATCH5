# Functions ??
# what is function ??
# 
# reusability ---> 
# readabilty --> proper structure 


#def functionName():
    #block of code 
    #block of code 
    #block of code 

#functionName()

# Naming conventions -->  camelCase or snake_case

# types of functions --> built in functions 

# print() , type() ,len(),input(),int(),float(), sum() ,max() , min(),

#  user defined functions 

def message():
    print("welcome to python training")
    print("bye bye")

message()
message()
message()
message()


# num = 1234 reverse of the number ?? 4321

num = "1234"
print(num[::-1])

#1234 % 10 = 4
#123 % 10 = 3
# 12 % 10 =2
# 1 % 10 = 1

# 1234 // 10 = 123.4

# rev = 4321

def reverse_no():
    num = 1234
    rev = 0

    while num > 0: 
        rev = rev * 10 + num % 10 
        num //= 10
    print(rev)

reverse_no()    



# parameters and arguments 

def add(a,b):  # parameters
    c=a+b 
    print(c)

add(10,20) #arguments 

add(19,200) #arguments 


def add(a,b):  # parameters
    c=a+b 
    print(c,"it is from print")

print(add(10,20)) #arguments 

# add(19,200) #arguments 


def add(a,b):  # parameters
    c=a+b 
    return c

print(add(10,20)) #arguments 

# add(19,200) #arguments 


def login(username , password):
    if username == "admin":
        if password == "Rocky123":
            return "login success"
        else:
            return "wrong password"
    else:
        return "invalid username"

print(login("admin" ,"Rocky123"))

print(login("sairam" ,"Rocky123")) 





