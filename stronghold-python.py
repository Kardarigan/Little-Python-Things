#مردم ها
people = 10
builder = 0
wood_miner = 0
stone_miner = 0
iron_miner = 0
farmer = 0
the_hunter = 0
#منابع 
wood = 0
stone = 0
iron = 0
wheat = 0
wool = 0
house = 5
coin = 50

#دستور ها
order = ['buy builder' , 'buy wood miner' , 'buy stone miner' , ' buy iron miner' , 'buy farmer' , 'buy hunter' , 'buy 1 house' , 'buy 2 house' , 'buy 3 house']
resources = ['buy wood' , 'buy stone' , 'buy iron' , 'buy wheat' , 'buy wool' , 'sell wood' , 'sell stone' , 'sell iron' , 'sell wheat' , 'sell wool']

#کمک گرفتن
l = input('what do you order?(press enter to skip or type L to learn the game)')
if l == 'L':
    input('''In this game you type commends in the list and after the commends, you get a report.
          at First 'builder'is  more important than others.''')

while True:
    #اطلاعات
    print('                    report')
    print('__________________________________________________')
    print()
    print ('👨 peolpe:', people )
    print ('👷‍♂️ builder:', builder)
    print ('🪓 wood miner:', wood_miner)
    print ('⛏️ stone miner:', stone_miner)
    print ('⛏️ iron miner:', iron_miner)
    print ('🌲 farmer:', farmer) 
    print ('🏹 hunter:', the_hunter)
    print ('🪓 wood:', wood)
    print ('⛏️ stone:', stone)
    print ('⛏️ iron:', iron)
    print ('🌲 wheat:', wheat)
    print ('🐑 wool:', wool)
    print ('🏠 house:' , house)
    print ('💰 coin:' , coin)
    print('__________________________________________________')
    print()
    #پرینت دستور ها
    print (order)
    print(resources)
    #دستور برای خریدن مردم
    dastoor = input('What order to do?')
    if dastoor == 'buy builder':
        people -= 1
        builder += 1

    if dastoor == 'buy wood miner':
        people -= 1
        wood_miner += 1


    if dastoor == 'buy stone miner':
        people -= 1
        stone_miner += 1

    if dastoor == 'buy iron miner':
        people -= 1
        iron_miner +=1
   
    if dastoor == 'buy farmer':
        people -= 1
        farmer += 1

    if dastoor == 'buy hunter':
        people -= 1
        the_hunter += 1    

    #دستور برای خریدن خانه
    if dastoor == 'buy 1 house':
        if builder > 0:
            coin -= 10
            people += 2
            house += 1
        else:
            print('you dont have builder')
    
    elif dastoor == 'buy 2 house':
        if builder > 0:
            coin -= 20
            people += 4
            house += 2
        else:
            print('you dont have builder')
    
    elif dastoor == 'buy 3 house':
        if builder > 0:
            coin -= 30
            people += 6
            house += 3
    else:
        print('you dont have builder')

    #دستور برای خریدن منابع
    if dastoor == 'buy wood':
        coin -= 10
        wood += 10    

    if dastoor == 'buy stone':
        coin -= 10
        stone += 10

    if dastoor == 'buy iron':
        coin -= 10
        iron += 10

    if dastoor == 'buy wheat':
        coin -= 10
        wheat += 10

    if dastoor == 'buy wool':
        coin -= 10
        wool += 10

    #دستور برای فروختن منابع
    if dastoor == 'sell wood':
        wood -= 20
        coin += 5   

    if dastoor == 'sell stone':
        stone -= 20
        coin += 5

    if dastoor == 'sell iron':
        iron -= 20
        coin += 5

    if dastoor == 'sell wheat':
        wheat -= 20
        coin += 5

    if dastoor == 'sell wool':
        wool -= 20
        coin += 5    

    #گرفتن منابع روزانه
    if wood_miner > 0:
        wood += wood_miner * 10

    if stone_miner > 0:
        stone += stone_miner * 10

    if iron_miner > 0:
        iron += iron_miner * 10

    if farmer > 0:
        wheat += farmer * 5

    if the_hunter > 0:
        wool += the_hunter * 10   

    #تمام شدن مرحله قدیمی و شروع مرحله جدید
    if house == 50 :
        print('we finish the setp')
        print('for reward you get :')
        print('coin 50')
        print('wood 30')
        print('stone 30')
        print('iron 30')
        print('wheat 30')
        print('wool 30')
        coin += 50
        wood += 30
        stone += 30
        iron += 30
        wheat += 30
        wool += 30