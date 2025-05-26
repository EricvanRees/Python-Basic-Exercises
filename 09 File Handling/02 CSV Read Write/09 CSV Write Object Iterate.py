"""
Write a Python program to create an object for writing and iterate over the rows to print the values.
"""

import csv

myfile = "my_data.csv"

with open(myfile, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["number1", "number2", "number3"])
    for i in range(3):
        row = [i + 10, i + 11, i + 12]
        writer.writerow(row)

with open(myfile) as file_obj:
    reader_obj = csv.reader(file_obj)
    for row in reader_obj:
        print(row)
