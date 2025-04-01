class Accout:
    def __init__(self,bal,acc):
        self.balance=bal
        self.account=acc
    
    #debit method 

    def debit(self,amount):
        self.balance-=amount
        print("Rs ",amount,"was debited..")
        print("Total balace is :",self.get_balance())

    def credit(self,amount):
        self.balance+=amount
        print("Rs ",amount,"was credited..")
        print("Total balace is :",self.get_balance())
        
    def get_balance(self):
        return self.balance

    
acc1=Accout(10000,12345)
acc1.credit(500)      
acc1.credit(1000)      
acc1.debit(6000)      