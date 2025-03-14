class AccountBalanceException(Exception):
    pass


balance = 10_000


def withdraw(amount):
    global balance

    minimum_balance = 5_000
    if amount > balance - minimum_balance:
        raise AccountBalanceException(f"Minimum balance should be {minimum_balance}")
    else:
        balance -= amount
        print(f"Withdrawing {amount} from account")
        print(f"Remaining balance: {balance - amount}")


if __name__ == "__main__":
    try:
        amount = int(input("Enter the amount to withdraw: "))
        withdraw(amount)
    except AccountBalanceException as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Error: {e}")
