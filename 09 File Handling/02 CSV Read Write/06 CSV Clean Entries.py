"""
Write a Python program that reads a CSV file and remove initial spaces, quotes around each entry and the delimiter.
"""

import csv

file = "C:\\Users\\mipc\\Downloads\\email tab.txt"

with open(file) as file:
    reader_obj = csv.reader(file, delimiter='\t')
    for row in reader_obj:
        row = ''.join(row).lstrip()
        print(row)
