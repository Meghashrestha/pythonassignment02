# 18. Find a package in the Python standard library for dealing with JSON.
# Import the library module and inspect the attributes of the module.
# Use the help function to learn more about how to use the module.
# Serialize a dictionary mapping 'name' to your name and 'age' to your age, to a JSON string.
# Deserialize the JSON back into Python.
import json
import createdmodule
def help():
    print("We can import the definitions inside a module to another module or the interactive interpreter in Python."
          "We use the import keyword to do this. ")
createdmodule.greeting("Megha")
createdmodule.__name__
print("The attributes of module\" createmdodule \" are : ")
print(dir(createdmodule))
print(help())
print("Dictionaries: ")
details = {"name": "Megha", "age": 22}
print(details)
details_dict = json.dumps(details, indent = 2)
print( details_dict)

# print("Now, converting into dictionaries from JSON\n")
json_string = json.loads(details_dict)
print(json_string)