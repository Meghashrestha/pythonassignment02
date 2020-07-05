# 4. Create a list. Append the names of your colleagues and friends to it. Has the id of the list changed? Sort the list.
# What is the first item on the list? What is the second item on the list?
# def colleague(name):

#
# def colleague(name):
#     print(list)
#     for i in range(0, n):
#         index = list.index(list[i])
#         name = list[i]
#         print("the id of %s is %d" % (name, index))
#     list.sort()
#     print(list)
#
#     for i in range(0, n):
#         index = list.index(list[i])
#         name = list[i]
#         print("the id of %s is %d" % (name, index))
#
#
# n = int(input("enter number of item"))
# list = []
# for i in range(0, n):
#     element = input("enter name: ")
#     list.append(element)
# print(colleague(list))

n = int(input("enter number of item"))
list = []
x = id(list)
print(id(list))
for i in range(0, n):
    element = input("enter name: ")
    list.append(element)
list.sort()
print(list)
y = id(list)
print(y)


if x==y :
    print("The id for both are same")
else:
    print("No")
