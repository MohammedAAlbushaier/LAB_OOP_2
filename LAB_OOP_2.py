import json
import os

# Creating a class called BanckAccount
class BankAccount:
    #creat an initi
    def __init__(self, account_holder: str, account_number: str, balance: float = 0.00):
        self.__account_holder = account_holder
        self.__account_number = account_number
        self.__balance = balance

    #Function to set the account name
    def set_account_name(self, account_holder: str):
        self.__account_holder = account_holder

    #Function to set the balance
    def set_balance(self, balance: float):
        self.__balance = balance

    #Function to get the balance
    def get_balance(self):
        return self.__balance

    # Function to get the account holder name
    def get_account_holder(self):
        return self.__account_holder

    # Function to get the account number
    def get_account_number(self):
        return self.__account_number

    # Function to get deposit money into the account
    def deposit(self, amount: float):
        if amount > 0:
            self.__balance += amount
            self._update_account_in_file()
            print(f"Thank you {self.__account_holder}, your new balance is {self.__balance}$")
        else:
            print("Please enter a valid amount.")

    # Function to get withdraw money into the account
    def withdraw(self, amount: float):
        if amount > 0:
            if self.__balance >= amount:
                self.__balance -= amount
                self._update_account_in_file()
                print(f"Thank you, {amount}$ has been withdrawn successfully.")
                print(f"Your new balance is {self.__balance}$")
            else:
                print(f"Sorry, {self.__account_holder}, you have insufficient funds.")
        else:
            print("Please enter a valid amount.")

    #To add the Account from the Dictonary into the json file called "balance.json"
    def add_to_file(self):
        accounts = self._read_accounts_file()
        # Check if account already exists
        for account in accounts:
            if account["account_number"] == self.__account_number:
                print("Account already exists.")
                return
        # Add new account
        accounts.append({
            "name": self.__account_holder,
            "account_number": self.__account_number,
            "balance": self.__balance
        })
        self._write_accounts_file(accounts)

    # To update the Accounts after running the intended function then send the updated file to the write_accounts_file
    def _update_account_in_file(self):
        accounts = self._read_accounts_file()
        for account in accounts:
            if account["account_number"] == self.__account_number:
                account["name"] = self.__account_holder
                account["balance"] = self.__balance
                break
        self._write_accounts_file(accounts)

    #To retrieve the Account information then load it into a set
    def _read_accounts_file(self):
        if not os.path.isfile("balance.json"):
            return []
        with open("balance.json", "r", encoding="UTF-8") as f:
            try:
                return [json.loads(line) for line in f]
            except json.JSONDecodeError:
                return []

    #To upload the accounts information into the json file called "balnce.json"
    def _write_accounts_file(self, accounts):
        with open("balance.json", "w", encoding="UTF-8") as f:
            for account in accounts:
                f.write(json.dumps(account) + "\n")

    #To get the last account number uploaded to the file then add 1 to it then assign the new number to the new account
    def assign_account_number(self):
        accounts = self._read_accounts_file()
        if accounts:
            # Extract account numbers and convert to integers
            account_numbers = [int(account["account_number"]) for account in accounts]
            last_account_number = max(account_numbers)
            return str(last_account_number + 1)
        return "1025463290"  # Starting account number

