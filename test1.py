import os


class Account:
    def __init__(self, acc_id, customer_id, balance=0):
        self.acc_id = acc_id
        self.customer_id = customer_id
        self.balance = balance
        self.transactions = []

    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(('deposit', amount))

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            self.transactions.append(('withdraw', amount))
            return True
        else:
            return False

    def transfer(self, amount, to_account):
        if self.balance >= amount:
            self.balance -= amount
            to_account.balance += amount
            self.transactions.append(('transfer', amount, to_account.acc_id))
            return True
        else:
            return False

    def __str__(self):
        return f"Account {self.acc_id}: balance={self.balance}"


class SavingsAccount(Account):
    MAX_WITHDRAWALS_PER_MONTH = 1

    def __init__(self, acc_id, customer_id, balance=0):
        super().__init__(acc_id, customer_id, balance)
        self.withdrawals_this_month = 0

    def withdraw(self, amount):
        if self.withdrawals_this_month < self.MAX_WITHDRAWALS_PER_MONTH:
            result = super().withdraw(amount)
            if result:
                self.withdrawals_this_month += 1
            return result
        else:
            return False

    def transfer(self, amount, to_account):
        return False

    def __str__(self):
        return f"Savings Account {self.acc_id}: balance={self.balance}"


class CheckingAccount(Account):
    CREDIT_LIMIT = -1000

    def __init__(self, acc_id, customer_id, balance=0):
        super().__init__(acc_id, customer_id, balance)

    def __str__(self):
        return f"Checking Account {self.acc_id}: balance={self.balance}"


class Customer:
    def __init__(self, cust_id, name, age):
        self.cust_id = cust_id
        self.name = name
        self.age = age
        self.accounts = []

    def add_account(self, account):
        self.accounts.append(account)

    def delete_account(self, account):
        self.accounts.remove(account)

    def __str__(self):
        return f"Customer {self.cust_id}: {self.name}, {self.age} years old"


import os


class Bank:
    def __init__(self):
        self.customers = []
        self.accounts = []
        self.transactions = []

    def load_data(self):
        # Load customers data
        with open(os.path.join(os.getcwd(), "customers.txt"), "r") as f:
            for line in f:
                cust_id, name, age = line.strip().split(",")
                self.customers.append(Customer(cust_id, name, int(age)))

        # Load accounts data
        with open(os.path.join(os.getcwd(), "accounts.txt"), "r") as f:
            for line in f:
                acc_id, cust_id, acc_type, balance = line.strip().split(",")
                acc = None  # Initialize acc to None
                if acc_type == "checking":
                    acc = CheckingAccount(acc_id, self.get_customer(cust_id), float(balance))
                elif acc_type == "savings":
                    acc = SavingsAccount(acc_id, self.get_customer(cust_id), float(balance))
                if acc is not None:  # Only append to self.accounts if acc was assigned a value
                    self.accounts.append(acc)

        # Load transactions data
        with open(os.path.join(os.getcwd(), "accountTransactions.txt"), "r") as f:
            for line in f:
                # acc_id, trans_id, date, trans_type, amount, balance = line.strip().split(",")
                if trans_type == "deposit":
                    trans = Deposit(float(amount))
                elif trans_type == "withdraw":
                    trans = Withdrawal(float(amount))
                elif trans_type == "transfer":
                    trans = Transfer(float(amount), self.get_account(acc_id))
                trans.trans_id = trans_id
                self.get_account(acc_id).transactions.append(trans)
                self.transactions.append(trans)

    def save_data(self):
        # Save customers data
        with open(os.path.join(os.getcwd(), "customers.txt"), "w") as f:
            for cust in self.customers:
                f.write("{},{},{}\n".format(cust.cust_id, cust.name, cust.age))

        # Save accounts data
        with open(os.path.join(os.getcwd(), "accounts.txt"), "w") as f:
            for acc in self.accounts:
                f.write("{},{},{},{}\n".format(acc.acc_id, acc.customer_id, acc.acc_type, acc.balance))

        # Save transactions data
        with open(os.path.join(os.getcwd(), "accountTransactions.txt"), "w") as f:
            for trans in self.transactions:
                f.write("{},{},{},{}\n".format(trans.trans_id, trans.account_id, trans.trans_type, trans.amount))

    def get_customer(self, cust_id):
        for cust in self.customers:
            if cust.cust_id == cust_id:
                return cust

            return None

    def get_account(self, acc_id):
        for acc in self.accounts:
            if acc.acc_id == acc_id:
                return acc
        return None

    def create_customer(self, name, age):
        cust_id = len(self.customers) + 1
        cust = Customer(cust_id, name, age)
        self.customers.append(cust)
        return cust

    def create_account(self, customer_id, acc_type):
        cust = self.get_customer(customer_id)
        if cust is None:
            return None
        acc_id = len(self.accounts) + 1
        if acc_type == "savings":
            acc = SavingsAccount(acc_id, cust.cust_id)
        else:
            acc = CheckingAccount(acc_id, cust.cust_id)
        cust.add_account(acc)
        self.accounts.append(acc)
        return acc

    def view_transactions(self, acc_id):
        acc = self.get_account(acc_id)
        if acc is None:
            return None
        return acc.transactions

    def view_balance(self, acc_id):
        acc = self.get_account(acc_id)
        if acc is None:
            return None
        return acc.balance

    def perform_operation(self, acc_id, operation, amount=None, to_acc_id=None):
        acc = self.get_account(acc_id)
        if acc is None:
            return False
        if operation == "deposit":
            acc.deposit(amount)
        elif operation == "withdraw":
            acc.withdraw(amount)
        elif operation == "transfer":
            to_acc = self.get_account(to_acc_id)
            if to_acc is None:
                return False
            acc.transfer(amount, to_acc)
        else:
            return False
        return True

    def delete_account(self, acc_id):
        acc = self.get_account(acc_id)
        if acc is None:
            return False
        cust = self.get_customer(acc.customer_id)
        if cust is None:
            return False
        cust.remove_account(acc)
        self.accounts.remove(acc)
        return True


# Create a Bank instance and load data from files
bank = Bank()
bank.load_data()

# Create a new customer and account
cust = bank.create_customer("John Doe", 25)
acc = bank.create_account(cust.cust_id, "checking")
#
# # Perform some transactions
# acc.deposit(1000)
# acc.withdraw(500)
# acc.transfer(250, bank.create_account(cust.cust_id, "savings"))
#
# # Print account balance and transactions
# print("Account balance:", bank.view_balance(acc.acc_id))
# print("Account transactions:", bank.view_transactions(acc.acc_id))
#
# # Delete the account
# bank.delete_account(acc.acc_id)
#
# # Save data to files
# bank.save_data()
