welcome=input('''welcome to game of war
\tshall we start?''')
name=input('''Please Enter Your Game Name(dont use word 'KING')
:''')

battle=True

money=10
army=100
army_health=100
enemy=150
rocket=0
hospital=0
train_area=0

build=''
buy=''
enemyfile=''
game=''

if welcome =='yes':
    home_page =input('''======================================================game=of=war======================================================
__________________________
Have a tutrial
________________________
Go to game
______________________
change name                                                                          ~~~~~
___________________                                                                 / *  *\\
                                                                              \t    \_____/
                                                                                       |
                                                                                       | 
                                                                                      /|\
                                                                          \t\t\t\t  / | \\                                                     
                                                                          \t\t\t /  |  \\   
                                                                                   /   |  _\\_
                                                                                       |   |_|
                                                                                       |     ||
                                                                                       /\    | 
                                                                                      /  \   |
                                                                                     /    \ 
                                                                                    /      \ 
                                                                                   /        \\
                                                                                                        _/          \_
choose :''')
                                                        
if home_page == '3':
    print(f'Sorry, it is not possible to change your name. Your name is {name}.')

elif home_page == '1':
    input('Tutorial coming soon...')

elif home_page == '2':
    game = input(f'''King {name}, there is an enemy close to us. What should we do?
    [1. Place a camp (recommended) to fight, 2. Run back home]: ''')
    if game == '1':
        battle = True
    else:
        print('ruuuuuuuuuuuuuuuuun!')

while battle:

    print(f'Money: {money}\nArmy: {army}\nArmy Health: {army_health}\nEnemies: {enemy}\nRockets: {rocket}\nHospitals: {hospital}\nTraining Areas: {train_area}')
    
    camp = input('''Now what? [1. Earn money by mining, 2. Attack, 3. Buy things, 4. Build things, 5. Use a hospital to heal, 6. Use an army training area, 7. Use a rocket]: ''')

    if camp == '1':
        money += 5
        army_health -= 10

    elif camp == '2' and enemy >= army:
        army -= 99
        print('You lost :(')
        battle = False

    elif camp == '3':
        buy = input('Buy men for $3, Buy rocket for $5 (men/rocket): ')
        if buy == 'men' and money >= 3:
            army += 20
            money -= 3
        elif buy == 'rocket' and money >= 5:
            rocket += 1
            money -= 5

    elif camp == '4':
        build = input('Build a hospital for $5, Build an army training area for $10 (hospital/train area): ')
        if build == 'hospital' and money >= 5:
            hospital += 1
            money -= 5
        elif build == 'train area' and money >= 10:
            train_area += 1
            money -= 10

    elif camp == '5' and hospital > 0:
        money -= 1
        army_health += 50

    elif camp == '6' and train_area > 0:
        money -= 2
        army += 15

    elif camp == '7' and rocket > 0:
        rocket -= 1
        enemy -= 20

    if army_health <= 0:
        print('You lost :(')
        battle = False

    if army >= enemy:
        enemyfile = input(f'''Hi there King {name}, we see you have upgraded your army for conquering our world...
    We request peace. From King Enemy.
    Accept peace? (yes/no): ''')
        if enemyfile.lower() == 'yes':
            print('You were betrayed by the enemy! Hahaha, you fell for my little trick.')
            print('You lost :| Never trust anyone in a game.')
            battle = False
        elif enemyfile.lower() == 'no':
            print('Computer: You did the right thing.')
            print('YOU WON')
            battle = False