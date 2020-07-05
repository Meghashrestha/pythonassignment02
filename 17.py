# 17. Write a program that serves as a basic calculator.
# It asks for two numbers, then it asks for an operator.
# Gracefully deal with input that doesn't cleanly convert to numbers. Deal with division by zero errors.
def Add(a, b):
    return a+b

def Sub(a, b):
    return a-b

def Mul(a, b):
    return a*b

def Div(a, b):
    try:
        result = a/b
        return result
    except ZeroDivisionError:
        return "try again"


print("calculator")
print("1.Addition")
print("1.Subtraction")
print("3.Multiplication")
print("4.Division")
while True:
    choice = input("Enter choices from 1-4: ")
    if choice in ('1', '2', '3', '4'):
        x = int(input("X: "))
        y = int(input("Y: "))
        if choice == '1':
            print(Add(x, y))
        elif choice == '2':
            print(Sub(x, y))
        elif choice == '3':
            print(Mul(x, y))
        elif choice == '4':
            print(Div(x, y))
        break
    else:
        print("Invalid choice.")

