"""
Write a Python function to create an HTML string with tags around the word(s).
Sample function and result :
add_tags('i', 'Python') -> '<i>Python</i>'
add_tags('b', 'Python Tutorial') -> '<b>Python Tutorial </b>'
"""

def create_html(tag, text):
  if tag == 'i':
    return f"<i>{text}</i>"
  elif tag == 'b':
    return f"<b>{text}</b>"
  else:
    return False
  
print(create_html("i", "Python Tutorial"))
print(create_html("b", "Python Tutorial"))