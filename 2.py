# . Write an if statement to determine whether a variable holding a year
# is a leap year.
def year(days):
    if days==365:
        print("Happy year")
    elif days==366 or days==364:
        print("ophs! Leap year")
    else:
        print("Incorrect days.Enter again")


days = int(input("enter days"))
print(year(days))