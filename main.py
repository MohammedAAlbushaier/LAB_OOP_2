from LAB_OOP_2 import BankAccount
import os
import json

#To print the menu of the Application
def display_menu():
    print("\nWelcome to Bank Account Application:")
    print("Please Choose a number from the following list")
    print("(1) Open a new bank account")
    print("(2) Display account balance")
    print("(3) Deposit money to your account")
    print("(4) Withdraw balance from your account")
    print("(5) Get account holder's name")
    print("(9) Exit the application")


#To open a new account then create an instance of the class BanckAccount
def open_new_account():
    name = input("Please enter the account holder name: ")
    balance = float(input("Please enter initial balance for the account: "))
    account = BankAccount(name, "", balance)  # Account number will be assigned automatically
    account_number = account.assign_account_number()
    account = BankAccount(name, account_number, balance)
    account.add_to_file()
    print(f"\nThank you {account.get_account_holder()} for choosing our Bank.")
    print(f"Your account number is {account.get_account_number()}\n")
    return account

#To print the account information
def display_balance(account):
    print(f"\nHello {account.get_account_holder()}, you have {account.get_balance()}$ in your bank account.\n")

#To send the Amount to be added using the deposit function from the BankAccount
def deposit_money(account):
    amount = float(input("Please enter the amount to deposit: "))
    account.deposit(amount)


#To send the Amount to be subtracted using the deposit function from the BankAccount
def withdraw_money(account):
    amount = float(input("Please enter the amount you would like to withdraw: "))
    account.withdraw(amount)

#To get the account holder information
def get_account_holder_name(account):
    print(f"\nThe account {account.get_account_number()} belongs to {account.get_account_holder()}\n")


# To load the Accounts in a dictonary instance
def load_accounts():
    """Load all accounts from the file into the accounts dictionary."""
    if not os.path.isfile("balance.json"):
        return {}
    with open("balance.json", "r", encoding="UTF-8") as f:
        try:
            accounts_data = [json.loads(line) for line in f]
            return {account["account_number"]: BankAccount(account["name"], account["account_number"], account["balance"]) for account in accounts_data}
        except json.JSONDecodeError:
            return {}


# To run the Bank Application
def main():
    accounts = load_accounts()  # Load accounts from file
    while True:
        display_menu()
        try:
            choice = int(input("Enter your choice please: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == 1:
            account = open_new_account()
            accounts[account.get_account_number()] = account  # Add new account to dictionary
        elif choice == 2:
            account_number = input("Please enter your account number: ")
            account = accounts.get(account_number)
            if account:
                display_balance(account)
            else:
                print("No account was found. Please open a new account first.")
        elif choice == 3:
            account_number = input("Please enter your account number: ")
            account = accounts.get(account_number)
            if account:
                deposit_money(account)
            else:
                print("No account was found. Please open a new account first.")
        elif choice == 4:
            account_number = input("Please enter your account number: ")
            account = accounts.get(account_number)
            if account:
                withdraw_money(account)
            else:
                print("No account was found. Please open a new account first.")
        elif choice == 5:
            account_number = input("Please enter your account number: ")
            account = accounts.get(account_number)
            if account:
                get_account_holder_name(account)
            else:
                print("No account was found. Please open a new account first.")
        elif choice == 9:
            print("Thank you for choosing our Bank Application see you agin soon."
                  " Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()