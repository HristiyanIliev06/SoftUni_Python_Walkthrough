current_version = list(map(int,input().split('.')))
new_version = []

if current_version[2] == 9:
    new_version.append(0)
    if current_version[1] == 9:
        new_version.append(0)
        new_version.append(current_version[0]+1)
    elif current_version[1] < 9: 
        new_version.append(current_version[1]+1)
        new_version.append(current_version[0])
elif current_version[2] < 9:
    new_version.append(current_version[2]+1)
    new_version.append(current_version[1])
    new_version.append(current_version[0])
new_version.reverse()
       
print('.'.join(map(str, new_version)))