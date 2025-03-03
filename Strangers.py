r= True
visitor=0
def game() :
    global visitor
    print('go turn on the radio')
    radio()
def radio():
    global visitor
    c=input('turn on the radio \t /*/''\n /*/turn on')
    if c == 'turn on':
        print('''good morning dear listeners,today we have had some reports about strange visitors among us
               government says that this issue is getting investigated,
               also about the global warming,today we experienced the hottest day of the history,may scientist find a way!!!''')  
        sleep()
    elif c == '':
        sleep()
def sleep():
    global visitor
    print('sleeping')
    q=input('bell ring')
    w=input('wake up \t /*/waking up')
    if w== 'waking up':
        man()
def man():
    global visitor
    print('should I check the window?  \t  /*/yes \n /*/ no')
    check=input('checking the window')
    if check== 'yes':
        print('I can see the street, it is kinda dead, it did not use to be like this,no worries after all I do not care' )
        conversation_one()
        
    elif check== 'no' :
        conversation_one()
def conversation_one():
    global visitor
    print('''I opened the door \n there is a man
          man:I guess you are alone here huh?
          you:who are you?
          man:who am I supposed to be?
          you:...
          man:ha ha ha ha!!! I LIVE NEAR YOU DUMB!!!
          you:YOU COULD HAVE SAID THAT!!!by the way, why are you here
          man:well I guess, can I come in?
          you:you have got a house dont ya?
          man: well yes you know...
          you:?
          man:people...people are changing
          you:strangers?
          man:well..um...so you listen to radio huh? or television
          you: I am a radio fan
          man:huh,old school, buy the way, people are getting sun stroke and they die because of the air quality 
          it is kinda bad huh? I am wearing a mask now but I might get suffocated if I stay outside
          my house I guess they are in my house
          you:what???
          man:...
          you:how am I soppose to believe that?arnt you one of theme?
          man:what the hell??
          you: you have a kid dont you?
          man:who cares about that brat!
          you:...
          man:please I am your neighbour
          you:...''')
    e=input('decide what to do? \t /*/let him in \n /*/shut the door ')
    if e == 'let him in' :
        letman()
        visitors+=1
    elif e== ' shut the door':
            print('that damn stranger...')
            checkroom()

def letman():
    global visitor
    print('''man:well I am happy about that, I am gonna stay at ypur living room
          you:just dont touch the pictures and other things''')
    sleep2()
def checkroom():
    global visitor
    print('I guess I am gonna have something')
    print('you can charge your energy with beer for talking')
    Drink=input('should I drink beer? \t /*/yes \n /*/no')
    if Drink== 'yes':
        drink()
    elif Drink== 'no':
        sleepextra()
def sleepextra():
    global visitor
    print('I should walk')

    sleep2()
def drink():
    global visitor
    R=input('drinking beer insert ...')
    if R == '...':

        energy=20
        beer=10

        for i in range(12):
               if R == '...': 
                     if beer <= 0:
                         energy+=0
                     else:
                         energy+=20
                         beer-=1
                     print(beer)
                     print(energy)

    print('I shall sleep')
    sleep2()
def sleep2():
    global visitor
    print('seconf night...')
    O=input('wake up? \t /*/ waking up')
    if O == 'waking up':
        conversation_2()
def conversation_2():
    global visitor
    print('''KNOCK!!!
          you:?
          woman:can I come in I do not resist?
           you:what??''')
    I=input('''let woman in?
            yes
            no''')
    if I == 'yes':
        print('woman:well I will remember this...')
        visitors+=1
        sleep3()
    elif I == 'no':
        print('woman: well I did not expected anyway')
        print('it is better')
        sleep3()
def sleep3():
    global visitor
    print('knock...')
    print('you:who is that???')
    print('''him:is..is that you?
          you:who are you???
          him:he he he...are you alone??
          you:...''')
    optionhim()
def optionhim():
    global visitor
    print('waht should you say???')
    ff=input('''yes...I am alone
             no there are people
             why?''')
    if ff == 'yes...I am alone':
        print('him:well...')
    elif ff == 'no there are people ':
        print('him:Oh')
    else:
        print('it is just a question...shouldent you answer me???')
        print('you:just do not bother me...')
        leave()
    def leave():
        print('him:well well.......')
    day3()
def day3():
    global visitor
    print('well I guess I have to watch some tv')
    tv()
def tv():
    global visitor
    print('''good morning dear veiwers...
          we warn you not to go out for your own sake because of the global warming
          about the strangers...new information has been revealed that strangers usually have dirty hands and bloody eyes...
          please check in people that cpme nearby for your own safety''')
    night3()
