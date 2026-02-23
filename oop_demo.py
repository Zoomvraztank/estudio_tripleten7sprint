class Account:
    def __init__(self,bank,acc_id,holder_id, balance=0.0):
        self.bank = bank
        self.acc_id = acc_id
        self.holder_id = holder_id
        self.balance = float(balance)

    def deposit(self, amount):
        self.balance += float(amount)
                              
    def withdraw(self, amount):
        self.balance -= float(amount)

first =Account ("old_trusty", "001", "10043", 500)
first.deposit(250)
first.withdraw(400)
print( first.balance) 