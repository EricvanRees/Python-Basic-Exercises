"""
Write a Python program that reads each row of a given csv file and skip the header of the file. Also print the number of rows and the field names.
"""

import csv

file = "C:\\Users\\mipc\\Downloads\\email.csv"
row_list = []

with open(file) as file:
    row_count = 0
    i = 0
    # get field names from header
    reader = csv.DictReader(file, delimiter=";")
    fieldnames = reader.fieldnames
    for fieldname in fieldnames:
        i += 1
        print(f"fieldname {i} is {fieldname}")

    reader_obj = csv.reader(file)
    next(reader_obj, None)  # skip the headers
    for row in reader_obj:
        print(row)
        row_count += 1

    print(f"row count is {row_count}")
