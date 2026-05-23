# Advance python 

# Decorators : it is callable that takes another function and returns modified callable 
# without arguments 
def sample_decorator(func):
    def demo():
        print("before excecution")
        func()
        print("after excecution")
    return demo

@sample_decorator
def sample():
    print("decorator implemented")
    print("training completed")
sample()

# with arguments 

def sample_decorator(func):
    def demo(args):
        print("before excecution")
        func(args)
        print("after excecution")
    return demo

@sample_decorator
def sample(args):
    print("decorator implemented")
    print("msg sent :",args)

sample("im superman")


# iterators :  
# __iter__() ---> returns iterator 
# __next__() ---> to fetch next value 


num =[10,22,37,67,89]
a = iter(num)

for i in range(5):
    print(next(a))


# Generators :  is a function which returns the iterator using yield keyword 

def numbers():
    yield 1
    yield 20

for num in numbers():
    print(num)



def gene():
    for i in range(10000):
        yield i

res=gene()

for i in range(10000):
    print(next(res))


# regular expression 

# sairam12345@gmail.com / outlook.in


# file handling 
# database ---> sql 
# web fundametals 
# flask 
