# Banking System
# Console-based Banking System to manage user accounts and transactions

import os
from datetime import datetime

# File names
ACCOUNTS_FILE = "accounts.txt"
TRANSACTIONS_FILE = "transactions.txt"

def create_account():
    print("\nCreating a new account...")
    name = input("Enter your name: ").strip()
    balance = float(input("Enter your initial deposit: "))
    password = input("Enter a password: ").strip()

    # Generate a unique account number
    account_number = generate_account_number()

    # Save account details
    with open(ACCOUNTS_FILE, "a") as file:
        file.write(f"{account_number},{name},{password},{balance}\n")

    print(f"Your account number: {account_number} (Save this for login)")
    print("Account created successfully!\n")

def login():
    print("\nLogging in...")
    account_number = input("Enter your account number: ").strip()
    password = input("Enter your password: ").strip()

    account = validate_credentials(account_number, password)
    if account:
        print("Login successful!\n")
        banking_menu(account)
    else:
        print("Invalid account number or password.\n")

def banking_menu(account):
    while True:
        print("\nBanking Menu")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Logout")
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            deposit(account)
        elif choice == "2":
            withdraw(account)
        elif choice == "3":
            check_balance(account)
        elif choice == "4":
            print("Logged out successfully.\n")
            break
        else:
            print("Invalid choice. Please try again.\n")

def deposit(account):
    amount = float(input("Enter amount to deposit: "))
    account['balance'] += amount
    update_account(account)
    log_transaction(account['account_number'], "Deposit", amount)
    print(f"Deposit successful! Current balance: {account['balance']}\n")

def withdraw(account):
    amount = float(input("Enter amount to withdraw: "))
    if amount > account['balance']:
        print("Insufficient balance.\n")
    else:
        account['balance'] -= amount
        update_account(account)
        log_transaction(account['account_number'], "Withdrawal", amount)
        print(f"Withdrawal successful! Current balance: {account['balance']}\n")

def check_balance(account):
    print(f"Current balance: {account['balance']}\n")

def validate_credentials(account_number, password):
    if not os.path.exists(ACCOUNTS_FILE):
        return None

    with open(ACCOUNTS_FILE, "r") as file:
        for line in file:
            acc_no, name, pwd, balance = line.strip().split(",")
            if acc_no == account_number and pwd == password:
                return {"account_number": acc_no, "name": name, "password": pwd, "balance": float(balance)}
    return None

def update_account(account):
    if not os.path.exists(ACCOUNTS_FILE):
        return

    accounts = []
    with open(ACCOUNTS_FILE, "r") as file:
        for line in file:
            acc_no, name, pwd, balance = line.strip().split(",")
            if acc_no == account['account_number']:
                accounts.append(f"{acc_no},{name},{pwd},{account['balance']}\n")
            else:
                accounts.append(line)

    with open(ACCOUNTS_FILE, "w") as file:
        file.writelines(accounts)

def log_transaction(account_number, transaction_type, amount):
    with open(TRANSACTIONS_FILE, "a") as file:
        file.write(f"{account_number},{transaction_type},{amount},{datetime.now().strftime('%Y-%m-%d')}\n")

def generate_account_number():
    last_account_number = 12345  # Default starting account number

    if os.path.exists(ACCOUNTS_FILE):
        with open(ACCOUNTS_FILE, "r") as file:
            for line in file:
                acc_no = line.split(",")[0]
                last_account_number = max(last_account_number, int(acc_no))

    return last_account_number + 1

def main():
    while True:
        print("\nWelcome to the Banking System!")
        print("1. Create Account")
        print("2. Login")
        print("3. Exit")
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            create_account()
        elif choice == "2":
            login()
        elif choice == "3":
            print("Thank you for using the Banking System. Goodbye!\n")
            break
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()
