class BankAccount:
    account_num = 0

    def __init__(self, balance):
        self.balance = balance
        BankAccount.account_num = BankAccount.account_num+1
        self.account_num = BankAccount.account_num

    def __str__(self):
        return "Account number: " + str(self.account_num) + "\nBalance: " + str(self.balance)

    def withdraw(self, amount):
        self. balance = self.balance - amount
        return self.balance

    def transfer(self, amount, other)
        self.withdraw(amount)
        other.lodge(amount)
        
    def lodge(self, amount):
        self. balance = self.balance + amount
        return self.balance


person1 = BankAccount(1000)

person2 = BankAccount(1500)
print(person1.__str__())
print(person2.__str__())


person2.withdraw(500)
person1.lodge(500)

print(person1.__str__())
print(person2.__str__())
