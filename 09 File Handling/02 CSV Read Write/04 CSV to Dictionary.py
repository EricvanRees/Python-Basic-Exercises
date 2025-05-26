"""
Write a Python program to read a given CSV file as a dictionary.
"""

import csv

file = "C:\\Users\\mipc\\Downloads\\email.csv"

with open(file) as file:
    reader_obj = csv.DictReader(file)
    for row in reader_obj:
        print(row)
