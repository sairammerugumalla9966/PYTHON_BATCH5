# Encapsulation in python : it is a process of wrapping data(variables) and methods in a single unit (class)
# and restricting  direct access to some data  

# data hiding : we protect important data from direct access 

# data security 
# controlled access 
# prevent accidental changes


# Access specifiers 
# public access specifiers
'''
class Parent:
    publicdata="sairam"
    def publicmethod(self):
        print(self.publicdata)

class Child(Parent):
    def method(self):
        print(self.publicdata)

obj=Parent()
obj.publicmethod() # sairam

obj1 = Child()
obj1.method()  # sairam
obj1.publicmethod()   # sairam
print(obj1.publicdata)  # sairam

'''

'''

# protected access specifiers :  {_} it can be accessed only by that class and subclass 

class Parent:
    _protecteddata="sairam"
    def _protectedmethod(self):
        print(self._protecteddata)

class Child(Parent):
    def method(self):
        print(self._protecteddata)


class Sample(Child):
    def demo(self):
        print(self._protecteddata)


obj=Parent()
obj._protectedmethod() # 


obj1 = Child()
obj1.method() 
# obj1.demo()

obj1._protectedmethod()   # 
print(obj1._protecteddata) 


obj1 = Child()
obj1.method()  # 
obj1._protectedmethod()   # 
print(obj1._protecteddata)  # 

'''

# private access specifiers : [__] double underscore before the data or methods 
# data can be accessed through the methods ,but not with objects 

'''
class Parent:
    __privatedata="sairam"
    def __privatedmethod(self):
        print(self.__privatedata)

class Child(Parent):
    def method(self):
        print(self.__privatedata)


obj=Parent()
obj.__privatedmethod() # sairam
print(obj.__privatedata)  # 
'''

# Data hiding : 

class Bank:
    __balance=50000
    def getBalance(self):
        return self.__balance

class API(Bank):
    def printBalance(self):
        return self.__balance
    

A=API()
print(A.getBalance())
print(A.printBalance())  #Error



    


