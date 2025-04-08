"""
Write a Python program to get the execution time of a Python method.
"""

import time

t = time.process_time()
for x in range(1000):
  print(x)

elapsed_time = time.process_time() - t
print(f"execution time: {elapsed_time} seconds")