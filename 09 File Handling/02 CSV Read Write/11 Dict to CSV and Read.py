"""
Write a Python program to write a Python dictionary to a csv file. After writing the CSV file read the CSV file and display the content.
"""

import csv

mydict = {"name": "Eric", "lastname": "van Rees", "age": 45}
myfile = "my_data.csv"

with open(myfile, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(mydict.keys())
    writer.writerow(mydict.values())

with open(myfile) as file_obj:
    reader_obj = csv.reader(file_obj)
    for row in reader_obj:
        print(row)
