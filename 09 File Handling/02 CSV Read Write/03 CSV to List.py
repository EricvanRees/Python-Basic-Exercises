"""
Write a Python program to read a given CSV file as a list.
"""

import csv

file = "C:\\Users\\mipc\\Downloads\\email.csv"

with open(file) as file:
    reader_obj = csv.reader(file)
    print(list(reader_obj))
