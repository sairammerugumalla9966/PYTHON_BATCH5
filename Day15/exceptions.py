# Exception handling in python

# Error ---> mistakes in program excecution 
# type of errors ---> syntax errors , logical errors , runtime errors 
# what happens when an error occurs ---> program will crash 


try:
    a=int(input("enter a value: "))
    b=int(input("enter a value: "))
    res=a/b
    print(res)

except ZeroDivisionError as zde:
    print(zde)

except Exception as e:
    print(e)

finally:
    print("end of the program")



class AgeError(Exception):
    pass

age = int(input("enter your age "))

if age < 18:
    raise AgeError("Age must be above 18")









