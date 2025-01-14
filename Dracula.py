from random import randint

def start():
    print('''
      ⣀⣤⣤⣶⣾⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣶⣶⣦⣤⣀⠀⠀⠀⠀⠀
⣀⣴⣶⣿⣿⣿⣿⣿⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣴⣿⣿⣿⣿⣿⣿⣷⣦⣄⡀
⠁⠀⠀⠈⠉⠛⣿⣿⣿⣿⣿⣷⣦⣀⢠⣆⣸⡆⢀⣤⣾⣿⣿⣿⣿⣿⠟⠋⠉⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀ '⠿⠿⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⠿⠿⠏⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠻⣿⣿⣿⣿⠿⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
Greetings Lord Dracula

Wallacia is under siege by Ottomans and we lost our supremacy in the nation.
My lord, we need your help to save our Homeland.
''')

    choice = int(input('''Will you help us sire?

1- Yes Sargent shall we begin?
2- No Dude I don't help the people who don't believe me'''))
    
    if choice == 1:
        describe()
    elif choice == 2:
        end()
        

def describe():
    print('''I'm Greatfull for you help sire.
          
The Ottoman army is coming furthur, they killing men, enslave women and forcing children to join their army.
With this amount of army we have no chance to diffence against them.
You can stop them with your power sire.

Ottomans are coming and we have to split our army in two fronts.
first in Castle and city for defending last stand
and second in frontline for next battle''')
    
    choice = int(input('where you wanna be?\n1- Castle and City\n2- Frontline'))
    h = randint(0, 1)
    
    if choice == 1:
        if h == 0:
            battle_lost()
        elif h == 1:
            battle_win()
    elif choice == 2:
        if h == 0:
            siege_lost()
        elif h == 1:
            siege_win()




def end():
    print('''The game has been ended, while only your deeds remain for your legacy.
          
We hope you enjoyed this game and see you next time.
Also, you can play again if you are willing to.''')















    
start()

input('Press Enter to Close the Game...')