class BankAccount():
    #CONSTRUCTOR
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    def __str__(self):
        return "Account Desc\nOwner name : {}\nBalances : {}".format(self.owner, self.balance)
    # METHODS
    def deposit(self, amount):
        self.balance += amount
        print("{}$ is deposited at your acc".format(amount))
    def withdraw(self, amount):
        if amount > self.balance:
            print("Funds unavailable")
            return 0
        else:
            self.balance -= amount
            print("{}$ has been withdrawn from your acc".format(amount))
            return amount
myBankAcc1 = BankAccount("Jack", 1000)
print(myBankAcc1)
myBankAcc1.deposit(90)
print(myBankAcc1)
myBankAcc1.withdraw(900)
print(myBankAcc1)