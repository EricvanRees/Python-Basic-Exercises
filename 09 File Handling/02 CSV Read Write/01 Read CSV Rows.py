"""
Write a Python program to read each row from a given csv file and print a list of strings.
"""
import csv

file = "C:\\Users\\mipc\\Downloads\\email.csv"
row_list = []

with open(file) as file:
    reader_obj = csv.reader(file)
    for row in reader_obj:
        row = ''.join(row)
        row_list.append(row)

    print(row_list)
