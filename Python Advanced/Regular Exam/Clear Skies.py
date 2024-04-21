n = int(input())    #100/100
airspace=[[item for item in input()] for _ in range(n)]
armor = 300
enemies = 4

def localize():
    for i in range(n):
        for j in range(n):
            if airspace[i][j]=='J':
                return i, j
            

def moves(command:str, current_loc):
    row, column = current_loc
    airspace[row][column]='-' 
    
    if command=='up':
        row-=1
    elif command=='down':
        row+=1
    elif command=='left':
        column-=1
    elif command=='right':
        column+=1
        
    new_location = airspace[row][column]     
    return new_location, row, column


while armor>0 and enemies>0:
    location, row, column = moves(input(), localize())
    
    if location=='E':
        armor-=100
        enemies-=1
    elif location=='R':
        armor=300 
    airspace[row][column]='J'
    
if enemies==0:
    print("Mission accomplished, you neutralized the aerial threat!")
elif armor==0:
    print(f"Mission failed, your jetfighter was shot down! Last coordinates [{row}, {column}]!")

airspace[row][column]='J'

[print(''.join(airspace[i])) for i in range(n)]     