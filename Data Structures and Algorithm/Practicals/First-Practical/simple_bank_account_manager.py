def deposit(account, amount):
    account_number, balance = account
    balance += amount
    updated_account = (account_number, balance)
    return updated_account

def withdraw(account, amount):
    account_number, balance = account
    balance -= amount
    updated_account = (account_number, balance)
    return updated_account
