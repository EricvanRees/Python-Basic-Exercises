"""
Write a Python function to insert a string in the middle of a string.
Sample function and result :
insert_sting_middle('[[]]<<>>', 'Python') -> [[Python]]
insert_sting_middle('{{}}', 'PHP') -> {{PHP}}
"""

def insert_str(astr, str_to_move):
  return astr[:2] + str_to_move + astr[2:]
  
print(insert_str("{{}}", "Python"))
print(insert_str("[[]]", "PHP"))