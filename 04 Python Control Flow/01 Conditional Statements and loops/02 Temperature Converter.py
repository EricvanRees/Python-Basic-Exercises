"""
Write a Python program to convert temperatures to and from Celsius and Fahrenheit.

[ Formula : c/5 = f-32/9 [ where c = temperature in celsius and f = temperature in fahrenheit ]

Expected Output :

60°C is 140 in Fahrenheit
45°F is 7 in Celsius
"""

def temp_converter(a_num, unity):
  if unity == "cel":
    fah = (int(a_num) * 9/5) + 32
    return fah
  else:
    cel = (int(a_num) - 32) * 5/9
    return cel
  
print(temp_converter(45, "fah"))

  
  