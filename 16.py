# # 16. Imagine you are creating a Super Mario game.
# # You need to define a class to represent Mario. What would it look like?
# # If you aren't familiar with SuperMario, use your own favorite video or board game to model a player.
def size(size1):
    print("Size")
    print("1.Small")
    print("2.Big")
    while True:
        choice = input("Enter choices 1/2: ")
        if choice in ('1', '2'):
            if choice == '1':
                size1= print("Small")
                return size1
            elif choice == '2':
                size1 = print("big")
                return size1
            break
        else:
            print("Invalid choice.")
def Jump(Jump1):
    print("Jump")
    print("1.High")
    print("2.Low")
    while True:
        choice = input("Enter choices 1/2: ")
        if choice in ('1', '2'):
            if choice == '1':
                Jump1= print("High")
                return Jump1
            elif choice == '2':
                Jump1 = print("Low")
                return Jump1
            break
        else:
            print("Invalid choice.")

def Tool(Tool1):
    print("Tool")
    print("1.Gun")
    print("2.Knife")
    while True:
        choice = input("Enter choices 1/2: ")
        if choice in ('1', '2'):
            if choice == '1':
                Tool1= print("Gun")
                return Tool1
            elif choice == '2':
                Tool1 = print("Knife")
                return Tool1
            break
        else:
            print("Invalid choice.")


def View_avatar():
    n = int(input("do you want to view avatar"))
    if n==1:
        print("default avatar")
        print("size : small")
        print("Jump : High")
        print("Tool : Gun")
    else:
        pass



print("Super mario ")
print("Select Avatar: \n")
print("Size")
print("2.Jump")
print("3.Tool")
print("4. View Avatar")
size1 = "Small"
Jump1 = "High"
Tool1 = "knife"





while True:
    choice = input("Enter choices from 1-4: ")
    if choice in ('1', '2', '3', '4'):
        if choice == '1':
            size(size1)

        elif choice == '2':
            Jump(Jump1)
        elif choice == '3':
            Tool(Tool1)
        elif choice == '4':
            View_avatar()
        break
    else:
        print("Invalid choice.")
