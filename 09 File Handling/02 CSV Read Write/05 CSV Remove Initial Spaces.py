"""
Write a Python program to read a given CSV files with initial spaces after a delimiter and remove those initial spaces.
"""

import csv

file = "C:\\Users\\mipc\\Downloads\\email tab.txt"

with open(file) as file:
    reader_obj = csv.reader(file, delimiter='\t')
    for row in reader_obj:
        row = '\t'.join(row).lstrip()
        print(row)
