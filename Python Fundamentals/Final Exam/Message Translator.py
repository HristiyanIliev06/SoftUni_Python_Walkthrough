import re
n = int(input())        # 100/100
pattern = r'\![A-Z]{1}[a-z]{2,}\!\:\[[a-zA-Z]{8,}\]'
def Translate(verify:str):
    separate = verify.split('!')
    command = separate[1]
    separate = separate[2].split('[')
    separate = separate[1].split(']')
    message = separate[0]
    print(f'{command}:', end =' ')
    for i in range(len(message)):
        if i!=len(message)-1:
            print(ord(message[i]), end=' ')
        else: print(ord(message[i]))
        
for _ in range(n):
    code = input()
    verification = re.fullmatch(pattern,code)
    if verification==None: print("The message is invalid")
    else: Translate(verification.group())