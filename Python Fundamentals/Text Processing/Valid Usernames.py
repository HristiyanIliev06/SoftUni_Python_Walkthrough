usernames = input().split(', ')
valids = []
approval = True
for username in usernames:
    if 3<len(username)<=16:
        for char in username:
            if not char.isalpha() and not char.isdigit() and char!='-' and char!='_':
                approval = False
                break
            else: approval = True
        if approval==True: valids.append(username)
            
            
print('\n'.join(valids))