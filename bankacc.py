import random

class Account:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

        self.__account_number = 67 #random.randint(10000000, 99999999)

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ${amount} to account #{self.__account_number}({self.name}). New balance: {self.balance}")
        return f"Deposited ${amount} to account #{self.__account_number}({self.name}). New balance: {self.balance}"

    def withdraw(self, amount):
        if 0 <= amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount} from account #{self.__account_number}({self.name}). New balance: {self.balance}")
            return f"Withdrew ${amount} from account #{self.__account_number}({self.name}). New balance: {self.balance}"
        elif amount < 0:
            print(f"u cant withdraw negative amount nice try. Current balance: {self.balance}")
            return f"u cant withdraw negative amount nice try. Current balance: {self.balance}"
        else:
            print(f"ur poor lollll. Current balance: {self.balance}")
            return f"ur poor lollll. Current balance: {self.balance}"

    def get_balance(self):
        print(self.balance)
        return self.balance

    def __str__(self):
        return f"Account({self.name}, Number: {self.__account_number}, Balance: {self.balance})"
    