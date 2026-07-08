
class Account:
    def __init__(self, name, account_number, balance=0):
        self.name = name
        self.balance = balance
        self.account_number = account_number

    def deposit(self, amount):
        if self.__checkinput(amount):
            if amount >= 0:
                self.balance += amount
                print(f"Deposited ${amount} to account #{self.account_number}({self.name}). New balance: {self.balance}")
                return self.balance
            else:
                print(f"u cant deposit negative amount nice try. Current balance: {self.balance}")
                return False
        else:
            return False

    def withdraw(self, amount):
        if self.__checkinput(amount):
            if 0 <= amount <= self.balance:
                self.balance -= amount
                print(f"Withdrew ${amount} from account #{self.account_number}({self.name}). New balance: {self.balance}")
                return self.balance
            elif amount < 0:
                print(f"u cant withdraw negative amount nice try. Current balance: {self.balance}")
                return False
            else:
                print(f"ur poor lollll. Current balance: {self.balance}")
                return False
        else:
            return False

    def __checkinput(self, input):
        if isinstance(input, (int, float)):
            return True
        else:
            print("Invalid input. Please enter a number or float.")
            return False

    def get_balance(self):
        print(f"balance for account #{self.account_number}({self.name}) is {self.balance}")
        return self.balance

    def __str__(self):
        return f"Account({self.name}, Number: {self.account_number}, Balance: {self.balance})"


class Bank:
    def __init__(self, accountsList):
        self.accounts = accountsList
        self.numAccounts = 0

    def addAccount(self, name, balance):
        self.numAccounts += 1
        account = Account(name, self.numAccounts, balance)
        self.accounts.append(account)
        return account

    # def removeAccount(self, account):
    #     if account in self.accounts:
    #         self.accounts.remove(account)
    #         return self.accounts
    #     else:
    #         print("Account not found.")
    #         return False