"""
Write a Python program to display the current date and time.
Sample Output :
Current date and time :
2014-07-05 14:34:14

"""

import datetime

def format_time():
    t = datetime.datetime.now()
    s = t.isoformat(timespec='seconds')
    newstr = s.replace('T', ' ')
    return newstr


print(format_time())