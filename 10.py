# 10. Write a function that takes camel-cased strings (i.e. ThisIsCamelCased), and converts them to snake case (i.e. this_is_camel_cased).
# Modify the function by adding an argument, separator,
# so it will also convert to the kebab case (i.e.this-is-camel-case) as well.

def camel_to_snake(string):
    return ''.join(['_' + i.lower() if i.isupper()
                    else i for i in string]).lstrip('_')

def camel_to_kebab(string):
    return ''.join(['-' + i.lower() if i.isupper()
                    else i for i in string]).lstrip('-')

string = input("enter the string")
if string != string.lower() and string != string.upper() and "_" not in string:
    print(camel_to_snake(string))
    print(camel_to_kebab(string))
else:
    print("not camelcase")