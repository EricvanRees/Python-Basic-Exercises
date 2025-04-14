"""
Write a Python program to create a histogram from a given list of integers.
"""

from collections import Counter

# Define a list of elements
my_list = [1, 2, 3, 2, 4, 2, 5]

# Create a Counter object to count occurrences
counter_obj = Counter(my_list)

# Print occurences for each integer
print(dict(counter_obj.most_common()))