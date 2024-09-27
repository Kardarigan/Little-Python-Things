import random
print("You have been chosen as the military commander! Make proper decisions in order to win the war.")
raid = True
army_num = 10
enemy_num = 10
swords = 5
shields = 5
user = ""
c_defence =0
u_defence =0
while raid:
    print("Computers turn!")
    a_d = random.randint(1, 2)
    if a_d == 1:
        c_a = random.randint(1, 2)
        if c_a <= u_defence:
            print("The computer tried to kill",c_a,"people.\nYou had defended",u_defence,"people.\nNobody died")
            u_defence = u_defence - c_a
        elif c_a > u_defence:
            print("The computer tried to kill",c_a,"people.\nYou had defended",u_defence,"people.\n",(c_a-u_defence),"people died")
            army_num = army_num - (c_a - u_defence)
    elif a_d == 2:
        c_d = random.randint(1, 2)
        c_defence = c_defence+ c_d
        print("The computer has defended",c_d,"people.")
    user = input("What should we do? (attack, defend, check stats)\n")
    if user == "check stats":
                 print("Enemies army number:",enemy_num,"\nYour army number:",army_num,"\nSwords:",swords,"\nShields:",shields)
                 user = input("What should we do? (attack, defend, check stats)\n")
    if user == "defend":
        if shields > 0:
            if shields == 1:
                print("This costed 1 shield.")
                shields = shields-1
                u_defence += 1
            if shields > 1:
                shield_generator = random.randint(1, 2)
                print("This costed",shield_generator,"shield(s)")
                shields = shields-shield_generator
                u_defence = u_defence + shield_generator
        elif shields == 0:
            print("You are out of shields")
    if user == "attack":
        if swords > 0:
            t_kill = 0
            if swords == 1:
                t_kill = random.randint(1, 2)
                print("This costed 1 sword")
                if c_defence >= t_kill:
                    print("You tried to kill",t_kill,"people.\nThe computer had defended",c_defence,"people.\nNobody died")
                    c_defence = c_defence - t_kill
                elif c_defence < t_kill:
                    killed = t_kill - c_defence
                    print("You tried to kill",t_kill,"people.\nThe computer had defended",c_defence,"people.\nYou killed",killed,"people.")
            elif swords > 1:
                used_s = random.randint(1,2)
                if used_s ==1:
                    t_kill = random.randint(1, 2)
                    if c_defence >= t_kill:
                        print("You tried to kill",t_kill,"people.\nThe computer had defended",c_defence,"people.\nNobody died")
                        c_defence = c_defence - t_kill
                    elif c_defence < t_kill:
                        killed = t_kill - c_defence
                        print("You tried to kill",t_kill,"people.\nThe computer had defended",c_defence,"people.\nYou killed",killed,"people.")
                elif used_s == 2:
                    t_kill = random.randint(2, 3)
                    if c_defence >= t_kill:
                        print("You tried to kill",t_kill,"people.\nThe computer had defended",c_defence,"people.\nNobody died")
                        c_defence = c_defence - t_kill
                    elif c_defence < t_kill:
                        killed = t_kill - c_defence
                        print("You tried to kill",t_kill,"people.\nThe computer had defended",c_defence,"people.\nYou killed",killed,"people.")

    if army_num <= 0:
        print("you lose!")
        raid = False
    if enemy_num <= 0:
        raid = False
        print("you won!")
                    




            
        
    
        
    
