command = ''
while True:
    command = input()
    if command!='End':
        if command!="SoftUni":
            result = ""
            for char in command:
                result+=2*char
            print(result)
        else: continue
    else: break    