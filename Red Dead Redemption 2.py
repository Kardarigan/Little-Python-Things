S = True

def start():
    print('''\t\t Welcome to Red Dead Redemption 2 - Train Heist!
You are Arthur Morgan, and Dutch has a plan.
Tonight, you and the gang are going to rob a train full of rich folks.''')
    choice_1()

def choice_1():
    s = int(input('1) Go with Dutch and Hosea to set the dynamite \n2) Stay at camp and wait'))
    if s == 1:
        dynamite()
    if s == 2:
        print('You missed the heist. Dutch is disappointed.')
        end()

def dynamite():
    print('''You ride with Dutch and Hosea in the night. Its cold and quiet.
You arrive at the railway and place the dynamite on the tracks.''')
    t = int(input('1) Light the fuse and blow the tracks \n2) Wait for Dutchs signal'))
    if t == 1:
        early_boom()
    if t == 2:
        signal_boom()

def early_boom():
    print('''You light the fuse too early!
The dynamite explodes before the train arrives.
You just destroyed empty tracks...''')
    print('The mission fails. Dutch is angry.')
    end()

def signal_boom():
    print('''You wait. Dutch raises his hand—the signal!
You light the fuse and BOOM! The train crashes and stops.
Time to board!''')
    board()

def board():
    print('''You jump onto the train with Lenny.
There are guards inside!''')
    g = int(input('1) Take cover and shoot \n2) Rush in with your knife'))
    if g == 1:
        shootout()
    if g == 2:
        knife_fail()

def shootout():
    print('''You and Lenny take cover and shoot carefully.
You take out the guards one by one.
You reach the private car where the safe is.''')
    s = int(input('1) Crack the safe slowly \n2) Blow it open with dynamite'))
    if s == 1:
        crack_safe()
    if s == 2:
        loud_boom()

def knife_fail():
    print('''You rush in, but the guards are ready.
You get shot before reaching them. You die.''')
    end()

def crack_safe():
    print('''You crack the safe quietly. Inside, theres gold and cash!
You and Lenny jump off the train and escape to the hills.''')
    print('Success! The gang is proud.')
    end()

def loud_boom():
    print('''You blow the safe, but the explosion is too loud.
More guards arrive from the back of the train.
A big shootout starts.''')
    b = int(input('1) Fight them \n2) Escape with what you have'))
    if b == 1:
        big_fight()
    if b == 2:
        escape()

def big_fight():
    print('''You fight bravely, but there are too many.
You get shot and fall off the train.''')
    end()

def escape():
    print('''You grab some money and jump off the train with Lenny.
You didnt get everything, but at least youre alive.''')
    print('success')
    end()

def end():
    print('''--- THE END ---
Thanks for playing!
Try again for different choices.''')

while S:
    start()
    S = False
