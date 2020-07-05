# 12. Create a function, is_palindrome, to determine if a supplied word is
# the same if the letters are reversed.
def is_palindrome(string):
    string1 = "".join(reversed(string))
    if string == string1:
        print("It is palindrome")
    else:
        print("not")

string = input("enter string: ")
print(is_palindrome(string))