"""
Write a Python program to read a given CSV file having tab delimiter.
"""

import csv

file = "C:\\Users\\mipc\\Downloads\\email tab.txt"

with open(file) as file:
    reader_obj = csv.reader(file, delimiter='\t')
    for row in reader_obj:
        print(row)
