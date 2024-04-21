required_experience = float(input())
battles = int(input())
earned_experience = 0.0
battle_num = 1

while required_experience>0 and battles>0:
    earned_experience = float(input())
    if battle_num%3==0:
        required_experience-=(earned_experience + 0.15*earned_experience)
    if battle_num%5==0:
        required_experience-=(earned_experience - 0.10*earned_experience)
    if battle_num%15==0:
        required_experience-=(earned_experience + 0.05*earned_experience)
    elif battle_num%3!=0 and battle_num%5!=0 and battle_num%15!=0:
        required_experience-=earned_experience
    battles-=1
    battle_num+=1
        
if required_experience<=0: print(f"Player successfully collected his needed experience for {battle_num-1} battles.")
else: print(f"Player was not able to collect the needed experience, {required_experience:.2f} more needed.")