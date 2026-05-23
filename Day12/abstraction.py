# Abstraction in python 
# abstraction means hiding internal inplimentation details and only showing the essential features to user.

# ATM 
# deposite 
# withdraw 
# balance 

# car 
# breaks 
# gears 

# Abstract class : a class which has one or more abstract methods ,then it is called as abstract class
# abstract method : if a method is declared without implementation logic , then it is called abstract method 
# for this abstract method with can not create objects ???

'''
class A:
    def method(self):
        pass

obj = A()
obj.method() #

'''
'''
from abc import ABC ,abstractmethod

class A(ABC):
    @abstractmethod
    def method(self):
        pass

obj = A()
obj.method() #
'''
# library ---> packages --> modules ---> classes ---> methods --> methods & variables 

# Concrete methods : normal methods inside a abstract class 


from abc import ABC ,abstractmethod

class A(ABC):

    @abstractmethod
    def method(self):
        pass

    def method1(self):
        print("this is concrete method")

    @abstractmethod
    def method2(self):
        pass


class B(A):
    def method(self):
        print("method is implemented in subclass")

    def method2(self):
        print("method2 is implemented in subclass")


obj = B()
obj.method()
obj.method1()
obj.method2() 



