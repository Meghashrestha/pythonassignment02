# 9. Write a binary search function. It should take a sorted sequence and the item it is looking for.
# It should return the index of the item if found. It should return -1 if the item is not found.
def binary_search(sorted_func):
    m=int(input(" enter the item you are searching for "))
    mid  = len(sorted_func)//2
    mid_val = sorted_func[mid]
    print(mid)
    print(mid_val)
    if m > mid_val:
        for i in range(mid, len(sorted_func)):
            sorted_func[i] = int(sorted_func[i])
            if m not in sorted_func:
                return -1
            else:
                index1 = sorted_func.index(sorted_func[m])

        print("the index of the %d is %d " % (m, index1))
    elif m<mid_val:
        for i in range(0, mid-1):
            sorted_func[i] = int(sorted_func[i])
            if m not in sorted_func:
                return -1
            else:
                index2 = sorted_func.index(sorted_func[m])

        print("the index of the %d is %d " % (m, index2))

    else:
        print("the index of the %d is %d " % (mid_val, mid)



n=int(input("enter the number of item in list :"))
sorted_func = []
for i in range(0, n):
    element = int(input("enter :" ))
    sorted_func.append(element)
print(sorted_func)
if sorted_func==sorted(sorted_func):
    print(binary_search(sorted_func))
else:
    print(" the list is not sorted ...")

