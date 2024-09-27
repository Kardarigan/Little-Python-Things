people = 60
enemies= 1000
Miner=0
pyadenezam=15
savarenezam=10
soldiers = (int(pyadenezam)+int(savarenezam))
gold = 0
coin = 0
spy = 0
number =1
Day='Daily report'
Day=Day.center(50)
raid = True
order = ['soldier','attack','miner','mint(coin)','building']
while enemies and raid and soldiers:
    number += 1
    gold+=int(Miner)
    print('Day ' + str(int(number)-1))
    print(('_'*50)+'\n')
    print(Day)
    print('_'*50)
    if coin < 0:
        print('''You owe a debt to the World Bank!
Please pay it as soon as possible, or your soldiers will be reduced.''')
        pyadenezam -= 10
        savarenezam -= 5
    print('''
You have ''' + str(coin) + ' coin.')
    print ('You have ' + str(people) + ' people.')
    print ('You have ' + str(soldiers) + ' soldiers.')
    print('You have ' + str(spy) + ' spy.')
    print('You have ' + str(gold) + ' gold.')
    print('_'*50)
    print()
    print(order)
    dastor=input('My King, what do you order?')
    if dastor == 'soldier':
        P=input('How many infantry(witout horse) do you want?(1coin)')
        if int(P) > people:
            print('You lack ' +str(int(P)-people)+' people')
        else:
            pyadenezam +=int(P)
            soldiers += int(pyadenezam)
            people -= int(P)
            coin -= 1 * int(P)
        S=input('How many cavalry(with horse) do you want?(2coin)')
        if int(S) > int(people):
            print('You lack ' +str(int(S)-people)+' people')
        else:
            savarenezam +=int(S)
            soldiers += int(savarenezam)
            people -= int(S)
            coin -= 2*int(S)
        Spy=input('Do you want spy?30coin(yes,no)')
        if Spy == 'yes':
            mission = input('''what's you spy mission?(1 or 2)
mission1)suicide bomber
mission2)Obtaining enemy intelligence''')
            if mission =='1':
                enemies -=20
                spy = 0
            elif mission =='2':
                print('Your enemi has '+ str(enemies)+' soldiers.')
                print('Your spy was detected and killed by the enemy.')
    elif dastor == 'attack':
        if int(soldiers) >= int(enemies):
            enemies-=(1* int(pyadenezam))
            enemies-=(2* int(savarenezam))
            pyadenezam -= 8
            savarenezam -= 10
            if pyadenezam <= 0:
                pyadenezam = 0
            elif savarenezam <= 0:
                savarenezam = 0
            soldiers += (int(pyadenezam)-8)+(int(savarenezam)-10)
        elif int(soldiers) < int(enemies):
            enemies-=(1* int(pyadenezam))
            enemies-=(2* int(savarenezam))
            pyadenezam -= 10
            savarenezam -=12
            if pyadenezam <= 0:
                pyadenezam = 0
            elif savarenezam <= 0:
                savarenezam = 0
            soldiers += (int(pyadenezam)-10)+(int(savarenezam)-12)
    elif dastor == 'miner':
        M = input('How many miner do you want?')
        Miner += int(M)
        people-=int(M)
    elif dastor == 'mint(coin)':
        Co=input('To get coin type(get)')
        Co = Co.lower()
        if Co == 'get':
            coin += gold
            gold = 0
    elif dastor == 'building':
        big=input('How many big house do you want?60coin(30people)')
        small=input('How many small house do you want?20coin(10people)')
        people += int(big)*30
        people += int(small)*10
        if small:
            coin -= 20*int(small)
        if big:
            coin -= 60*int(big)
    if soldiers<=0:
        print('You lose!!!')
        raid = False
    elif int(enemies)<=0:
        print('You win and press enter to start new war!!!')
        pyadenezam += 15
        savarenezam += 10
        enemies += (int(soldiers)*2)+20