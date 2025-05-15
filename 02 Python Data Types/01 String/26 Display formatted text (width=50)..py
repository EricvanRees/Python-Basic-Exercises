"""
Write a Python program to display formatted text (width=50) as output.
"""
import textwrap

mytext = "Luuk de Jong kan niet geloven dat PSV woensdag de oppositie in de Eredivisie heeft overgenomen van Ajax. De Amsterdammers speelden gelijk bij FC Groningen door een tegentreffer in de 99e minuut, waardoor de Eindhovenaren plots de beste papieren voor de titel hebben."

wrap_text = textwrap.fill(mytext, width=50)
print(wrap_text)
