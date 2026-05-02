# OOPS ---> Object oriented programming system 


# approachs / paradigms 
# procedural paradigm --->
# functional paradigm --->
# object oriented paradigm --->

# in python each and everything is a object 

# class ----> is a blueprint to create the objects 

# object --> instance of class (by product)

# pen is a object  ---> properties ---> color , brand , model , price 
# behaviour --> it is used to write 

# object : attributes / variables 
# methods / functions 


# syntax 

class ClassOne: # class definition (methods , parameters/attributes)
    print("sairam")

c1=ClassOne()   #object creation 
print(c1)

class SampleClass:
    a =10 
    b =20

print(SampleClass.a)

obj = SampleClass()
print(obj.a)


obj1 = SampleClass()
obj1.a=100
print(obj1.a)


obj2 = SampleClass()
print(obj2.a)


class SampleClass1:
    def sample(self):
        print("demo method for class")

s1 =SampleClass1()
s1.sample()



