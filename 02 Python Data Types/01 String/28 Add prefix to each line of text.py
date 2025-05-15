"""
Write a Python program to add prefix text to all of the lines in a string.
"""

import textwrap

mytext = ''' \
Luuk de Jong kan niet geloven dat PSV woensdag de oppositie in de\n Eredivisie heeft overgenomen van Ajax. De Amsterdammers speelden gelijk\n bij FC Groningen door een tegentreffer in de 99e minuut, waardoor de\n Eindhovenaren plots de beste papieren voor de titel hebben.
'''

print(textwrap.indent(mytext, '***', lambda line: True))
