import uuid
import datetime
import os


class Account:
    def __init__(self, account_id):
        self.account_id = account_id

    def delete_accounts(self):
        with open("accounts.txt", "r") as file:
            lines = file.readlines()

            # Find the line with the given account ID and remove it
            for i, line in enumerate(lines):
                if line.startswith(f"{account_id},"):
                    del lines[i]
                    break  # stop searching after the line is deleted
            # Write the modified lines back to the file
            with open("accounts.txt", "w") as file:
                file.writelines(lines)
        print(f"Your account(ID:{account_id}) has been deleted successully")

    def view_balance(self):
        with open('accountsTransactions.txt', 'r') as f:
            lines = f.readlines()
        for line in lines:
            fields = line.strip().split(',')
            if fields[0] == self.account_id:
                balance = float(fields[5])
        print(f"Current balance for account {self.account_id}: {balance}")



    def deposit(self, amount: float):
        if amount <= 0:
            raise ValueError("Amount must be positive.")
        now = datetime.datetime.now()
        transaction_id = str(uuid.uuid4())[:8]
        with open('accountsTransactions.txt', 'r') as f:
            lines = f.readlines()
            for line in lines:
                fields = line.strip().split(',')
                if fields[0] == self.account_number:
                    balance = float(fields[5])
                    balance += amount
        with open('accountsTransactions.txt', 'a') as f:
            f.write(f'{self.account_number},{transaction_id}, {now}, Deposit, {amount},{balance}\n')
            new_transaction = f'account number: {self.account_number},transaction ID: {transaction_id}, {now},Deposit amount: {amount},balance:{balance}\n'
            print(new_transaction)


# checking account >18
class CheckingAccount:
    def __init__(self, account_id, account_type):
        self.account_id = account_id
        self.account_type = account_type


    def create_account(self):
        with open("accounts.txt", "r") as file:
            lines = file.readlines()
            last_id = lines[-1].split(",")[0]  # retrieve the last line
            account_id = int(last_id) + 1
            account_type = "Checking Account"
            new_account = f"{account_id},{name},{age},{account_type}"

        with open("accounts.txt", "a") as file:
            file.write(str(new_account) + "\n")
        print(f"Hello,{name}, A Checking Account created for you successfully, your account ID is {account_id}")



    def withdraw(self, amount: float):
        with open("accountsTransactions.txt", "r+") as f:
            lines = f.readlines()
            # reset the file pointer to the beginning
            f.seek(0)
            for line in lines:
                if line.startswith(f"{account_id},"):
                    last_line = lines[-1].strip()  # remove any trailing whitespace
                    last_balance = float(last_line.split(",")[-1])
                    print(last_balance)
                    # assumption: the credit limit can be negative = -100
                    if last_balance - amount > -100:
                        last_balance -= amount
                    else:
                        print("Insufficient balance")
                        break
        # update the database
        now = datetime.datetime.now()
        transaction_id = str(uuid.uuid4())[:8]
        with open('accountsTransactions.txt', 'a') as f:
            f.write(f'{self.account_id},{transaction_id}, {now}, Withdrawal, {amount},{last_balance}\n')
            new_transaction = f'account ID: {self.account_id},transaction ID: {transaction_id}, {now},Withdrawal amount: {amount},balance:{last_balance}\n'
            print(new_transaction)

    def transfer(self, amount: float, account_id, to_account_id):
        with open("accountsTransactions.txt", "r+") as f:
            lines = f.readlines()
            # reset the file pointer to the beginning
            f.seek(0)
            # for line in lines:
            #     if line.startswith(f"{account_id},"):
            #         print(lines)
            #         last_line = lines[-1].strip()  # remove any trailing whitespace
            #         print(last_line)
            #         last_balance = float(last_line.split(",")[-1])
            #         print(last_balance)
            #         last_balance -= float(amount)

            for line in lines:
                if line.startswith(f"{account_id},"):
                    fields = line.strip().split(',')
                    if fields[0] == self.account_id:
                        balance = float(fields[5])
                        balance -= amount
            now = datetime.datetime.now()
            transaction_id = str(uuid.uuid4())[:8]
            with open('accountsTransactions.txt', 'a') as f:
                f.write(f'{self.account_id},{transaction_id}, {now}, Deposit, {amount},{balance}\n')
                new_transaction = f'account number: {self.account_id},transaction ID: {transaction_id}, {now},Deposit amount: {amount},balance:{balance}\n'
                print(new_transaction)

            # for line in lines:
            #     if line.startswith(f"{to_account_id},"):
            #         last_line = lines[-1].strip()  # remove any trailing whitespace
            #
            #         last_balance = float(last_line.split(",")[-1])
            #
            #         last_balance += float(amount)

        # update database
        # now = datetime.datetime.now()
        # transaction_id = str(uuid.uuid4())[:8]
        # with open('accountsTransactions.txt', 'a') as f:
        #     f.write(f'{self.account_id},{transaction_id}, {now}, TransferOut, {amount},{last_balance}\n')
        #     f.write(f'{self.to_account_id},{transaction_id}, {now}, TransferIn, {amount},{last_balance}\n')
        #     new_transaction1 = f'account number: {self.account_id},transaction ID: {transaction_id}, {now},TransferOut amount: {amount},balance:{last_balance}\n'
        #     new_transaction2 = f'account number: {self.to_account_id},transaction ID: {transaction_id}, {now},TransferIn amount: {amount},balance:{last_balance}\n'
        #     print(new_transaction1)
        #     print(new_transaction2)


    # savings account <18


