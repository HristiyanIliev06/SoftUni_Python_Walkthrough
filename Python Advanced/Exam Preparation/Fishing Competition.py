n = int(input())        #75/100
fishing_area = [[item for item in input()] for _ in range(n)]
row = 0
column = fishing_area[0].index('S')
fishing_area[0].pop(column)
fishing_area[row].insert(column, '-')
fish = 0

try:
    while True:
        command = input()
        if command=="collect the nets":
            if fish>=20:
                print("Success! You managed to reach the quota!")
            else:
                print(f"You didn't catch enough fish and didn't reach the quota! You need {20-fish} tons of fish more.")
                
            if fish>0:
                print(f"Amount of fish caught: {fish} tons.")
                
            fishing_area[row].pop(column)
            fishing_area[row].insert(column, 'S')
            [print(''.join(line)) for line in fishing_area]
            break
        
        if command=="up" and row==0:
            row=n-1
        elif  command=="up" and row!=0:
            row-=1
        elif command=="down" and row==n-1:
            row=0
        elif  command=="down" and row!=n-1:
            row+=1
        elif command=="right" and column==n-1:
            column=0
        elif command=="right" and column!=n-1:
            column+=1
        elif command=="left" and column==0:
            column=n-1
        elif command=="left" and column!=0:
            column-=1
            
        if fishing_area[row][column].isdigit():
            fish+=int(fishing_area[row][column])
            fishing_area[row].pop(column)
            fishing_area[row].insert(column, '-')
            
        if fishing_area[row][column]=="W":
            print(f"You fell into a whirlpool! The ship sank and you lost the fish you caught. Last coordinates of the ship: [{row},{column}]")
            break
except RuntimeError:
    pass
            