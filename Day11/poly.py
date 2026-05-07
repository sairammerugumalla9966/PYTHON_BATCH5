
# polymorphism : ploy --> many ,  morphs ---> forms

# operator overloading : an opertaor performing differently in different cases 

# '+'  ---> if use between intergers the it is called addition operator 
# '+'  ---> if use between strings or lists then it is called concatination operator 

print(10+20) # 30 
print("hi" + "prasad") # hi prasad 

l1 =[1,2,3]
l2 = [4,5,6]
l =l1+l2
print(l)


# * --> multiplication 
# * ---> repitation 
# *args --->packing and unpacking arguments 


# polymorphism in methods / functions  : if a method handles more than one datatype and different parameters , then it is called polymorphism

print("sairam",12)
print(99.00)


def sum(*args):
    if args:
        var=type(args[0])()
        print(var)
    for i in args:
        var+=1
    return var 

print(sum(12,"sairam" ,99.00, True))



# method overriding : 

class parent:
    def method55(self):
        print("this is parent class")


class child(parent):
    def method55(self):
        print("this is child class")

ch =child()
ch.method55()   # run time 


# method overloading :if a class contains more that one method with same name and methods contain differnt datatypes
# or parameters or differnt no of parameters or both is called method overloading 