class SavingsAccount:
    def __init__(self, account_id, account_type):
        self.account_type = account_type
        self.account_id = account_id

    def create_account(self):
        with open("accounts.txt", "r") as file:
            lines = file.readlines()
            last_id = lines[-1].split(",")[0]  # retrieve the last line
            account_id = int(last_id) + 1
            account_type = "Savings Account"
            new_customer = f"{account_id},{name},{age},{account_type}"

        with open("accounts.txt", "a") as file:
            file.write(str(new_customer) + "\n")
        print(f"Hello,{name}, A Checking Account created for you successfully, your account ID is {account_id}")

    def withdraw(self, amount: float):
        with open("accountsTransactions.txt", "r+") as f:
            lines = f.readlines()
            # reset the file pointer to the beginning
            f.seek(0)

            for line in lines:
                if line.startswith(self.account_id):
                    last_line = lines[-1].strip()  # remove any trailing whitespace
                    last_balance = last_line.split(",")[-1]

                    fields = line.split(",")
                    datetime_field = fields[2]
                    date = datetime_field[:8]  # Extract the year and month (YYYY-MM) from the datetime field

                    today = datetime.date.today()
                    today_str = today.strftime('%Y-%m')

            if float(amount) > float(last_balance):
                print("Insufficient balance. Withdrawal cancelled.")
            else:
                if str(date.strip()) == str(today_str.strip()):
                    if "Withdrawal" or "Transfer" in line == True:
                        print("Withdrawal already made this month. Try again next month.")


                    else:
                        self.balance -= amount
                        f.write(f'{self.account_number},{transaction_id},{now},"Withdrawal",{amount},{self.balance}\n')
                        print(f"Withdrawal successful. New balance: {self.balance}")

        # # update the database
        now = datetime.datetime.now()
        transaction_id = str(uuid.uuid4())[:8]
        with open('accountsTransactions.txt', 'a') as f:
            f.write(f'{self.account_id},{transaction_id}, {now}, Withdrawal, {amount},{last_balance}\n')
            new_transaction = f'account ID: {self.account_id},transaction ID: {transaction_id}, {now},Withdrawal amount: {amount},balance:{last_balance}\n'
            print(new_transaction)

class Customer:
    def __init__(self, name):
        self.name = name
        self.account_id = account_id
        self.age = age

    def create_customer(self):
        with open("customers.txt", "r") as file:
            lines = file.readlines()
            for line in lines:
                if name in line:

            last_id = lines[-1].split(",")[0]  # retrieve the last line
            customer_id = int(last_id) + 1

            new_customer = f"{customer_id},{name},{age},{account_type}"

        with open("accounts.txt", "a") as file:
            file.write(str(new_account) + "\n")
        print(f"Hello,{name}, A Checking Account created for you successfully, your account ID is {account_id}")



# user interface command lines

while True:
    print("Welcome to the bank!")
    print("What would you like to do?")
    print("1. Create a new account")
    print("2. View balance")
    print("3. Withdraw money")
    print("4. Deposit money")
    print("5. Transfer money")
    print("6. Delete account")

    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter your name: ")
        age = int(input("Enter your age: "))
        customer = Customer(name)
        customer.create_customer()
        if age >= 18:
            my_account = CheckingAccount(name, age)
            my_account.create_account()
        elif 14 < age < 18:
            my_account = SavingsAccount(name, age)
            my_account.create_account()
        else:
            print("You can only create an account if you are older than 14 years old")

    elif choice == "2":
        account_id = input("enter id")
        my_account = Account(account_id)
        my_account.view_balance()

    elif choice == "3":
        account_id = input("enter account ID")
        account_type = input("enter account type: Checking or Savings")
        amount = input("enter withdrawal amount")

        if account_type == "Checking":
            my_account = CheckingAccount(account_id, account_type)
            my_account.withdraw(amount)
        elif account_type == "Savings":
            my_account = SavingsAccount(account_id, account_type)
            my_account.withdraw(amount)



    elif choice == "4":
        account_id = input("enter id")
        amount = float(input("enter amount"))
        my_account = Account(account_id)
        my_account.deposit(amount)



    elif choice == "5":
        account_id = input("enter your account ID")
        account_type = input("enter account type: Checking or Savings")
        amount = input("enter transfer amount")
        to_account_id = input("enter the account ID you are goign to transfer to")

        if account_type == "Checking":
            my_account = CheckingAccount(account_id, account_type)
            my_account.transfer(amount,account_id,to_account_id)
        elif account_type == "Savings":
            my_account = SavingsAccount(account_id, account_type)
            my_account.transfer(amount,account_id, to_account_id)

    elif choice == "6":
        account_id = input("enter your account id")
        my_account = Account(account_id)
        my_account.delete_accounts()


    elif choice == "7":
        print("Thank you for banking with us!")
        break

    else:
        print("Invalid choice. Please try again.")
