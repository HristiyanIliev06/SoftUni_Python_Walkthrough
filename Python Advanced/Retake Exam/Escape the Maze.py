n = int(input())    #100/100
maze = [[item for item in input()] for _ in range(n)]

health = 100
row = 0
column = 0

for i in range(len(maze)):
    if 'P' in maze[i]:
        row = i
        column = maze[i].index('P')
        maze[row][column] = '-'
        break

def isfree_to_move(direction:str):
    if 0<row and direction=='up':
        return True
    elif row<(n-1) and direction=='down':
        return True
    elif 0<column and direction=='left':
        return True
    elif column<(n-1) and direction=='right':
        return True
    
    return False
    
def movement(row:int, column:int, direction:str):
    if direction=='up' and isfree_to_move(direction):
        row-=1
    elif direction=='down' and isfree_to_move(direction):
        row+=1
    elif direction=='left' and isfree_to_move(direction):
        column-=1
    elif direction=='right' and isfree_to_move(direction):
        column+=1
        
    return row, column
        
while True:
    command = input()
    row, column = movement(row, column, command)
    
    if maze[row][column] =='M':
        health-=40
        maze[row][column] ='-'
        if health<=0:
            maze[row][column] ='P'
            health = 0
            print("Player is dead. Maze over!")
            break
        
    if maze[row][column] == 'H':
        health+=15
        if health>100:
            health=100
        maze[row][column] ='-'
        continue
        
    if maze[row][column] == 'X':
        maze[row][column] = 'P'
        print("Player escaped the maze. Danger passed!")
        break
    
print(f"Player's health: {health} units")
for each_row in maze:
    print(''.join(each_row))
            
    