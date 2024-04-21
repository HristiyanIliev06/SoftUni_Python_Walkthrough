budget = float(input())
flour = float(input())
eggs = 0.75*flour
milk = 1.25*flour/4

loaves=0
colored_eggs = 0
loafrd = 0

while(budget>0.1):
    budget-=(flour+eggs+milk)
    loaves+=1
    colored_eggs+=3
    loafrd+=1
    if loafrd==3:
        loafrd=0
        eggs-=(loaves-2)
        
print(f"You made {loaves} loaves of Easter bread! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.")
