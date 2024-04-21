size = [int(x) for x in input().split(',')]
rows = size[0]
columns = size[1]

matrix = [[input() for _ in range(columns)] for _ in range(rows)]

def print_matrix(matrix:list):
    last_state = ""
    for row in range(rows):
        for column in range(columns):
            last_state+=matrix[row][column]
        last_state+='\n'
    
    return last_state

likely_coords = ()
def localize_M(*args)->tuple:
    for row in range(rows):
        for column in range(columns):
            if matrix[row][column] =='M':
                return row, column
    
    return args
            
def count_C()->int:
    count = 0
    for row in range(rows):
        for column in range(columns):
            if matrix[row][column] =='M':
                count+=1
                
    return count
            
def out_of_cupboard(row:int, column:int):
    if row<0 or column<0 or row>rows or column>columns:
        return 'yes'
            
def movement(direction:str):
    row, column = localize_M()
    prow, pcolumn = localize_M()
    if direction=='up':
        row-=1
    if direction=='down':
        row+=1
    if direction=='left':
        column-=1
    if direction=='right':
        column+=1
        
    '''if out_of_cupboard(row, column=5)==0:
        row, column = localize()
        matrix[row][column]
        return "No more cheese for tonight!"'''
    
    return (row, column, prow, pcolumn)

commands = []    
while True:
    command = input()
    commands.append(command)
    if commands[-1] =='danger':
        break    

i = -1    
while True:
    i+=1
    command = commands[i]
    if command=='danger':
        print("Mouse will come back later!")
        break
    
    (row, column, prow, pcolumn) = movement(command)
    if out_of_cupboard=='yes':
        matrix[prow][pcolumn]='M'
        print("No more cheese for tonight!")
        break    
    elif matrix[row][column]=='T':
        matrix[row][column]=='M'
        print("Mouse is trapped!")
        break
    elif matrix[row][column]=='@':
        row = prow
        column = prow    
    elif matrix[row][column]=='C':
        matrix[prow][pcolumn]='*'
        matrix[row][column]='*'
        likely_coords = (row, column)
        localize_M(likely_coords)   
    elif count_C==0:
        matrix[row][column] = 'M'
        print("Happy mouse! All the cheese is eaten, good night!") 
        break  
   
print(print_matrix(matrix))    