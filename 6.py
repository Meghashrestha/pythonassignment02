# 6. Create a list with the names of friends and colleagues. Search for the
# name ‘John’ using a for a loop. Print ‘not found’ if you didn't find it.
list = []
n = int(input("enter the number of friends name you want to enter :"))
for i in range(0, n):
    element = input("enter name: ")
    list.append(element)
print(list)
print("searching John")
if 'john' in list :
    print("john is in list")
else:
    print("not found")

