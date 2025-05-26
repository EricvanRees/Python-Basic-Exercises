"""
Write a Python program to read specific columns of a given CSV file and print the content of the columns.
"""

import csv

file = "C:\\Users\\mipc\\Downloads\\email.csv"

with open(file, newline='') as f:
    reader_obj = csv.DictReader(f, delimiter=';')
    for row in reader_obj:
        print(row['First name'], row['Last name'])
