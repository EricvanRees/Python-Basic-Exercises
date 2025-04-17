"""
Write a Python program to convert all units of time into seconds.
"""

def convert_time(amount, unit):
  if unit == "seconds":
    return f"{amount} seconds equals {amount} seconds"
  elif unit == "minutes":
    seconds = amount * 60
    return f"{amount} minutes equals {seconds} seconds"
  elif unit == "hours":
    seconds = amount * 3600
    return f"{amount} hours equals {seconds} seconds"
  else:
    return False
  
print(convert_time(10, "minutes"))
print(convert_time(10, "seconds"))
print(convert_time(10, "hours"))