import random

def roll():
    max_num=6
    min_num=1
    number=random.randint(min_num,max_num)
    return number

while True:
    players=input("Enter the number for players (2,4) : ")
    players=int(players)
    if 2<= players <=4:
        break
    else:
        continue
max_score=50
point_table=[]
for i in range(players):
    point_table.append(0)
iterate=0    
print("Lets begin the game of dice : ")
# choice=int(input("Enter yes to roll the dice or no to quit (yes,no) : "))
check_point=0
while max(point_table)<max_score:
    if  iterate==0:
        my_choice=input("Do you want to roll or quit (r,q) : ")
        if my_choice=="r":
            check_point=roll()
            print(f"You got {check_point} on dice")
        elif my_choice=="q":
            break
        else:
            continue
        if check_point!=1:
            point_table[iterate]+=check_point
        else:
            point_table[iterate]=0
    elif iterate!= 0 :
        check_point=roll()
        print(f"Player {iterate} got {check_point} on dice.")
        if check_point!=1:
            point_table[iterate]+=check_point
        else:
            point_table[iterate]=0
    iterate=(iterate+1)%len(point_table)
print(f"User Points are : {point_table[0]}")
print(f"Player {point_table.index(max(point_table))} won the game.")   
print(point_table)             
    
                    
                  