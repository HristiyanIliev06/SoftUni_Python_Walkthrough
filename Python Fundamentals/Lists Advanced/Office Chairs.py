rooms = int(input())
remaining_chairs = 0
needed_chairs = 0
marker = 0

for room in range(1, rooms+1):
    info = input().split()
    if len(info[0])>int(info[1]):
        remaining_chairs+=len(info[0])-int(info[1])
    elif len(info[0])<int(info[1]):
        needed_chairs+=int(info[1])-len(info[0])
        marker = needed_chairs
        print(f"{needed_chairs} more chairs needed in room {room}")
        needed_chairs = 0
        
if marker==0: print(f"Game On, {remaining_chairs} free chairs left")