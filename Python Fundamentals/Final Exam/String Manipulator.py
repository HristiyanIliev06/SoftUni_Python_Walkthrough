string = input()
def Translate(char:chr, replacement:chr):       # 100/100
    translated = ""
    for s in string:
        if s!=char: translated+=s
        else: translated+=replacement
    return translated

def Includes(substring):
    if substring in string: return True
    else: return False
    
def Start(substring):
    checkmarks = 0
    for i in range(len(substring)):
        if substring[i]==string[i]: checkmarks+=1
    if checkmarks==len(substring): return True
    else: return False
    
def Lowercase():
    return string.lower()

def FindIndex(char):
    last_index=0
    for index in range(len(string)):
        if string[index]==char:
            last_index = index
    return last_index           

def Remove(startIndex:int, count:int):
    Lstring = list(string)
    for _ in range(count):
        Lstring.pop(startIndex)
    return ''.join(Lstring)

while True:
    command = input().split()
    if command[0]=="End": break
    if command[0]=="Translate":
        print(Translate(command[1],command[2]))
    if command[0]=="Includes":
        print(Includes(command[1]))
    if command[0]=="Start":
        print(Start(command[1]))
    if command[0]=="Lowercase":
        print(Lowercase())
    if command[0]=="FindIndex":
        print(FindIndex(command[1]))
    if command[0]=="Remove":
        print(Remove(int(command[1]),int(command[2])))
    