from abc import ABC, abstractmethod
from datetime import datetime


class Transaction:
    def __init__(self, transaction_type, amount):
        self.transaction_type = transaction_type
        self.amount = amount
        self.timestamp = datetime.now()

    def __str__(self):
        return (
            f"{self.timestamp:%d-%m-%Y %H:%M:%S} | "
            f"{self.transaction_type:<10} | ₹{self.amount}"
        )


class Account(ABC):
    def __init__(self, account_number, account_holder, balance=0):
        if balance < 0:
            raise ValueError("Initial balance cannot be negative")

        self.account_number = account_number
        self.account_holder = account_holder
        self.__balance = balance          # encapsulation
        self.transactions = []            # data structure: list

    @property
    def balance(self):
        return self.__balance

    def _update_balance(self, amount):
        """Protected helper method for subclasses."""
        self.__balance += amount

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")

        self._update_balance(amount)
        self.transactions.append(
            Transaction("Deposit", amount)
        )

    @abstractmethod
    def withdraw(self, amount):
        pass

    def view_transactions(self):
        if not self.transactions:
            print("No transactions found.")
            return

        for transaction in self.transactions:
            print(transaction)


class SavingsAccount(Account):
    def __init__(
        self,
        account_number,
        account_holder,
        balance,
        minimum_balance=1000
    ):
        super().__init__(account_number, account_holder, balance)
        self.minimum_balance = minimum_balance

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")

        if self.balance - amount < self.minimum_balance:
            print("Minimum balance requirement violated.")
            return

        self._update_balance(-amount)
        self.transactions.append(
            Transaction("Withdraw", amount)
        )


class CurrentAccount(Account):
    def __init__(
        self,
        account_number,
        account_holder,
        balance,
        overdraft_limit=5000
    ):
        super().__init__(account_number, account_holder, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")

        if self.balance - amount < -self.overdraft_limit:
            print("Overdraft limit exceeded.")
            return

        self._update_balance(-amount)
        self.transactions.append(
            Transaction("Withdraw", amount)
        )


class Bank:
    def __init__(self):
        self.accounts = {}      # data structure: dictionary

    def create_account(self, account):
        self.accounts[account.account_number] = account

    def find_account(self, account_number):
        return self.accounts.get(account_number)


if __name__ == "__main__":
    bank = Bank()

    savings = SavingsAccount(
        1001,
        "Harry",
        10000,
        minimum_balance=2000
    )

    current = CurrentAccount(
        1002,
        "Tom",
        5000,
        overdraft_limit=3000
    )

    bank.create_account(savings)
    bank.create_account(current)

    account = bank.find_account(1001)

    account.deposit(2000)
    account.withdraw(7000)

    print(f"Balance: ₹{account.balance}")

    print("\nTransaction History:")
    account.view_transactions()

    print("\nPolymorphism Demo")

    for account in bank.accounts.values():
        print(
            f"{account.account_holder}: "
            f"₹{account.balance}"
        )