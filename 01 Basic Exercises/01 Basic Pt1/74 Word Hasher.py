"""
Write a Python program to hash a word.
"""

def hash_word(a_word):
  return str(hash(a_word))

print(hash_word("abc"))
print(hash_word("pindakaas"))
print(hash_word("knuffelbeer"))