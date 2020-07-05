# 13. Write a function to write a comma-separated value (CSV) file.
# It should accept a filename and a list of tuples as parameters.
# The tuples should have a name, address, and age.
# The file should create a header row followed by a row for each tuple.
# If the following list of tuples was passed in: [('George', '4312 Abbey Road', 22), ('John', '54 Love Ave', 21)]
# it should write the following in the file:
# name,address,age George,4312 Abbey Road,22
# John,54 Love Ave,21
import csv
import os

def csv_file():
    path = '/home/megha/PycharmProjects/pythonassignment2/csv file'

    fields = ('Name','Address','Age')
    filename = input("Enter file name: ")+'.csv'
    csvFilename = os.path.join(path,filename)
    my_tuple = ()
    list = []
    count = int(input("Enter number of items to be written in File: "))
    for i in range(0,count):
        data  = input("Enter Name , Address , Age seperated by: ")
        my_tuple = tuple(data.split())
        list.append(my_tuple)
    print(list)
    with open(csvFilename,'w',newline='') as f:
        writer = csv.writer(f,delimiter=',')
        writer.writerow(fields)
        writer.writerows(list)

csv_file()
