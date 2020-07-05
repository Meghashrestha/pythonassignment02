# 7. Create a list of tuples of first name, last name, and age for your friends and colleagues.
# If you don't know the age, put in None. Calculate the average age, skipping over any None values.
# Print out each name, followed by old or young if they are above or below the average age.

tuple1 = ('megha', 'shrestha', 22)
tuple2 = ('reshma', 'shah', 10)
tuple3 = ('ram', 'gupta', None)
tuple4 = ('shyam', 'bhatrai', 16)

print(tuple1)
print(tuple2)
print(tuple3)
print(tuple4)

list1 = []
list2 = []
list3 = []
list4 = []
list1.append(tuple1)
list2.append(tuple2)
list3.append(tuple3)
list4.append(tuple4)
list5 = []
list6 = []
list5 = list1 + list2 + list3 + list4
print(list5)
for i in list5:
    if i[2]!=None:
        element = i[2]
        list6.append(element)
    else:
        pass
print(list6)
res = sum(list6)
average_age = res/4
print("average age is ", average_age)
for i in list5:
    if i[2]== None:
        print("no age assigned for %s" %i[0])
    elif i[2] >= 18 :
        print("%s is older than 18" %i[0])
    elif i[2] < 18:
        print("%s is younger than 18" %i[0])
    else:
        pass


