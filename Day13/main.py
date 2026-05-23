
'''
from calculator import add,sub
# from calculator import *

a= int(input("enter a value : "))
b= int(input("enter b value : "))

option = int(input("enter 1 for add or 2 for sub "))

if option == 1:
    print(add(a,b))
elif option == 2:
    print(sub(a,b))

else:
    print("you have choosen wrong option")


import calculator

a= int(input("enter a value : "))
b= int(input("enter b value : "))

option = int(input("enter 1 for add or 2 for sub "))

if option == 1:
    print(calculator.add(a,b))
elif option == 2:
    print(calculator.sub(a,b))

else:
    print("you have choosen wrong option")
'''

# Inbuilt modules in python :

# help("modules")

import math

print(math.sqrt(81))
print(math.factorial(5))



import random

print(random.random())  # 0-1

print(random.randint(1000,9999))

print(random.choice([1,2,4,5,7,89,9]))  # random number from a sequence 

print(random.sample([101,102,103.104,105,106],2))


import datetime

today = datetime.datetime.now()
print(today)


import sys

print(sys.version)


