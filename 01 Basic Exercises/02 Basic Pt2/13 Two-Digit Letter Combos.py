"""
Write a Python program to get all possible two-digit letter combinations from a 1-9 digit string.
string_maps = {
"1": "abc",
"2": "def",
"3": "ghi",
"4": "jkl",
"5": "mno",
"6": "pqrs",
"7": "tuv",
"8": "wxy",
"9": "z"
}
"""

def string_map():
  string_map = {}
  alphabet = "abcdefghijklmnopqrstuvwxyz"
  for i in range(1, 10):
    string_map[i] = alphabet[0:3]
    alphabet = alphabet[3:]
      
  return string_map

print(string_map())