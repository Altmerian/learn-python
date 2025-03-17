class MinimumBalanceError(Exception):
    def __init__(self, balance: float):
        self.balance = balance

    def __str__(self):
        return "Balance is too low: " + str(self.balance)


class BankAccount:
    MINIMUM_BALANCE = 1000

    account_number = 1001

    def __init__(self, name: str, balance: float = 1000):
        if balance < BankAccount.MINIMUM_BALANCE:
            raise MinimumBalanceError(balance)
        self.name = name
        self.balance = balance
        self.account_number = BankAccount.account_number
        BankAccount.account_number += 1

    def deposit(self, amount: float):
        self.balance += amount

    def withdraw(self, amount: float):
        if self.balance - amount < BankAccount.MINIMUM_BALANCE:
            raise MinimumBalanceError(self.balance - amount)
        self.balance -= amount

    def show_details(self):
        print("Account Number:", self.account_number)
        print("Name:", self.name)
        print("Balance:", self.balance)


if __name__ == "__main__":
    account1 = BankAccount("John", 1000)
    account1.deposit(500)
    account1.withdraw(200)
    account1.show_details()

    print("Next account number:", BankAccount.account_number)

    try:
        account2 = BankAccount("Jane", 500)
        account2.deposit(500)
        account2.withdraw(200)
        account2.show_details()
    except MinimumBalanceError as e:
        print(e)

    print("Next account number:", BankAccount.account_number)

    try:    
        account3 = BankAccount("Jim", 1000)
        account3.deposit(500)
        account3.withdraw(2000)
        account3.show_details()
    except MinimumBalanceError as e:
        print(e)

    print("Next account number:", BankAccount.account_number)
