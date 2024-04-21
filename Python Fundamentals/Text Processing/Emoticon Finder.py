text = input()
emoticons = list()

for i in  range(len(text)):
    if text[i]==":":
        emoticons.append(":"+text[i+1])
        
print('\n'.join(emoticons))