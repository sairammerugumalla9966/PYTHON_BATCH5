'''
# loops : if you repeat a block of code multile times then it is a loop 

print("sairam")


# for loop 
 # a for loops is used for iteration over a sequence . (range , list , tuple , string)

# when we know the range (how many times)

#for varibale in sequence:
    #statements 
    #statements 

employees=["sathwik", "sumanth","Naseem", "manasa","sairam"]

for emp in employees:
    print(emp, "is a super man ")

print("come out of dreams")


# strings 

name=input("enter any name")

for x in name:
    print(x)


for i in range(1,11):
    print(i)


'''
# while loop 
# when you dont know the range 
# it excecutes untill the condition is true 

# while condition :
    #statements 
    #statements 
'''
i=1
while i<=5:
    print(i)
    i+=1

'''
# prime number 
# number which is divisible by 1 and itself 

'''

# is prime number or not 

num=int(input("enter any number : "))
count=0

for i in range(1,num+1):
    if num%i==0:
        count+=1

if count==2:
    print(num, "is a prime number")
else:
    print(num, "is a not prime number")




# prime number or not using while loop 

num=int(input("enter any number : "))
count=0
i=1
while i<=num:
    if num%i==0:
        count+=1
    i+=1

if count==2:
    print(num, "is a prime number")
else:
    print(num, "is a not prime number")


# first 10 prime numbers program 

# 2,3,5,7,11,13,17,.......

num=2
count=0
while count<10:
    i=1
    factor=0
    while i<=num:
        if num%i==0:
            factor+=1
        i+=1

    if factor==2:
        print(num)
        count+=1
    num+=1




 # for loop : if we know how many times we want run the loop (know iterations)
 # sequence can be string , list , tuple or range

# for var in sequence:
    # block of code
    # block of code
    # block of code
    # block of code
for i in range(1,5): #1, 2 ,3 ,4
    print(i ,end =" ")
    print()


for char in "power start":
    print(char)

# count vowles in this string 

msg ="python education" 
count=0

for char in msg:
    if char in "aeiou":
        count += 1  # (count = count + 1)

print("count is : " ,count)


# reverse numbers

for i in range(5,0,-1):
    print(i)


# while loop 

# while condition:
    # block of code 
    # block of code 

i=1 # initialization
while i <= 5:  # condition
    print(i)
    i+=1    # incrementation 



# is_prime
 
num=int(input("enter any number : "))
count=0

for i in range(1,num+1): #14 iteration
    if num%i==0:
        count+=1

if count==2:
    print(num, "is a prime number")
else:
    print(num, "is a not prime number")


# 13 is prime or not ?? 

# prime number or not using while loop 

num=int(input("enter any number : "))
count=0
i=1
while i<=num:
    if num%i==0:
        count+=1
    i+=1

if count==2:
    print(num, "is a prime number")
else:
    print(num, "is a not prime number")


# To print  first 10 prime numbers using while loop  



# git bash
# git commands
# # nested loops 
# patterns using loops  
# functions 


'''
