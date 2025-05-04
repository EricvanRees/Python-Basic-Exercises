"""
Write a Python program that prints long text, converts it to a list, and prints all the words and the frequency of each word.
"""

text = "FC Barcelona heeft zaterdag tegen La Liga-hekkensluiter Real Valladolid geen kleerscheuren opgelopen in de strijd om de Spaanse landstitel. De al gedegradeerde thuisclub kwam verrassend op voorsprong, maar na de invalbeurt van Frenkie de Jong stelde Barça orde op zaken (1-2)."

def word_freq(text):  

  words = text.split(" ")
  mylist = list(words)
  count_dict = {}
  for word in mylist:
    print(word)
    if count_dict.get(word) is not None:
      count_dict[word] += 1
    else:
      count_dict[word] = 1
      
  return {k: v for k, v in sorted(count_dict.items(), key=lambda item: item[1], reverse=True)}

print(word_freq(text))

