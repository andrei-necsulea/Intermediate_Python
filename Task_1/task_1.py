'''
Write a function that will return the 5 most common words from Mickiewicz's work.

https://pastebin.com/raw/aAHeW5Pt
(copy and save to a text file what you will find at this link).

Hint: use the open() function, split() method, dictionary and loop.
'''

import string

def common_words(file):
   with open(file, "r", encoding="utf-8") as f:
        words = f.read().lower().split()

   dictionary = dict()

   for word in words:
     for char in string.punctuation:
        word = word.replace(char , "")
     dictionary[word] = dictionary.get(word , 0)+1

   sorted_items = sorted(dictionary.items(), key=lambda x: x[1], reverse=True)[:5]

   return tuple(key for key, value in sorted_items)

print(common_words("file.txt"))