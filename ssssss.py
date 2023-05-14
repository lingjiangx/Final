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
            'age': age
        }
        self.customers.append(customer)
        print("Customer created successfully. Customer ID:", customer_id)

    def save_customers_to_file(self):
        with open('customers.json', 'w') as file:
            json.dump(self.customers, file, indent=4)
        print("Customer information saved to customers.json.")


customer = Customer()


class Account:
    def __init__(self):
        self.accounts = []
        self.transactions = []

    def create_account(self, name, age):
        if age >= 18:
            account_type = "Checking Account"
        elif 14 < age < 18:
            account_type = "Saving Account"
        else:
            print("Age should be 15 or above to create an account.")
            return

        account_id = str(uuid.uuid4())[:8]  # Generate account ID

        account = {
            'account_id': account_id,
            'name': name,
            'age': age,
            'account_type': account_type

        }
        self.accounts.append(account)
        print("Account created successfully.")

    def save_accounts_to_file(self):
        with open('accounts.json', 'w') as file:
            json.dump(self.accounts, file, indent=4)
        print("Account details saved to accounts.json.")

    #  make a deposit
    def deposit(self, account_id, amount):
        try:
            with open('transactions.json', 'r') as file:
                transactions = json.load(file)
        except json.decoder.JSONDecodeError:
            transactions = []

        for transaction in transactions:
            if transaction['account_id'] != account_id:
                last_balance = 0
                new_balance = last_balance + amount


            elif transaction['account_id'] == account_id:
                last_balance = transaction["balance"]
                new_balance = last_balance + amount

            transaction_id = str(uuid.uuid4())[:8]  # Truncate UUID to 8 characters

            updated_transaction = {
                'transaction_id': transaction_id,
                'account_id': account_id,
                'deposit amount': amount,
                'balance': new_balance}

        self.transactions.append(updated_transaction)

        print(
            f"Transaction detail-transaction_id:{transaction_id}, account_id:{account_id},deposit amount:{amount},balance:{new_balance}")

        self.save_transactions_to_file()

    def save_transactions_to_file(self):
        with open('transactions.json', 'w') as file:
            json.dump(self.transactions, file, indent=4)
        print("Transaction made successfully.")

    # view transaction
    def view_transaction(self, account_id, transaction_id):
        with open('transactions.json', 'r') as file:
            transactions = json.load(file)

        for transaction in transactions:
            if transaction['account_id'] == account_id and transaction['transaction_id'] == transaction_id:
                print(transaction)
                break
            else:
                print("Transaction ID not found.")

    # withdraw
    def withdraw(self, account_id, amount):
        with open('accounts.json', 'r') as file:
            accounts = json.load(file)

        for account in accounts:
            if account['account_id'] == account_id:
                if account['account_type'] == "Checking Account":
                    return CheckingAccount.withdraw_from_checking(self, amount)
                elif account['account_type'] == "Saving Account":
                    return SavingAccount.withdraw_from_saving(self, amount)
        else:
            print("Unknown account type.")
            return False

    #
    # class CheckingAccount(Account):
    #     def __init__(self, account_id, customer_id, balance=0, credit_limit=-100):
    #         super().__init__(account_id, customer_id, balance)
    #         self.credit_limit = credit_limit
    #
    #     def withdraw_from_checking(self, amount):
    #         print("true")
    #         if self.balance - amount >= self.credit_limit:
    #             self.balance -= amount
    #             print("Withdrawal successful.")
    #             return True
    #         else:
    #             print("Insufficient funds.")
    #             return False

    # class SavingAccount(Account):
    #
    #     def __init__(self, account_id, customer_id, balance=0, monthly_withdrawals=1):
    #         super().__init__(account_id, customer_id, balance)
    #         self.monthly_withdrawals = monthly_withdrawals
    #
    #     def withdraw_from_saving(self, amount):
    #         print("true")
    #         if self.monthly_withdrawals > 0:
    #             self.balance -= amount
    #             self.monthly_withdrawals -= 1
    #             print("Withdrawal successful.")
    #             return True
    #         else:
    #             print("Monthly withdrawal limit exceeded.")
    #             return False

    # create account

    # delete account
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


account = Account()

while True:
    print("\n*** Bank Services Menu ***")
    print("1. Create Customer")
    print("2. Create Account")
    print("3. Deposit")
    print("4. Delete Account")
    print("5. View your transaction details")
    print("6. Withdraw")
    print("7. View balance")
    print("8. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter your name: ")
        age = int(input("Enter your age: "))
        customer.create_customer(name, age)
        customer.save_customers_to_file()

    elif choice == "2":
        name = input("Enter your name: ")
        age = int(input("Enter your age: "))
        Account.create_account(name, age)
        Account.save_accounts_to_file()

    elif choice == "3":
        account_id = input("Enter your account ID: ")
        amount = float(input("Enter deposit amount: "))
        account.deposit(account_id, amount)

    elif choice == "4":
        account_id = input("Enter your account ID: ")
        account.delete_account(account_id)

    elif choice == "5":
        account_id = input("Enter your account ID: ")
        transaction_id = input("Enter your transaction ID: ")
        account.view_transaction(account_id, transaction_id)

    elif choice == "6":
        account_id = input("Enter your account ID: ")
        amount = input("Enter your withdrawal amount: ")
        account.withdraw(account_id, amount)

    elif choice == "7":
        account_id = input("Enter your account ID: ")
        account.view_balance(account_id)




    elif choice == "8":
        break
    else:
        print("Invalid choice. Please try again.")



    def transfer_from_checking(self, account_id, amount, to_account_id):
        with open('transactions.json', 'r') as file:
            transactions = json.load(file)

        # new_balance_out = None
        # new_balance_in = None

        for transaction in transactions[::-1]:
            if transaction['account_id'] == account_id:
                last_balance = transaction['balance']
                if last_balance - amount >= -100.0:
                    new_balance_out = last_balance - amount
                    print(f"{new_balance_out} Transfer Out successful.")
                    transaction_id = str(uuid.uuid4())[:8]  # Truncate UUID to 8 characters
                    updated_transaction_out = {
                        'transaction_id': transaction_id,
                        'account_id': account_id,
                        'transferOut amount': amount,
                        'balance': new_balance_out
                    }
                    self.transactions.append(updated_transaction_out)
                    break
                else:
                    print("Insufficient funds.")
        else:
            print("Account ID not found.")
        self.save_transactions_to_file()

        for transaction in transactions[::-1]:
            if transaction['account_id'] == to_account_id:
                last_balance = transaction['balance']
                new_balance_in = last_balance + amount
                print(f"{new_balance_in} Transfer In successful.")
                transaction_id = str(uuid.uuid4())[:8]  # Truncate UUID to 8 characters
                updated_transaction_in = {
                    'transaction_id': transaction_id,
                    'account_id': to_account_id,
                    'transferIn amount': amount,
                    'balance': new_balance_in
                }
                self.transactions.append(updated_transaction_in)
                break
        else:
            print("Account ID not found.")

        print("Transaction detail")
        self.save_transactions_to_file()
