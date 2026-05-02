# Constructor / (__init__) method :

# a method is declared in a class , it will be excecuted automatically when an object is created 

'''
def __init__(self ,paramter1 , perameter2 ):
    self.parameter1 = parameter 
    self.parameter2 = parameter 

'''

class ConstructorClass:
    def __init__(self):
        print("method excecutes automatically")

obj=ConstructorClass()

#########################################################

class BankAccount:
    def __init__(self , acno , name , ifsccode,balance):
        self.acno = acno
        self.name=name
        self.ifsccode=ifsccode
        self.balance=balance

    def display(self):
        print(self.acno ,self.name , self.ifsccode, self.balance)

obj1=BankAccount(101511007788 ,"sairam","BNK125", 100000)
obj1.display()


obj1=BankAccount(101511007781 ,"prasad","BNK125", 1000000)
obj1.display()

# obj3 =BankAccount()  ---> error 
# obj1.display()


class BankAccount1:
    def __init__(self , acno , name , ifsccode,balance):
        self.acno = acno
        self.name=name
        self.ifsccode=ifsccode
        self.balance=balance

    def withdraw(self,amount):
        self.balance -= amount


    def deposite(self,amount):
        self.balance += amount

    def checkbalance(self):
        print(self.balance)

obj9 = BankAccount1(101511007783 ,"ram","BNK125", 10000)
obj9.checkbalance()

obj9.withdraw(5000)
obj9.checkbalance()






