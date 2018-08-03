class Simple():
    def __init__(self, value):
        self.value = value

    def add_to_value(self, amount):
        self.value = self.value + amount



myob = Simple(300)
print(myob.value)
myob.add_to_value(50)
print(myob.value)






class Account():

    def __init__(self,owner,balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self,dep_amount):
        self.balance = self.balance + dep_amount
        print(f'Added {dep_amount} to the balance')

    def withdrawal(self,wd_amount):
        if self.balance >= wd_amount:
            self.balance = self.balance - wd_amount
            print("Withdrawal accepted!")
        else:
            print("Sorry, you do not have enough balance")

    def __str__(self):
        return f"\nOwner: {self.owner}\nBalance: {self.balance}"


a = Account('Ronald', 1000)
print(a)

print(a.owner)
print(a.balance)

print(a.deposit(1400))
print(a.withdrawal(45))
print(a.withdrawal(50000))
print(a)