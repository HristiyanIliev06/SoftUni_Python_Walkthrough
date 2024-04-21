size = int(input())
board = [[item for item in input()]for _ in range(size)]
earnings = 100
row = 0
column = board[row].index('G')

"""def move(command, *position):
    row = position[0]
    column = position[1]
    board[row][column] = '-'
    if command== "up":
        row -= 1
    if command == "down":
        row += 1
    if command == "left":
        column-=1
    if command == "right":
        column+=1"""
    
def hunter():
    if row not in range(size) or column not in range(size) or earnings<=0:
        return "Alert!"
    
def comprehension(detected, earnings):
    if detected=='W': earnings+=100
    if detected=='P': earnings-=200
    if detected=='J': earnings+=100000
    return earnings