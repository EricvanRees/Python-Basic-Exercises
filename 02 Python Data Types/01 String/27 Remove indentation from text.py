"""
Write a Python program to remove existing indentation from all of the lines in a given text.
"""
import textwrap

mytext = '''
  Luuk de Jong kan niet geloven 
  dat PSV woensdag de oppositie 
  in de Eredivisie heeft overgenomen van Ajax. 
  De Amsterdammers speelden gelijk bij FC Groningen door een tegentreffer in  de 99e minuut, waardoor de Eindhovenaren plots de beste papieren voor de titel hebben.
'''
print()
print(textwrap.dedent(mytext))
print()
