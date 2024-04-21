string = input()
strength = 0
new_string = ""

for i in range(len(string)):
    if string[i]=='>':
        strength += int(string[i+1])
        new_string+='>'
    elif strength>0 and string[i]!='>': strength-=1
    else: new_string+=string[i]
          
print(new_string)