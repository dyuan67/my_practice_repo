from bank_account import BankAccount

account1 = BankAccount("1234", 1000)
print(account1)
account1.deposit(1000)
print(account1)
account1.withdraw(2)
print(account1.get_balance())

account2 = BankAccount("1r2t3t", 10)
print(account2)
account2.withdraw(3)
account2.deposit(20000)
print(account2.get_balance())
