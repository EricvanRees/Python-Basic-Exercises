"""
Write a Python program that converts seconds into days, hours, minutes, and seconds.
"""

def convert_time(amount, unit):
  if unit == "days":
    days = amount / 86400
    return f"{amount} seconds is equal to {days:.2f} days"
  elif unit == "hours":
    hours = amount / 3600 
    return f"{amount} seconds is equal to {hours:.2f} hours"
  elif unit == "seconds":
    return f"{amount} seconds is equal to {amount} seconds"
  else:
    return False
  
  
print(convert_time(10000, "days"))
print(convert_time(10000, "hours"))
print(convert_time(10000, "seconds"))
