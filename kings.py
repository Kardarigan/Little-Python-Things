B = None
people = 60
enemies= 1000
x =0
Miner=0
pyadenezam=15
savarenezam=10
soldiers = (int(pyadenezam)+int(savarenezam))
gold = 0
coin = 0
spy = 0
number =0
Day='Daily report'
Day=Day.center(50)
raid = True
order = ['soldier','attack','miner','bank','building']
name = input('Helo my king welcome to your own city!First please type your name ==> ')
if name:
    input('Good lets start!!!')
    input('In this game you are the king of this city and You will rule for 10,000 days')
    print()
    print()
print('                   Daily report')
print('__________________________________________________')
print()
print('You have 0 coin.')
print('You have 60 people.')
print('You have 25 soldiers.')
print('You have 0 gold.')
print('__________________________________________________')
print()
print('''['soldier', 'attack', 'miner', 'bank', 'building']''')
l=input('My King '+name+', what do you order?(press enter to skip or type L to learn the game)')
if l == 'L':
    input('''In this game you type commends in the list and after the commends, you get daily report.
          at First 'miner'is  more important than others.''')
while enemies and raid and soldiers and number!= 10001:
    soldiers = (int(pyadenezam)+int(savarenezam))
    number += 1
    gold+=int(Miner)
    print('\n'+('_'*50)+'\n')
    print('                      Day ' + str(int(number)))
    print(('_'*50)+'\n')
    print(Day)
    print('_'*50)
    if coin < 0:
        print('''You owe a debt to the World Bank!
Please pay it as soon as possible, or your soldiers will be reduced.''')
        soldiers = (int(pyadenezam)-10) + (int(savarenezam)-5)
        pyadenezam -=10
        savarenezam -= 5
    print('''
You have ''' + str(coin) + ' coin.')
    print ('You have ' + str(people) + ' people.')
    print ('You have ' + str(soldiers) + ' soldiers.')
    print('You have ' + str(gold) + ' gold.')
    print('_'*50)
    print()
    print(order)
    dastor=input('My King '+str(name)+', what do you order?')
    if dastor == 'soldier':
        P=input('How many infantry(witout horse) do you want?(1coin)'+ ' ('+str(coin)+')')
        if int(P) >= people-1:
            print('You lack ' +str(int(P)-people)+' people')
        else:
            pyadenezam +=int(P)
            people -= int(P)
            coin -= 1 * int(P)
        S=input('How many cavalry(with horse) do you want?(2coin)'+ ' ('+str(coin//2)+')')
        if int(S) > int(people):
            print('You lack ' +str(int(S)-people)+' people')
        else:
            savarenezam +=int(S)
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
        if int(M) >= people-1:
            print('you lack ' + str(int(M)-people) + ' people.')
        else:
            Miner += int(M)
            people-=int(M)
    elif dastor == 'bank':
        Co=input('''1) loan
2) coin''')
        if Co == '2':
            coin += gold
            gold = 0
        elif Co == '1':
            if B != None:
                input('''You dont't premishen to do that''')
            else:
                print()
                B=input('''1) 3000coin(5day)[+20%]
2)10000coin(5day)[+20%]
3) 1000000coin(5 day)[+20%]''')
                if B == '1':
                    coin +=  3000
                    x = 0
                elif B == '2':
                    coin += 10000
                    x = 0
                elif B == '3':
                    coin+= 1000000
                    x = 0
    elif dastor == 'building':
        big=input('How many big house do you want?60coin(30people)'+ ' ('+str(int(coin)//60)+')')
        if big:
            coin -= 60*int(big)
            people += int(big)*30
        small=input('How many small house do you want?20coin(10people)'+ ' ('+str(int(coin)//20)+')')
        if small:
            coin -= 20*int(small)
            people += int(small)*10
    if soldiers<=0:
        print('You lose!!!')
        raid = False
    elif int(enemies)<=0:
        input('You win and press enter to start new war!!!')
        pyadenezam += 15
        savarenezam += 10
        enemies += (int(soldiers)*2)+20
    if x == 5:        
        if B == '1':
            coin -= 3600
            x = 0
            B = None
        elif B == '2':
            coin -= 12000
            x = 0
            B = None
        elif B == '3':
            coin -= 1200000
            x = 0
            B = None
    x += 1