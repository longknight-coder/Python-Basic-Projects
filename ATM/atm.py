# phase1
bank_account = 0
history = []

def balance():
    global bank_account
    print(f"[{bank_account}] rupees in your account")
    history.append("checked balance")

def deposite():
    global bank_account
    a = int(input("enter the money you want to deposite : "))
    bank_account += a
    print(f"your total balance is {bank_account}")
    history.append(f"deposited {a}")


def withdraw():
    global bank_account
    b = int(input("enter the money you want to withdraw : "))
    if bank_account < b:
        print("insifficient balance")
    else:
        bank_account -= b
        print(f"your total balance is {bank_account}")
    history.append(f"withdraw {b}")


def instruction():
    print("""
    1. Check Balance
    2. Deposit
    3. Withdraw
    4. Exit
    5. History
    """)


while True:
    instruction()
    user = input("enter what you want 1/2/3/4/5 : ")
    if user == "1":
        balance()

    elif user == "2":
        deposite()

    elif user == "3":
        withdraw()

    elif user == "4":
        break

    elif user == "5":
        for i in history:
            print(i)
    else:
        print("invalid")
        
print("hello")
# this is 
# SyntaxWarningwa
