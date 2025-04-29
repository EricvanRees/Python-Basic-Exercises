"""
Get the common items between two lists.
"""

list1 = ["1","2","3"]
list2 = ["3","4","5"]

def find_common_items(lista, listb):
  common_items = []
  for item in lista:
    if item in listb:
      common_items.append(item)
      
  return common_items

print(find_common_items(list1, list2))