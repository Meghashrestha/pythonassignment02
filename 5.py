# . Create a tuple with your first name, last name, and age. Create a list,
# people, and append your tuple to it. Make more tuples with
# the corresponding information from your friends and append them to the list. Sort the list. When you learn about sort method,
# you can use the key parameter to sort by any field in the tuple, first name, last name, or age.

tuple1 = ('megha', 'shrestha', '22')
print(tuple1)
list1 = []
list1.append(tuple1)
# list1.sort()
print(list1)
final_list = []
line = input("Enter the list of tuples:\n")
while (line != ''):
    final_list.append(tuple(line.split()))
    line = input()
print(final_list)
list3 = list1 + final_list
print("final list")
print(list3)
list3.sort(key = lambda x: x[0])
print("list sorted by first name")
print(list3)
list3.sort(key = lambda x: x[1])
print("list sorted by last name")
print(list3)
list3.sort(key = lambda x: x[2])

print("list sorted by age")
print(list3)