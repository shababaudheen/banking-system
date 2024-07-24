# Banking System

import random
import sys
from details import Account


class Bank:

    def __init__(self):
        print("Press 1 to login to your account.\nPress 2 for create new account."
              "\nPress any other number exit this page")
        num1 = int(input("Enter the number according to your purpose: "))
        if num1 == 1:
            a = input("Username: ")
            b = input("Password: ")
            self.username = a
            self.password = b
            self.login()
        elif num1 == 2:
            self.new_account()
        else:
            sys.exit()

    def login(self):
        if self.username in Account and self.password in Account[self.username]["Password"]:
            self.home()
        else:
            print("Invalid username or password")
            self.__init__()

    def home(self):
        print("Click 1 to know your account balance.\nPress 2 to deposit the cash.\nPress 3 to withdraw the "
              "cash.\nPress any other number to logout and exit.")
        print(f"Welcome {Account[self.username]["Name"]}")
        num = int(input("Enter the number according to your need: "))
        if num == 1:
            self.balance()
        elif num == 2:
            self.deposit()
        elif num == 3:
            self.withdraw()
        else:
            print("Thank you for using our service")
            sys.exit()

    def balance(self):
        print("Your current balance is ", Account[self.username]["Balance"])
        self.home()

    def deposit(self):
        cash_deposit = int(input("Amount of cash to be deposited "))
        print(f"{cash_deposit} rupees credited in your account successfully")
        print("Your current balance is ", Account[self.username]["Balance"] + cash_deposit)
        with open("details.py", "r") as file:
            content = file.read()
            content = content.replace(f"{Account[self.username]["Balance"]}",
                                      f"{Account[self.username]["Balance"] + cash_deposit}")
        with open("details.py", "w") as file:
            file.write(content)
        self.home()

    def withdraw(self):
        cash_withdraw = int(input("Amount of cash to be withdrawn "))
        if cash_withdraw <= Account[self.username]["Balance"]:
            print(f"{cash_withdraw} rupees debited from your account successfully")
            print("Your current balance is ", Account[self.username]["Balance"] - cash_withdraw)
            with open("details.py", "r") as file:
                content = file.read()
                content = content.replace(f"{Account[self.username]["Balance"]}",
                                          f"{Account[self.username]["Balance"] - cash_withdraw}")
            with open("details.py", "w") as file:
                file.write(content)
            self.home()
        else:
            print("Your account balance is insufficient to be withdrawn. ")
            self.withdraw()

    def new_account(self):
        name = input("Enter your name: ")
        dob = input("Enter your Dob (dd/mm/yyyy): ")
        e_mail = input("Enter your e-mail id: ")
        phone_no = int(input("Enter your phone: "))
        acc_no = random.randint(10000000000, 99999999999)
        balance = 0
        print(f"Your account number is {acc_no}")
        print("Please create an username and password for this account")
        user = input("Create an username: ")
        pass_word = input("Create a new password: ")
        if user not in Account:
            Account[user] = {"Acc. No.": acc_no, "Password": pass_word, "Balance": balance, "Name": name,
                             "E-mail": e_mail, "Phone No.": phone_no, "DOB": dob}
            print("You have created your account successfully")
            print("Login again for accessing your account")
            with open("details.py", "w") as file:
                file.write(f"Account = {Account} \n")
            self.__init__()
        else:
            print("Please try with different username")
            self.new_account()


k1 = Bank()
k1.__init__()
