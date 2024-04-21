first = input().split(' | ')        # 77/100
dictionary = {}
for item in first:
    pair = item.split(': ')
    key = pair[0]
    meanings = []
    if key not in dictionary:
        meanings.append(pair[1])
        dictionary[key]=meanings
    else:
        meanings.append(''.join(dictionary[key]))
        meanings.append(pair[1])  
        dictionary[key] = meanings
        
second = input().split(' | ')
command = input()
if command=="Test":
    for word in reversed(list(dictionary.keys())):
        if word in second:
            print(f'{word}:')
            for definition in dictionary[word]:
                print(f'-{definition}')
elif command=="Hand Over":
    for word in dictionary.keys():
        print(word, end=' ')