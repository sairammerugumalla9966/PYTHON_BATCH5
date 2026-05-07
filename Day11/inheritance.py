# Inheritance : ability to access or use the methods and attributes of another class 
# parent class and child class 

# single inheritance 

class Parent:
    def method1(self):
        print("this is parent class method")



class Child(Parent): 
    def medtho2(self):
        print("this is child class method")

child = Child()
child.medtho2()

child.method1()

parent = Parent()
parent.method1()
#parent.method2()


# Multiple inheritance 
# a new class is created using two or more parent classes then it is called multiple inheritance 

class Father:
    name = "surya"
    def method1(self):
        print("this is fathers class method")


class Mother:
    def method2(self):
        print("this is mothers class method")


class Child1(Father,Mother): 
    def medtho3(self):
        print("this is child class method")


child1 = Child1()
child1.method1()
child1.method2()
child1.medtho3()
print(child1.name)


mother = Mother()
mother.method2()

father = Father()
father.method1()

# parents class have same method name , then which ever class is inherted first will be accessed 

class Father:
    name = "surya"
    def method1(self):
        print("this is fathers class method")


class Mother:
    def method1(self):
        print("this is mothers class method")


class Child1(Mother,Father): 
    def medtho3(self):
        print("this is child class method")


child1 = Child1()
child1.method1()

# child1.medtho3()
# print(child1.name)


# multi level inheritance : deriving a child class from a parent class and from that child class we create another child class.


class GrandParent:
    name = "surya"
    def show(self):
        print("this is grand parent class method")


class Parent(GrandParent):
    def demo(self):
        print("this is parent class method")


class Child2(Parent): 
    def display(self):
        print("this is child class method")

child2 = Child2()
child2.demo()

# herarical inheritance : one parent and multiple children 


class Parent:
    name = "surya"
    def show(self):
        print("this is parent class method")


class Son1(Parent):
    def demo(self):
        print("this is son 1 class method")


class Son2(Parent): 
    def display(self):
        print("this is child class method")

son1 = Son1()
son1.name
son1.display()

# Hybrid inheritance : combination of more than one type of inheritance 

class Parent:
    name = "surya"
    def show(self):
        print("this is parent class method")


class Son1(Parent):
    def demo(self):
        print("this is son 1 class method")


class Son2(Parent , Son1): 
    def display(self):
        print("this is child class method")

son1 = Son1()
son1.name
son1.display()



# ploymorphism : method overloading , method overriding 
# operator overloading 
# encapsulation 
# abstraction 
# access specifiers 









