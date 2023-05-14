class Account:
    def __init__(self, name, age, account_id, account_type, balance):
        self.name = name
        self.age = age
        self.account_id = account_id
        self.account_type = account_type
        self.balance = balance

    def deposit_money(self, amount):
        self.balance += amount
        self.transaction_history.append(f"Deposit: +${amount}, Balance: ${self.balance}")

# create a new account object
new_account = Account("John", 30, "123456", "Checking Account", 39.0)

# deposit money into the account
new_account.deposit_money(100.0)

# check the new balance
print(new_account.balance)



class SavingsAccount:
    def __init__(self, account_id: int, name, age, account_type: "", balance: int):
        self.name = name
        self.age = age
        self.account_type = account_type
        self.balance = balance
        self.account_id = account_id

    def withdraw_money(self, amount):
        if amount > self.balance:
            print("Insufficient balance.")
        else:
            self.balance -= amount
            # print(f"Withdrawal of {amount} successful. New balance: {self.balance}")

    def __str__(self):
        return f"{self.account_id}, {self.name}, {self.age}, {self.account_type}, {self.balance}"


#  add addtional feature: if withdrawal or transfer time = 0, if it is, you can proceed. elif time = 1, break.

class CheckingAccount:
    def __init__(self, account_id: int, name, age, account_type: ""):
        self.name = name
        self.age = age
        self.account_type = account_type
        self.account_id = account_id

    def __str__(self):
        return f"{self.account_id},{self.name},{self.age},{self.account_type},{self.balance}"


#  add addtional feature: negative blance > -100

def create_savingsaccounts():  # <18
    # create new customers with the generated account IDs
    with open("accounts.txt", "r") as file:
        lines = file.readlines()
        print(lines)
        last_id = lines[-1].split(",")[0]  # retrieve the last line
        print(last_id)
        account_id = int(last_id) + 1
        print(account_id)

        account_type = "Savings Account"
        balance = 0
        new_customer = SavingsAccount(account_id, name, age, account_type, balance)
    with open("accounts.txt", "a") as file:
        file.write(str(new_customer) + "\n")
    print(f"Hello,{name}, A Savings Account created for you successfully, your account ID is {account_id}")


def create_checkingaccounts():  # >18
    # create new customers with the generated account IDs
    with open("accounts.txt", "r") as file:
        lines = file.readlines()
        print(lines)
        last_id = lines[-1].split(",")[0]  # retrieve the last line
        print(last_id)
        account_id = int(last_id) + 1
        print(account_id)

        account_type = "Checking Account"
        balance = 0
        new_customer = CheckingAccount(account_id, name, age, account_type, balance)
    with open("accounts.txt", "a") as file:
        file.write(str(new_customer) + "\n")
    print(f"Hello,{name}, A Checking Account created for you successfully, your account ID is {account_id}")


def delete_accounts():
    with open("accounts.txt", "r") as file:
        lines = file.readlines()
        account_id = input("Enter your account ID: ")
        # Find the line with the given account ID and remove it
        for i, line in enumerate(lines):
            if line.startswith(f"{account_id},"):
                del lines[i]
                break  # stop searching after the line is deleted
        # Write the modified lines back to the file
        with open("accounts.txt", "w") as file:
            file.writelines(lines)
    print(f"Your account(ID:{account_id}) has been deleted successully")


def view_balance():
    account_id = input("Enter your account ID: ")
    with open("accounts.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            if line.startswith(f"{account_id},"):
                parts = line.strip().split(",")
                print(f'{parts[0]: <15}{parts[1]: <15}{parts[2]: <5}{parts[3]: <25}{parts[4]}')
                balance = line.split(",")[-1]
                print(f"Your balance is {balance}")
                break


# after you do the deposit, then update the transaction to the database


def deposit_money():
    account_id = input("Enter your account ID: ")
    transaction_type = "deposit"
    amount = float(input("Enter the amount to deposit: "))

    # update the account file with the new balance
    with open("accounts.txt", "r+") as file:
        lines = file.readlines()
        file.seek(0)  # reset the file pointer to the beginning
        for line in lines:
            if line.startswith(f"{account_id},"):
                values = line.strip().split(",")
                old_balance = float(values[-1])
                new_balance = old_balance + amount
                values[-1] = str(new_balance)
                updated_line = ",".join(values) + "\n"
                file.write(updated_line)
                print(f"Your deposit amount is {amount}, and your new balance is {new_balance}.")
            else:
                file.write(line)
        file.truncate()  # truncate the file in case the new content is shorter than the old content

    # update transaction history,
    with open("accountsTransactions.txt", "r+") as file:
        lines = file.readlines()
        file.seek(0)  # reset the file pointer to the beginning
        print(lines)
        last_tran_id = lines[-1].split(",")[1]  # retrieve the last line
        print(last_tran_id)
        new_tran_id = int(last_tran_id) + 1
        print(new_tran_id)

        for line in lines:
            if line.startswith(f"{account_id},"):
                values = line.strip().split(",")
        print(values)
        print(values[-1])

        old_balance = float(values[-1])
        new_balance = old_balance + amount
        print(new_balance)
    with open("accountsTransactions.txt", "a") as file:
        file.write(str(f"{account_id},{new_tran_id}, {transaction_type},{amount},{new_balance}") + "\n")


def withdraw_money():
    account_id = input("Enter your account ID: ")
    transaction_type = "withdrawal"
    amount = float(input("Enter the amount to withdraw: "))

    # update the account file with the new balance
    with open("accounts.txt", "r+") as file:
        lines = file.readlines()
        file.seek(0)  # reset the file pointer to the beginning
        for line in lines:
            if line.startswith(f"{account_id},"):
                balance = float(line.split(",")[-1])
                print(balance)
                if "Checking" in line:
                    print("This line contains a checking account")


# def view_transactions_and_balance():
#     account_id = input("Enter your account ID: ")
#     with open("accountsTransactions.txt", "r") as file:
#         lines = file.readlines()
#         print("Account ID Transaction ID Date Transaction Type Amount Balance")
#         for line in lines:
#             if line.startswith(f"{account_id},"):
#                 print(line)
# for line in lines:
#     if line.startswith(f"{account_id},"):
#         account_info = line.strip().split(", ")
#         balance = account_info[-1]
#         transaction_history = account_info[4:-1]
#         print(f"Transaction history for account {account_id}: {transaction_history}")
#         print(f"Current balance: {balance}")
#         return
#
# print(f"No account found with ID {account_id}")


# user interface command lines

while True:
    print("Welcome to the bank!")
    print("What would you like to do?")
    print("1. Create a new account")
    print("2. View balance")
    print("3. View transactions")
    print("4. Withdraw money")
    print("5. Deposit money")
    print("6. Delete account")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter your name: ")
        age = int(input("Enter your age: "))
        if age >= 18:
            create_checkingaccounts()
        elif 14 < age < 18:
            create_savingsaccounts()
        else:
            print("You can only create an account if you are older than 14 years old")


    elif choice == "2":
        view_balance()

    elif choice == "3":
        view_transactions_and_balance()

    elif choice == "4":
        withdraw_money()

    elif choice == "5":
        deposit_money()

    elif choice == "6":
        delete_accounts()

    elif choice == "7":
        print("Thank you for banking with us!")
        break

    else:
        print("Invalid choice. Please try again.")
