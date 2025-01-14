enemies = 200
soldiers = 150
coin = 15
rocket = 0
spy = 0
orders = ['attack' , 'defense' , 'buy soldiers' , 'sell soldiers' , 'buy rocket' , 'use rocket' , 'buy spy' , 'use spy' , 'peace']
raid = True

while raid:
    
    print ('soldiers')
    print (soldiers)
    print ('enemies')
    print (enemies)
    print ('coin')
    print (coin)
    print ('rocket')
    print (rocket)
    print ('spy')
    print (spy)

    print (orders)
    dastoor = input('What order do you have?')
    if dastoor == 'attack':
        if soldiers == enemies:
            enemies -= 10
            soldiers-= 10

        if soldiers <= enemies:
            enemies -=10
            soldiers -=20

        elif soldiers >= enemies :
            enemies -= 20
            soldiers -= 10
    
    if dastoor == 'defense':
        if enemies == soldiers:
            enemies-=5
            
        elif enemies > soldiers:
            soldiers -=5
            enemies -=5

        elif enemies < soldiers:
            enemies -= 10

    if dastoor == 'buy soldiers' and coin > 0:
        coin-=1
        soldiers+=10

    if dastoor == 'sell soldiers' and soldiers >= 10:
        soldiers -=10
        coin += 1
   
    if dastoor == 'buy rocket' and coin > 4:
        coin -= 4
        rocket += 1

    if dastoor == 'use rocket' and rocket > 0:
        rocket -= 1
        enemies -= 50
    
    if dastoor == 'buy spy'and coin >= 3:
        coin -= 3
        spy += 1

    if dastoor == 'use spy' and spy > 0:
        spy-=1
        enemies-=30

    if dastoor == 'peace' and enemies == soldiers:
        if enemies == soldiers:
            print ('the war is done')
            raid = False
        else:
            print('enemy refused our peace request!')

    if coin == 0:
        print ("we haven/'t got any coin _ tap enter to continue")



    if enemies < 1:
        print('we win! _ tap enter to go in next war')
        soldiers+=100
        enemies+=2*soldiers
        coin+=15

    elif soldiers < 1:
        print('we loss!.')
        raid = False

print('game over')