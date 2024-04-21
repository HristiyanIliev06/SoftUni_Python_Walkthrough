deck = input().split(', ')
command = []
num = int(input())

def Remove_at(command:list):
    if -1<int(command[1]) <= len(deck):
        deck.pop(int(command[1]))
        return 'Card successfully removed'
    else: return 'Index out of range'   

for _ in range(num):
    command = input().split(', ')
    if command[0]=='Add':
        if command[1] not in deck:
            deck.append(command[1])
            print('Card successfully added')
        else: print('Card is already in the deck')
    elif command[0]=='Insert':
        if -1<int(command[1]) <= len(deck):
            if command[2] in deck:
                print('Card is already in the deck')
            else: 
                print('Card successfully added')
                deck.insert(int(command[1]), command[2])
        else: print('Index out of range')
    elif command[0]=='Remove':
        if command[1] in deck:
            deck.remove(command[1])
            print('Card successfully removed')
        else: print('Card not found')
    elif command[0]=='Remove At':
        print(Remove_at(command))
        
print(', '.join(deck))