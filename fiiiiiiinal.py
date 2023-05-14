import json
import uuid


class Customer:
    def __init__(self):
        self.customers = []

    def create_customer(self, name, age):
        customer_id = str(uuid.uuid4())[:8]  # Truncate UUID to 8 characters
        customer = {
            'customer_id': customer_id,
            'name': name,
            'age': age,
            'balance': 0
        }
        self.customers.append(customer)
        print("Customer created successfully. Customer ID:", customer_id)

    def save_customers_to_file(self):
        with open('customers.json', 'w') as file:
            json.dump(self.customers, file, indent=4)
        print("Customer information saved to customers.json.")


customer = Customer()


class Account:
    def __init__(self, credit_limit=None):
        self.accounts = []
        self.transactions = []
        self.credit_limit = credit_limit

    def create_account(self, name, age):
        if age >= 18:
            account_type = "Checking Account"
        elif 14 < age < 18:
            account_type = "Saving Account"
        else:
            print("Age should be 15 or above to create an account.")
            return

        account_id = str(uuid.uuid4())[:8]  # Truncate UUID to 8 characters
        account = {
            'account_id': account_id,
            'name': name,
            'age': age,
            'account_type': account_type
        }
        self.accounts.append(account)
        print("Account created successfully. Account ID:", account_id)

    def save_accounts_to_file(self):
        with open('accounts.json', 'w') as file:
            json.dump(self.accounts, file, indent=4)
        print("account information saved to accounts.json.")

    def delete_account(self, account_id):
        with open('accounts.json', 'r') as file:
            accounts = json.load(file)

        for account in accounts.copy():
            if account['account_id'] == account_id:
                accounts.remove(account)

                with open('accounts.json', 'w') as file:
                    json.dump(accounts, file, indent=4)
                print("Account deleted successfully.")
                break

            else:
                print("Account ID not found.")

    def deposit(self, account_id, amount):
        try:
            with open('transactions.json', 'r') as file:
                transactions = json.load(file)
        except FileNotFoundError:
            transactions = []

        for transaction in transactions:
            if transaction['account_id'] == account_id:
                last_balance = transaction["balance"]
                new_balance = last_balance + amount
                break
        else:
            # No existing transaction found for the account ID
            last_balance = 0
            new_balance = last_balance + amount

        transaction_id = str(uuid.uuid4())[:8]  # Truncate UUID to 8 characters
        updated_transaction = {
            'transaction_id': transaction_id,
            'account_id': account_id,
            'deposit amount': amount,
            'balance': new_balance
        }

        self.transactions.append(updated_transaction)

        print(f"Transaction detail - transaction_id: {transaction_id}, account_id: {account_id}, "
              f"deposit amount: {amount}, balance: {new_balance}")

        self.save_transactions_to_file()

    def save_transactions_to_file(self):
        with open('transactions.json', 'w') as file:
            json.dump(self.transactions, file, indent=4)
        print("Transaction made successfully.")

    def view_all_transactions(self, account_id):
        with open('transactions.json', 'r') as file:
            transactions = json.load(file)

        for transaction in transactions:
            if transaction['account_id'] == account_id:
                print(transaction)

    def view_balance(self, account_id):
        with open('transactions.json', 'r') as file:
            transactions = json.load(file)

        for transaction in transactions[::-1]:
            if transaction['account_id'] == account_id:
                last_balance = transaction['balance']
                print(last_balance)
                break
            else:
                print("Please input valid Id or You don't have any transactions")

    def search_an_transaction(self, account_id, transaction_id):
        with open('transactions.json', 'r') as file:
            transactions = json.load(file)

        for transaction in transactions:
            if transaction['account_id'] == account_id and transaction['transaction_id'] == transaction_id:
                print(transaction)
                break
            else:
                print("Transaction ID not found.")

    def withdraw(self, account_id, amount):
        with open('accounts.json', 'r') as file:
            accounts = json.load(file)

        for account in accounts:

            if account['account_id'] == account_id:
                if account['account_type'] == "Checking Account":
                    CheckingAccount.withdraw_from_checking(self, account_id, amount)

                elif account['account_type'] == "Saving Account":
                    SavingAccount.withdraw_from_saving(self, account_id, amount)

                else:
                    print("Unknown account type.")


    def transfer(self, account_id, amount, to_account):
        with open('accounts.json', 'r') as file:
            accounts = json.load(file)

        for account in accounts:

            if account['account_id'] == account_id:
                if account['account_type'] == "Checking Account":
                    CheckingAccount.transfer_from_checking(self, account_id, amount, to_account)

                elif account['account_type'] == "Saving Account":
                    SavingAccount.transfer_from_saving(self, account_id, amount, to_account)

                else:
                    print("Unknown account type.")


class CheckingAccount(Account):
    def __init__(self, credit_limit):
        super().__init__()
        credit_limit = credit_limit

    def withdraw_from_checking(self, account_id, amount):
        with open('transactions.json', 'r') as file:
            transactions = json.load(file)

        for transaction in transactions[::-1]:
            if transaction['account_id'] == account_id:
                last_balance = transaction['balance']
                if last_balance - amount >= -100.0:
                    new_balance = last_balance - amount
                    print(f"{new_balance} Withdrawal successful.")
                    break
                else:
                    print("Insufficient funds.")
                    break
        else:
            print("Account ID not found.")

        transaction_id = str(uuid.uuid4())[:8]  # Truncate UUID to 8 characters

        updated_transaction = {
            'transaction_id': transaction_id,
            'account_id': account_id,
            'withdraw amount': amount,
            'balance': new_balance}

        self.transactions.append(updated_transaction)
        print(
            f"Transaction detail-transaction_id:{transaction_id}, account_id:{account_id},withdraw amount:{amount},balance:{new_balance}")
        self.save_transactions_to_file()




account = Account()

while True:
    print("\n*** Bank Services Menu ***")
    print("1. Create Customer")
    print("2. Create Account")
    print("4. Delete Account")
    print("3. Deposit")
    print("8. view all transactions")
    print("9. view balance")
    print("10. Search for a transaction")
    print("6. Withdraw")
    print("7. Transfer")


    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter your name: ")
        age = int(input("Enter your age: "))
        customer.create_customer(name, age)
        customer.save_customers_to_file()

    elif choice == "2":
        name = input("Enter your name: ")
        age = int(input("Enter your age: "))
        account.create_account(name, age)
        account.save_accounts_to_file()

    elif choice == "3":
        account_id = input("Enter your account ID: ")
        amount = float(input("Enter deposit amount: "))
        account.deposit(account_id, amount)

    elif choice == "4":
        account_id = input("Enter your account ID: ")
        account.delete_account(account_id)

    elif choice == "8":
        account_id = input("Enter your account ID: ")
        account.view_all_transactions(account_id)

    elif choice == "9":
        account_id = input("Enter your account ID: ")
        account.view_balance(account_id)

    elif choice == "10":
        account_id = input("Enter your account ID: ")
        transaction_id = input("Enter your transaction ID: ")
        account.search_an_transaction(account_id, transaction_id)

    elif choice == "6":
        account_id = input("Enter your account ID: ")
        amount = float(input("Enter your withdraw amount: "))
        account.withdraw(account_id, amount)

    elif choice == "7":
        account_id = input("Enter your account ID: ")
        amount = float(input("Enter your transfer amount: "))
        to_account_id = input("Enter your To account ID: ")
        account.transfer(account_id, amount, to_account_id)










    elif choice == "8":
        break
    else:
        print("Invalid choice. Please try again.")
