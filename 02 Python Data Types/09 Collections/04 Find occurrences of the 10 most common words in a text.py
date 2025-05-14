"""
Write a Python program to find the occurrences of the 10 most common words in a given text.

Sample Output:
[('Python', 6), ('the', 6), ('and', 5), ('We', 2), ('with', 2), ('The', 1), ('Software', 1), ('Foundation', 1), ('PSF', 1), ('is', 1)]
"""

from collections import Counter

mytext = "Dat KPN en Ziggo samen de markt voor internetaansluitingen verdelen is niet langer vanzelfsprekend. Het klantenbestand van Ziggo krimpt al jaren en KPN groeit alleen door overnames. Odido en Delta zijn de lachende derde. Dat KPN en Ziggo samen de markt voor internetaansluitingen verdelen is niet langer vanzelfsprekend. Het klantenbestand van Ziggo krimpt al jaren en KPN groeit alleen door overnames. Odido en Delta zijn de lachende derde. In 2015 hadden Ziggo en KPN volgens de Autoriteit Consument & Markt (ACM) bijna het alleenrecht op de internetmarkt. Het marktaandeel van alle andere internetaanbieders bij elkaar kwam niet boven de 5 procent uit."

mytext_edited = mytext.split(" ")

ten_most_common_words = Counter(mytext_edited).most_common(10)
print(ten_most_common_words)
