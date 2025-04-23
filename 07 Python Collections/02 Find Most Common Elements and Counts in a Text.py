"""
Write a Python program to find the most common elements and their counts in a specified text.

Original string: lkseropewdssafsdfafkpwe
Most common three characters of the said string:
[('s', 4), ('e', 3), ('f', 3)]
"""

from collections import Counter

mystr = "lkseropewdssafsdfafkpwe"
count = Counter(mystr).most_common(3)
print(count)
