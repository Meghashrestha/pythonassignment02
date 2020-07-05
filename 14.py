# 14. Write a function that reads a CSV file.
# It should return a list of dictionaries, using the first row as key names, and each subsequent row as values for those keys.
# For the data in the previous example it would return: [{'name': 'George', 'address': '4312 Abbey Road', 'age': 22},
# {'name': 'John', 'address': '54 Love Ave', 'age': 21}]
import csv
import os



with open('/home/megha/PycharmProjects/pythonassignment2/csv file/myfile.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    my_tuple= ()
    list1=[]
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            element=(f'Name:{row[0]} Adress: {row[1]} Age:  {row[2]}.')
            # print(f'\tName:{row[0]} Adress: {row[1]} Age:  {row[2]}.')
            line_count += 1
            my_tuple = tuple(element.split(','))
            print(my_tuple)
            list1.append(my_tuple)
    print(list1)
    print(f'Processed {line_count} lines.')