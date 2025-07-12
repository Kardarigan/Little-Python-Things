# Initial values
nDays = 10
nCoins = 100
nPeople = 30
owned_buildings = []
nEnemy = 2000

#daily report
def daily_report():
    print('__________________________________________________')
    print('____________________NEWS PAPER____________________')
    print('__________________________________________________')
    print('coins = ' , nCoins)
    print('Day: ' , nDays + 1)
    print('number of people = ' , nPeople)

#building
def building():
    global nCoins
    global nPeople
    global nPowerplant
    build_work = input('Do you want to build anything today [y/n]?')
    building_list = ['1.power plant(makes electricity and every day you will get 100 coin) , value = 100 coin' , 
                     '2.small house(add 2 people to your city) , value = 20 coin' , 
                     '3.medium house(add 5 people to your city) , value = 50 coins' , 
                     '4.big house(add 10 people to your city) , value = 100 coins']
    if build_work == 'n':
        return
    elif build_work == 'y' :
        print(building_list)
        building_choice = input('enter the name of the building you want to make: ')
        #power plant
        if building_choice == '1':
            owned_buildings.append('power plant')
            nCoins = nCoins - 100
            nPowerplant = owned_buildings.count('power plant')
        #small house
        elif building_choice == '2':
            nPeople = nPeople + 2
            nCoins = nCoins - 2
        #medium house
        elif building_choice == '3':
            nCoins = nCoins - 50
            nPeople = nPeople + 5
        #big house
        elif building_choice == '4':
            nCoins = nCoins - 100
            nPeople = nPeople + 10
    else:
        print('invalid input')
        return
army_owned = []
nSoldier = 0
nRocket = 0
#enemy move
def enemy_move():
    global army_buy
    global nSoldier
    global nPeople
    global nCoins
    nEnemy = 100
    if nDays == 0:
        print('!ENEMY HAS COME USE YOUR COINS TO GET READY FOR THE WAR!')
        print('you can do the fowlloing thing to upgrade your army')
        army_buy_option = ['1.make your people a soldier' , '2.rocket , value = 50 coins']
        print(army_buy_option)
        army_buy = input('enter the name of the thing you want to buy for the army: ')
        if army_buy == '1':
            number_soldier_add = int(input('enter the number of people you want to make soldier,you have ' + str(nPeople) + ' number of people.'))
            if number_soldier_add > 0:
                if nPeople < number_soldier_add:
                     nSoldier = nSoldier + nPeople    
                else:
                    nPeople = nPeople - number_soldier_add
                    nSoldier = nSoldier + number_soldier_add
                    army_owned.append(nSoldier)
        if army_buy == '2':
            n_rocket_add = int(input('how many rockets do you want to buy?')  )
            if n_rocket_add > 0:
                
                if nCoins < (n_rocket_add * 50):
                    print('you dont have that much coins')
                    return
                else:
                    nCoins = nCoins - (50 * n_rocket_add)
                    print('you have ' , nRocket , ' rockets.')
                    army_owned.append(nRocket)   
#war
def war():
    global nSoldier
    global nEnemy
        
    print('IT IS TIME TO FIGHT USE THINGS YOU HAVE BOUGHT FOR THE ARMY')
    print('these are the things you have to use: ',army_owned)
    print('what do you want to use of your army? if you use? you can use your 1.soldiers or your 2.rockets\nthe enemy has 2000 people and you have ' , nSoldier , 'soldiers you also have ' , nRocket , 'rockets\nif you use your soldier ech one will kill 2 of your enemys and if you use your rockets each one will kill 100 people of your enemy.')
              
    war_use = input()
    if war_use == '1':
        nSoldier_use = int(input('enter the number of soldiers you want to send to the war now: '))
        nEnemy = nEnemy - (nSoldier_use * 2)
        nSoldier = nSoldier - (nSoldier_use)
        print('you have killed some of your enemy people now the nenmy has ' , nEnemy , ' people left now you have ' , nSoldier , 'soldiers left')
    if war_use == '2':
        nRockets_use = int(input('enter the number of rockets you want to use: '))
        nEnemy = nEnemy - (nRockets_use *100)


#game
for i in range(10):
    
    nDays = nDays - 1
    daily_report()
    building()
    nCoins = nCoins + (nPowerplant * 100)
    if nDays == 0:
        while (nSoldier > 0) or (nEnemy > 0):
            enemy_move()
            war()
