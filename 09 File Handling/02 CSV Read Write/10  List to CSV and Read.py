"""
Write a Python program to write a Python list of lists to a csv file. After writing the CSV file read the CSV file and display the content.
"""

import csv

my_data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

myfile = "my_data.csv"

with open(myfile, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(my_data)

with open(myfile) as file_obj:
    reader_obj = csv.reader(file_obj)
    for row in reader_obj:
        print(row)
