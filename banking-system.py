#BANKING APPLICATION
ac_no=0
cus_name=""
branch_code=" "
mobile= 0
bal =0
def CreateAccounts():
    global cus_name
    global branch_code
    global mobile
    global bal
    ac_no= int(input("enter account number :"))
    cus_name=input("enter your name:")
    branch_code=int(input("enter branch code :"))
    mobile=int(input("enter mobile number:"))
    bal=int(input("enter current balance :"))
def showacdetails():
    print("account NO:",ac_no )
    print("customer name:",cus_name)
    print("branch code:",branch_code)
    print("mobile no:",mobile)
def deposite(amount):
    global bal
    bal=bal+amount
    check_balance()
def withdraw(amount):
    global bal
    bal=bal - amount
    check_balance()
def check_balance():
    print("current balance:",bal)
#main
choice1='y'
while (choice1=='y'):
    welcome = input("welcome to our banking application.please press ENTER to continue")
    print("1.accounts\n 2.withdraw\n 3.deposit\n 4.check_balance")
    choice=int(input("select any option:"))
    if choice==1:
        CreateAccounts()
    elif choice==2:
        amount=int(input("enter amount to withdraw"))
        withdraw(amount)
    elif choice==3:
        amount=int(input("enter amount to deposit"))
        deposite(amount)
    elif choice==4:
        check_balance()
    else:
        print("please select any 4 options above")
        print("do you want to continue ....press y")
        choice1=input()
