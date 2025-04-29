"""
Create a 5x5 list of lists with row values ranging from 0 to 4.
"""

def create_list_of_lists():
  list_of_lists = []
  i = 0
  for _ in range(5):
    anylist = []
    for j in range(5):      
      anylist.append(i)
    i += 1
    list_of_lists.append(anylist)  
  
  return list_of_lists

print(create_list_of_lists())