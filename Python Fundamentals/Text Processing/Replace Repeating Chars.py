string = input()
checker = ''
new_string = ""

for i in range(len(string)):
    if checker!=string[i]:
        checker = string[i]
        new_string+=checker
        
print(new_string)