
'''
# Types of variables in OOPS :

# local variables 
# variables which are inside of the methods 
# local variables can not be accessed through objects or class name 

class A :
    def demo(self):
        name ="python"
        print(name)

    def sample(self):
        salary = 50000
        print(salary)

obj = A()
obj.demo()
obj.sample()


# class variables or static variables : variables which are declared inside a class and outside of the method 
# class var can be accessed by class name and also all the objects which are created from the class 
# we can also update the class variables using class name
# we can also update the class variables using objects 


class sample:
    a =100
    b =200

    def sample_method(self):
        print("samplemethod")

    job = "trainer"



print(sample.a ,"through class name")
print(sample.b,"through class name")

x = sample()
sample.job ="developer"  # updated 

x.job ="python developer"

print(x.job , "through obj")
print(x.a , "through obj")
print(x.b,"through obj")


# Instance variables : variables which are created for the objects 

# 2 ways to create instance variables 
# self.variablename = variablename
# obj.variablename = value 

# instance variables can be created through self parameter and can also be accessed by the all objects 
#instance variables can be created through objects and can also be accessed by the objects 
# instance variables created from one object can not be accessed by other object  


class demo:

    def __init__(self , a ,b):
        self.instancevar1 = a
        self.instancevar2 = b

o = demo(999,888)



o.instancevar3 ="sairam"
o.instancevar4 ="trainer"

print(o.instancevar1)
print(o.instancevar2)
print(o.instancevar3)
print(o.instancevar4)


o1 =demo(1111,2222)
print(o1.instancevar1)
print(o1.instancevar2)
print(o1.instancevar3)
print(o1.instancevar4)

'''

class demo1:

    def __init__(self , a ,b):
        self.instvar1 = a
        self.instvar2 = b

    def updatevar(self, newvalue):
        self.instvar1 = newvalue

    
ob = demo1(999,888)

ob.instvar1 = 7777  # with objects we can update the instance variables 
print(ob.instvar1)

#ob.updatevar(0)  # update the instance variable through self paramerter 
#print(ob.instvar1)

