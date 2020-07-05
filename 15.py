# 15. Imagine you are designing a banking application.
# What would a customer look like?
# What attributes would she have? What methods would she have?
def checkBalance():
    print("Balance: ",balance)

def deposit(balance):
    deposit_amt = int(input("Enter amount to be deposited: "))
    balance = balance + deposit_amt
    print("New Balance: ",balance)

def withdraw(balance):
    withdraw_amt = int(input("Enter the amount to be withdrawn: "))
    if (balance >= withdraw_amt):
        balance = balance - withdraw_amt
        print("New Balance: ",balance)
    else:
        print("No enought amount in your account.")

def information():
    print("Name: Megha")
    print("Address: Kathmandu")
    print("Phone Number: 9844856333")
    print("Gender: Female")




print("Welcome to Banking system!\n ")
print("Actions: \n")
print("1.Check Balance")
print("2.Deposit.")
print("3.Withdraw")
print("4. View Information")
balance = 1000
print("Your balance: ",balance)





while True:
    choice = input("Enter choices from 1-4: ")
    if choice in ('1', '2', '3', '4'):
        if choice == '1':
            checkBalance()
        elif choice == '2':
            deposit(balance)
        elif choice == '3':
            withdraw(balance)
        elif choice == '4':
            information()
        break
    else:
        print("Invalid choice.")