def night3():
    global visitor
    print('knock knock...')
    print('''you:again...
          woman:oh oh sorry 
          you:...
          woman:should I come...I gust need somewhere to rest please
          you:well
          woman:since things has changed...I need somewhere to rest...in daytime IT IS SO FREAKING HOT you see
          you:you see I need to let someone in but...
          woman:please...then let me in''')
    print('shouls you let her? YES OR NO ...')
    A=input('should you let her in?  ')
    if A == 'yes':
        woman3()
        visitors+=1
    else:
        print('...')
        drink2()
def woman3():
        global visitor
        print('woman:well I am so happy to hear that...I will stay in your kitchen')
        day4()
def drink2():
        global visitor
        N=input('drinking beer insert ...')
        if N == '...':

          energy=20
          beer=10

        for i in range(12):
               if N == '...': 
                     if beer <= 0:
                         energy+=0
                     else:
                         energy+=20
                         beer-=1
                     print(beer)
                     print(energy)
        day4()
def day4():
    global visitor
    print('''I should turn on the tv
          tv:dear veiwers...there are new signs that we have detected
          soldiers have come up to new idea that you can find strangers just take picture of them...
          it will turn unnormal
          and the global warming is getting worse each day...please stay alert and check your home''')
    print('I shouls check them')
    check()
def check():
    global visitor
    print('I should check the visitors')
    oooo=input('did you let the man? yes or no')
    if oooo == 'yes':
        print('I should check the first man')
        print('''man: well I am glad you are still here...
              you: I should check you
              man:what! do you think I am a damn stranger?
              you: It is just checking...and you are in my house by the way
              man:damn''')
        uu=input('''check the man
                 eyes
                 photo
                 hands
                 if they had one of them...you are allowed to kill''')
        if uu == 'hands':
            print('visitor does not have dirty hands')
            print('''you:clear
                  man:see!!''')
        elif uu == 'eyes':
            print('he has bloody eyes')
            print('man: it is just a sickness please')
            dd=input('kill or stay???')
            if dd == 'kill':
                killman()
                visitors-=1
            else:
                stay()
        else:
            print('it is a normal picture')
            print('man:see...I hate to take pictures man...')
            stay()
    else:
        night4()
    
def killman():
    global visitor
    print('you killed the first man')
    print('now you killed your first visitor')
    visitors-=1
    night4()
def stay():
    global visitor
    print('man:well that was not fair')
def night4():
    global visitor
    print('KNOCK')
    print('''you:oh
          him:well the end is near...are you alone?''')
    pp=input('''answer him
             yes I do not have anyone here(if you killed your only visitor or did not let anyone in)
             no there are people here
             why...''')
    if pp == 'no I do not have anyone here':
        end()
    else:
        print('well...beware')
        day5()
def end():
        global visitor
        print('that man killed you')
        while r:
           game()
           if end():
               r=False
               print('you died')
def day5():
        global visitor
        print('I should check people')
        ppppp=input('did you let her? yes or no')
        if ppppp == 'yes':

            print('I should check her')
            print('''woman:well
                  you: I should check you
                  woman:wellokay after all I have got nothing''')
            iii=input('''check her
                      photo
                      eyes
                      hands''')
            if iii == 'hands':
                print('clear')
                check2()
            elif iii == 'eyes':
                print('clear')
                check2()
            else:
                print('''clear
                      woman:well...''')
                check2()
        else:
            check2()
def check2():
            global visitor
            uuuu=input('did you let woman yes or no? ')
            if uuuu == 'yes':
                print('I should check her...')
                print('''woman:aaah you are here
                      you:I should check you...
                      woman:okay?''')
                eee=input('check her hands eyes or photo')
                if eee == 'hands':
                    print(' it is dirty')
                    print('woman:wait listen I work in the garden please')
                    tt=input('kill or stay?')
                    if tt == 'kill':
                       kill2()
                elif eee =='eyes':
                    print('clear')
                    stay2()
                else:
                    print('clear')
                    print('woman:OH I AM GLAD')
                    stay2()
            else:
                night5()
def kill2():
            global visitor
            print('you have killed one of your visitors')
            visitors-=1
            night5()
def stay2():
            global visitor
            night5()
def night5():
        global visitor
        print('KNOCK KNOCK')
        print('''soldier:we have to pick one of your roommates
              you:why???
              soldier:it is an order''')
        III=input('have you let that woman in? yes or no?   ')
        if III == 'yes':
            print('we will pick her')
            visitors-=1
            night6()
        else:
            print('no one was taken')
            night6()
def night6():
        global visitor
        print(visitor)
        if visitor ==0 :
            end()
        elif visitor == 2:
            end2()
        elif visitor == 1:
            end3()
def end2():
        global visitor
        print('one of them was a stranger')
        while r:
            game()
            if end2():
                r= False
def end3():
        global visitor
        print('you survived but you will noy last so much')
        game()
        if end3():
            r= False
game()

            

        
               
        
            
        

               
           
