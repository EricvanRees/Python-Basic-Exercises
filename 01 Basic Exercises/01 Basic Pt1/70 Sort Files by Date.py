"""
Write a Python program to sort files by date.

NOTE: only returns file names and creation date, no sorting yet

"""

""" import datetime
import os

# Path to the file
path = r"C:\\Users\\mipc\\Downloads\\samples"

files = os.listdir(path)
# Filtering only the files.
print(files)

for f in files:
  if os.path.isfile(path+'/'+f): 

    # file modification timestamp of a file
    m_time = os.path.getmtime(path+'/'+f)
    # convert timestamp into DateTime object
    dt_m = datetime.datetime.fromtimestamp(m_time)
    print('Modified on:', dt_m)

    # file creation timestamp in float
    c_time = os.path.getctime(path+'/'+f)
    # convert creation timestamp into DateTime object
    dt_c = datetime.datetime.fromtimestamp(c_time)
    print('Created on:', dt_c) """