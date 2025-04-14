"""
Write a Python program that retrieves the date and time of file creation and modification.
"""

import os, os.path, time

# create file path
file = os.path.realpath(__file__)
# print date and time of file creation
print("created: %s" % time.ctime(os.path.getctime(file)))
# print date and time of file modification
(mode, ino, dev, nlink, uid, gid, size, atime, mtime, ctime) = os.stat(file)
print("last modified: %s" % time.ctime(mtime))