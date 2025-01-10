class BankAccount:
    def __init__(self, owner, initial_balance):
        self.owner = owner
        self.balance = initial_balance

    def deposit(self, amount):
        self.balance += amount
        return f"{self.owner} has deposited {amount}. {self.owner} your new balance is {self.balance}."

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return f"{self.owner} has withdrew {amount}. {self.owner} your new balance is {self.balance}."
        else:
            return "Insufficient funds."


account1 = BankAccount("Carlos", 1000)
account2 = BankAccount("Alejandro", 200)


print(account1.withdraw(200))
print(account2.deposit(100))
