# 11. Create a variable, filename.
# Assuming that it has a three-letter extension,
# and using slice operations, find the extension.
# For README.txt, the extension should be txt. Write code using slice operations that will give the name without the extension.
# Does your code work on filenames of arbitrary length?

def filename(name):
    list1 = name.split('.')
    element = list1[1]
    list1.remove(element)
    string = ' '.join([str(elem) for elem in list1])
    print(string)

name = input("enter file name : ")
if '.' in name:
    i = name.index('.')

    if len(name[i-1:])==3:
        print(filename(name))
    else:
        print("enter extension with 3 character")
else:
    print("no")


