import pickle
import os
import pathlib


class Bank:
    name = ""
    surname = ""
    account_number = 0
    balance = 0
    accounts_list = []

    # def __init__(self, name, surname, account_number, balance, accounts_list):
    #     self.name = name
    #     self.surname = surname
    #     self.account_number = account_number
    #     self.balance = balance
    #     self.accounts_list = accounts_list

    def create_account(self):
        self.accounts_list = []
        self.account_number = int(input("Enter the account number: "))
        self.accounts_list.append(self.account_number)
        self.name = input("Enter the client's name: ")
        self.surname = input("Enter the client's surname: ")
        print("\n\nAccount created")
        self.balance = 0
        # print(f"{self.name} {self.surname} has remaining balance of ${round(self.balance, 2)}.")

    # def deposit_amount(self, amount):
    #     if amount > 0:
    #         self.balance += amount
    #     else:
    #         print("Invalid amount to deposit!")
    #     # print(f"{self.name} {self.surname} has remaining balance of ${round(self.balance, 2)}.")
    #
    # def withdraw_amount(self, amount):
    #     if amount > self.balance or amount < 0:
    #         print("Insufficient money on the account or wrong amount inputted!")
    #         # print(f"{self.name} {self.surname} has remaining balance of ${round(self.balance, 2)}.")
    #     else:
    #         self.balance -= amount
    #         # print(f"{self.name} {self.surname} has remaining balance of ${round(self.balance, 2)}.")

# name = ""
# surname = ""
# account_number = 0
# balance = 0
# accounts_list = []


def creating_bank_account():
    create_bank_account = Bank()
    create_bank_account.create_account()
    manage_accounts_file(create_bank_account)


def manage_accounts_file(account):
    file = pathlib.Path("accounts.txt")
    if file.exists():
        infile = open("accounts.txt", 'rb')
        old_list = pickle.load(infile)
        old_list.append(account)
        infile.close()
        os.remove("accounts.txt")
    else:
        old_list = [account]

    outfile = open("new_accounts.txt", 'wb')
    pickle.dump(old_list, outfile)
    outfile.close()
    os.rename("new_accounts.txt", 'accounts.txt')

# def create_account():
#     # global name
#     # global surname
#     # global account_number
#     # global balance
#     # global accounts_list
#     file = pathlib.Path("accounts.txt")
#     if file.exists():
#         infile = open("accounts.txt", 'rb')
#         info = pickle.load(infile)
#         infile.close()
#         os.remove("accounts.txt")
#
#         account_number = int(input("Enter the account number: "))
#         name = input("Enter the client's name: ")
#         surname = input("Enter the client's surname: ")
#         print("\n\nAccount created")
#         balance = 0
#         print(f"{name}, {surname}, 'has remaining balance of $ ', {round(balance, 2)}.")
#         Bank.accounts_list.append(account_number)
#
#         outfile = open("new_accounts.txt", 'wb')
#         pickle.dump(info, outfile)
#         outfile.close()
#         os.rename("new_accounts.txt", 'accounts.txt')


def display_all():
    file = pathlib.Path("accounts.txt")
    if file.exists():
        infile = open("accounts.txt", 'rb')
        info = pickle.load(infile)
        for item in info:
            print(item.name, " ", item.surname, " ", item.account_number, " ", item.balance)
        infile.close()
    else:
        print("The file does not exists")


def deposit_amount(num):
    # global name
    # global surname
    # global account_number
    # global balance
    file = pathlib.Path("accounts.txt")
    if file.exists():
        infile = open("accounts.txt", 'rb')
        info = pickle.load(infile)
        infile.close()
        os.remove("accounts.txt")

        for item in info:
            if item.account_number == num:
                amount = float(input("Please enter the amount the client wants to deposit: "))
                if amount > 0:
                    item.balance += amount
                else:
                    print("Invalid amount to deposit!")
                print(f"The remaining balance is ${round(item.balance, 2)}")

        outfile = open("new_accounts.txt", 'wb')
        pickle.dump(info, outfile)
        outfile.close()
        os.rename("new_accounts.txt", 'accounts.txt')
    else:
        print("The file does not exists")


def withdraw_amount(num):
    # global name
    # global surname
    # global account_number
    # global balance
    file = pathlib.Path("accounts.txt")
    if file.exists():
        infile = open("accounts.txt", 'rb')
        info = pickle.load(infile)
        infile.close()
        os.remove("accounts.txt")

        for item in info:
            if item.account_number == num:
                amount = float(input("Please enter the amount the client wants to withdraw: "))
                if amount > item.balance:
                    print("Insufficient money on the account!")
                    print("Account balance is: $", item.balance)
                else:
                    item.balance -= amount
                print(f"The remaining balance is ${round(item.balance, 2)}")

        outfile = open("new_accounts.txt", 'wb')
        pickle.dump(info, outfile)
        outfile.close()
        os.rename("new_accounts.txt", 'accounts.txt')
    else:
        print("The file does not exists")


def transfer_money():
    # global name
    # global surname
    # global account_number
    # global balance
    # global accounts_list
    file = pathlib.Path("accounts.txt")
    if file.exists():
        infile = open("accounts.txt", 'rb')
        info = pickle.load(infile)
        infile.close()

        os.remove("accounts.txt")
        while len(info.accounts_list) > 1:
            account_1 = int(input("Please input the account number you want money to withdraw from "))
            if account_1 in info.accounts_list:
                account_2 = int(input("Please input the account number you want money to transfer to "))
                if account_2 in info.accounts_list:
                    transfer_amount = float(input("Please enter the amount you want to transfer "))
                    if 0 < transfer_amount <= account_1.balance:
                        account_1.balance -= transfer_amount
                        account_2.balance += transfer_amount
                    else:
                        print("Insufficient money on the account or wrong amount!")
                else:
                    print("The account number does not exists. Please input another one.")
            else:
                print("The account number does not exists. Please input another one.")

        outfile = open("new_accounts.txt", 'wb')
        pickle.dump(info, outfile)
        outfile.close()
        os.rename("new_accounts.txt", 'accounts.txt')


def delete_account(num):
    file = pathlib.Path("accounts.txt")
    if file.exists():
        infile = open("accounts.txt", 'rb')
        old_list = pickle.load(infile)
        infile.close()
        new_list = []

        for item in old_list:
            if item.account_number != num:
                new_list.append(item)
        os.remove("accounts.txt")
        outfile = open("new_accounts.txt", 'wb')
        pickle.dump(new_list, outfile)
        outfile.close()
        os.rename("new_accounts.txt", 'accounts.txt')
    else:
        print("The file does not exists")
