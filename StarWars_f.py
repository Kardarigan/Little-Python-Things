import random

def welcome_masage():
    print('Welcome to Star Wars Adenture Game!' )
    jedi_name=input('Enter your name of Jedi Knight : ')
    Jediname = jedi_name.title()
    print('Hello,',Jediname,'you have to stand against black holes and enemies.')
    print('Your mission is to restore peace to the galaxy.' + '\n')
        
def choose_action():
    print('Choose one of the options :')
    print('1) Attack')
    print('2) protection')
    print('3) Collection of weapons')
    print('4) Exit')

    Choice = input('Enter (1-4) your choice : ') 

    while Choice not in ['1', '2', '3', '4']:
            print('invalid choice!, please choose again.' )
            Choice = input('Enter (1-4) your choice : ')
            return int(Choice)
        
def attack():
    damage = random.randint(10, 30)
    print('You attacked and dealt damage to an enemy!', '+', damage)
    return damage
    
def protection():
    defence = random.randint(5, 15)
    print('You defended yourself and preserved your health!')
    return defence

def weapons():
    weapon = random.choice(['Lightsaber', 'Blaster', 'Force Push', 'Autoturret', 'AB-75 Bo-rifle', 'anakin skywalker\'s second lightsaber'])
    print('You found a new weapon! : ' + weapon , '+20')
    return weapon
        
def exit_massage():
    print('Thanks for playing! Your final score :', score )

def main():
    score = 0
    credit = 0
    health = 100
    welcome_masage()
    while health > 0 and credit < 100 :
        print('\nYour credit : ', credit)
        print('Your score : ', score) 
        print('Your health : ', health)
        
        Choice = choose_action()
        if Choice == 1:
            score += attack()
        elif Choice == 2:
            health += protection()
        elif Choice == 3:
            score += 20 
        elif Choice == 4:
            exit_massage() 
            break

        enemyAttack = random.randint(0,15)
        print('the enemy attacked, dealing', enemyAttack, 'damage.')
        health -= enemyAttack

        if health <= 0:
            print('Unfortunately, you failed! Your final score :',score)

if __name__ == "__main__":
    main()

    


 