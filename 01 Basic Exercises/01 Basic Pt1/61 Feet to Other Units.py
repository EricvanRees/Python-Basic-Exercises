"""
Write a Python program to convert the distance (in feet) to inches, yards, and miles.
"""

def convert_dist(amount, unity):
  if unity == "inches":
    inches = amount * 12
    return f"{amount} feet equals {inches} inches"
  elif unity == "yards":
    yards = amount / 3
    return f"{amount} feet equals {yards:.2f} yards"
  elif unity == "miles":
    miles = amount /5280
    return f"{amount} feet equals {miles:.2f} miles"
  else:
    return False
  
print(convert_dist(100, "inches")) 
print(convert_dist(100, "yards")) 
print(convert_dist(100, "miles")) 
