import random
Tass = ['''
   _________________________________     
  /                                /|
 /________________________________/ |
|                                 | |
|                                 | |
|                                 | |
|                                 | |
|                                 | |
|                                 | |
|                •                | |
|                                 | |
|                                 | |
|                                 | |
|                                 | |
|                                 |/
|_________________________________/
        ''','''
   _________________________________
  /                                /|
 /________________________________/ |
|                                 | |
|                                 | |
|                                 | |
|                •                | |
|                                 | |
|                                 | |
|                                 | |
|                                 | |
|                                 | |
|                •                | |
|                                 | |
|                                 |/
|_________________________________/
''','''
   _________________________________
  /                                /|
 /________________________________/ |
|                                 | |
|                                 | |
|                                 | |
|       •                         | |
|                                 | |
|                                 | |
|                •                | |
|                                 | |
|                                 | |
|                        •        | |
|                                 | |
|                                 |/
|_________________________________/
''',''' 
   _________________________________
  /                                /|                
 /________________________________/ |
|                                 | |
|                                 | |
|                                 | |
|       •                •        | |
|                                 | |
|                                 | |
|                                 | |
|                                 | |
|                                 | |
|       •                •        | |
|                                 | |
|                                 |/
|_________________________________/
''','''
   _________________________________
  /                                /|
 /________________________________/ |
|                                 | |
|                                 | |
|                                 | |
|       •                •        | |
|                                 | |
|                                 | |
|                •                | |
|                                 | |
|                                 | |
|       •                •        | |
|                                 | |
|                                 |/
|_________________________________/
''','''
   _________________________________
  /                                /|
 /________________________________/ |
|                                 | |
|                                 | |
|                                 | |
|       •                •        | |
|                                 | |
|                                 | |
|       •                •        | |
|                                 | |
|                                 | |
|       •                •        | |
|                                 | |
|                                 |/
|_________________________________/
''']
while True:
    input('Press enter to start!!!')
    tass_1 = random.choice(Tass)
    tass_2 = random.choice(Tass)
    tass_3 = random.choice(Tass)
    print(tass_1,tass_2,tass_3)
    if tass_1 == tass_2 == tass_3:
        if tass_1 == Tass[5]:
            print('🤯')
        else:
            print('Good job!!!')
    else:
        print('Try again!!!')