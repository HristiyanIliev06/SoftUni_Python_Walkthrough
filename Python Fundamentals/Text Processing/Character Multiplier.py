enter = input().split()
multiplied_total = 0
string1 = enter[0]
string2 = enter[1]

if len(string1)==len(string2):
    for i in range(len(string1)):
        multiplied_total+=ord(string1[i])*ord(string2[i])
else:
    for i in range(min(len(string1), len(string2))):
        multiplied_total+=ord(string1[i])*ord(string2[i])
    for i in range(abs(len(string1)-len(string2))):
        if max(len(string1), len(string2))==len(string1):
            multiplied_total+=ord(string1[i])
        else: multiplied_total+=ord(string2[i])
print(multiplied_total)