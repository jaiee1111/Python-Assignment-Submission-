
class bankaccount :
    def __init__(self, acc_no, balance):
        self.acc_no = acc_no
        self.balance = balance
        
    def deposit(self, amount):
        self.balance +=amount
        print("amount deposited:",amount)
        
    def withdrow(self, amount):
        if 0<amount <= self.balance:
            self.balance -=amount
            print("amount withdrowed",amount)
        elif amount>self.balance:
            print ("insufficient balance")
        else:
            print("insufficient balance")
            
    def check_balance(self):
        print("account{self.account_number}balance:{self.balance}")
  
# explain usage
account = bankaccount("123456789",500.00)

# perform opretions  
account.check_balance() 
account.deposit(2000)
account.withdrow(1500)
account.check_balance()
    