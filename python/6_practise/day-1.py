class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
class inSufficirent_BalanceError:
    pass

class Account(Person):
    def __init__(self, name, age, account_number, Balance):
        super().__init__(name, age)
        self.account_number = account_number
        self.Balance = 0
    def deposit(self,amount):
        self.Balance+= amount
        return self.Balance
    
    def withdraw(self, amount):
        if self.Balance <= amount:
            raise inSufficirent_BalanceError("Insufficient Balance")
        else:
            self.Balance -= amount
    def __str__(self):
        return f"{self.name} | Balance:{self.Balance}"
    
class Bank:
    bank_name = "ABC Bank"

    @classmethod
    def change_bank_name(cls, new_name):
        cls.bank_name = new_name

Bank.change_bank_name("XYZ Bank")
print(Bank.bank_name)
