# 20. Write a Python class to find the three elements that sum to zero
# from a list of n real numbers. Input array : [-25, -10, -7, -3, 2, 4, 8, 10] Output : [[-10, 2, 8], [-7, -3, 10]]

def three_element(arr, n):
    found = True
    for i in range(0, n - 2):

        for j in range(i + 1, n - 1):

            for k in range(j + 1, n):

                if (arr[i] + arr[j] + arr[k] == 0):
                    print("[%d, %d, %d]" % (arr[i], arr[j], arr[k]))
                    found = True

    if (found == False):
        print(" not exist ")


arr = []
x = int(input("enter the number of item :"))
for i in range(0, x):
    element = int(input("enter : "))
    arr.append(element)
# arr = [0, -1, 2, -3, 1]
print(arr)
n = len(arr)


print(three_element(arr, n))

