class BankAccount:
    def __init__(self, account_holder=0, balance=0):
        self.account_holder = account_holder
        self._balance = balance
    def deposit(self, amount):
        self._balance += amount
    def display_balance(self):
        print("Balance:", self._balance)
class SavingsAccount(BankAccount):
    def __init__(self, account_holder, balance, interest_rate):
        super().__init__(account_holder, balance)
        self.interest_rate = interest_rate
    def add_interest(self):
        self._balance += self._balance * self.interest_rate
account1 = SavingsAccount("John", 1000, 0.05)
account1.deposit(500)
account1.add_interest()
account1.display_balance()  
print(account1.account_holder)  
print(account1._balance)  
print(account1.interest_rate)  


        