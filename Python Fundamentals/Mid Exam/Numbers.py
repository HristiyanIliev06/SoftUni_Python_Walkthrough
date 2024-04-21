sequence = list(map(int,input().split()))
command = input().split()
index = 0

while command[0]!='Finish':
    if command[0]=='Add':
        sequence.append(int(command[1]))
    elif command[0]=='Remove':
        sequence.remove(int(command[1]))
    elif command[0]=='Replace':
        index = sequence.index(int(command[1]))
        sequence.pop(index)
        sequence.insert(index, int(command[2]))
    elif command[0]=='Collapse':
        for num in sequence:
            if num<int(command[1]):
                sequence.remove(num)
    command = input().split()
    
print(*sequence)