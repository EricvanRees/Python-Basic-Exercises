"""
Write a Python program that iterates over elements as many times as its count.

Sample Output: ['p', 'p', 'p', 'p', 'q', 'q']
"""

from collections import Counter

c = Counter(p=2, q=3, e=5)
print(list(c.elements()))