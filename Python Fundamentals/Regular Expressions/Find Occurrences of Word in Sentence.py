import re
text = input()
word = input()
words = re.findall(f'\\b{word}\\b', text, re.I)
print(len(words))