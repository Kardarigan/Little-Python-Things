from random import*
from time import*
energy=360
choice_play=int(input('Hi Dear if you want to play whit your Friend enter 1 if you want to play the game enter 2 '))

def game():
    global energy
    while True:
            sleep(5)
            energy+=1
            n={"Avada Kedavra":200, "Crucio":100, "Imperio":100, "Fiendfyre":110}
            print('Welcome to the macig world.' \
            'Here in this game you can duel with dark enimes how are persons of the preson  that we dont say his name.\nYou have 360 energy means that per the damege you lose energy but in the defence magics you win 30 energy if you can beat your enemy.')
            sd= {
                "Protego": 40,              
                "Protego Duo": 50,           
                "Protego Horribilis": 60,    
                "Protego Totalum": 70,       
                "Protego Maxima": 90,        
                "Repello Inimicum": 65,      
                "Salvio Hexia": 90,              
                "Petrificus Totalus": -20,
                "Incarcerous": -15,
                "Impedimenta": -10,
                "Locomotor Mortis": -10,
                "Rictusempra": -5,
                "Tarantallegra": -5,
                "Silencio": -10,
                "Langlock": -5,
                "Mimblewimble": -5,
                "Oppugno": -15,
                "Serpensortia": -20,
                "Avis": -10,
                "Expelliarmus": -25,
                "Stupefy": -30,
                "Expulso": -40,
                "Reducto": -45,
                "Bombarda": -50,
                "Diffindo": -35,
                "Depulso": -30,
                "Relashio": -25,
                "Incendio": -40,
                "Everte Statum": -30,
                "Confringo": -50,
                "Bombarda Maxima": -80,
                "Sectumsempra": -90,
            }
            sdupdate={
        "Legilimens": -90,
        "Muffliato": 50,
        "Obliviate": -90,
        "Obscuro": -15
    }

            ensl = {
                "Stan Shunpike": {
                    "Stupefy":-30, "Expelliarmus":-25, "Protego":40, "Finite Incantatem":20, "Mimblewimble":-5
            },
                "krab": {
                    "Depulso":-30, "Reducto":-45, "Protego":40, "Obscuro":-15, "Expulso":-40, "Protego Horribilis":60
                },
                "Draco Malfoy": {
                    "Expelliarmus":-25, "Stupefy":-30, "Diffindo":-35, "Protego":40, "Rictusempra":-5, "Impedimenta":-10, "Petrificus Totalus":-20
                },
                "Lucius Malfoy": {
                    "Sectumsempra":-90, "Legilimens":-90, "Protego Totalum":70, "Obliviate":-90, "Expulso":-40, "Salvio Hexia":45, "Repello Inimicum":65
                },
                "Bellatrix Lestrange": {
                    "Crucio":-120, "Confringo":-50, "Bombarda Maxima":-80, "Protego Horribilis":70, "Obliviate":-90
                },
                "Severus Snape": {
                    "Sectumsempra":-90, "Legilimens":-90, "Expulso":-40, "Salvio Hexia":90, "Protego Totalum":70, "Muffliato":50
                },
                "Delphi Riddle": {
                    "Crucio":-120, "Fiendfyre":-110,"Protego Maxima":90, "Obliviate":-90, "Confringo":-80, "Imperio":-115,"Avada Kedavra":-180
                },
                "Tom Riddle (Voldemort)": {
                    "Avada Kedavra":-180, "Imperio":-115, "Crucio":-120, "Fiendfyre":-110, "Repello Inimicum":95,
                    "Legilimens":-90, "Obliviate":-90, "Bombarda Maxima":-80, "Protego Maxima":120,"Fiendfyre":-110
                }
            }
            yhp=120
            st=70
            def p():
                print(yhp)
                print(energy)   
            print(f'At first stage you have to duel with stan shunpike.{sd}(Hp 70) ')
            while st>0:
                stn = choice(list(ensl['Stan Shunpike'].keys()))
                print(stn)
                r=input('Spell:')
                if stn=="Protego":
                    da=sd.get(r,0)+40
                    st+=da
                    print(f"Enemy HP: {st}")
                    p()
                    energy+=da
                else:
                    da=sd.get(r,0)
                    energy+=da
                    print(f"Enemy HP: {st}")
                    p()
                    st+=da
                    yhp+= sd.get(stn, 0)
                if r=='Protego'or r=='Protego Duo' or r=='Protego Horribilis'or r=='Protego Totalum' or r=='Protego Maxima'or r=='Repello Inimicum'or r=='Salvio Hexia' or r=='Protego Horribilis'or r=='Protego Totalum' or r=='Protego Maxima':
                    de=sd.get(r,0)
                    print(de)
                    yhp+=de
                    print(st)
                    p()
                if st<=0:
                    print('its not bad for the first but ')
                    break      
                if energy<=0:
                    print('Ohh No You lose energy.')
                    exit()
                    break
                elif yhp<=0:
                    print("You lose.")
                    exit()
                    break
            yhp=120
            k=80
            print(f'At second stage you have to duel with krab.{sd}(Hp 80) ')
            while k>0:
                kn=choice(list(ensl['krab'].keys()))
                print(kn)
                r=input('Spell:')
                if kn=="Protego":
                    da=sd.get(r,0)+40
                    k+=da
                    print(f"Enemy HP: {k}")
                    p()
                    energy+=da  
                elif kn=="Protego Horribilis":
                    da=sd.get(r,0)+65
                    k+=da
                    energy+=da
                    print(f"Enemy HP: {k}")
                    p()
                else:
                    da=sd.get(r,0)
                    k+=da
                    yhp+= sd.get(kn, 0)  
                    energy+=da
                if r=='Protego'or r=='Protego Duo' or r=='Protego Horribilis'or r=='Protego Totalum' or r=='Protego Maxima'or r=='Repello Inimicum'or r=='Salvio Hexia' or r=='Protego Horribilis'or r=='Protego Totalum' or r=='Protego Maxima':
                    de=sd.get(r,0)
                    print(de)
                    yhp+=de
                    print(st)
                    p()
                if energy<=0:
                    print('Ohh No You lose energy.')
                    exit()
                    break
                if k<0:
                    print("You arn't a  Amatur")
                    break
                if yhp<=0:
                    print("You lose.")
                    exit()
                    break
            yhp=120
            dr=85
            print(f'At Third stage you have to duel with Draco malfoy.{sd}(Hp 85) ')
            while dr>0:
                drn = choice(list(ensl['Draco Malfoy'].keys()))
                print(drn)
                r=input('Spell:')
                if drn=="Protego":
                    da=sd.get(r,0)+40
                    dr+=da
                    print(f"Enemy HP: {dr}")
                    p()
                    energy+=da
                else:
                    da=sd.get(r,0)
                    energy+=da
                    dr+=da
                    yhp+= sd.get(drn, 0)  
                    print(f"Enemy HP: {dr}")
                    p()
                if r=='Protego'or r=='Protego Duo' or r=='Protego Horribilis'or r=='Protego Totalum' or r=='Protego Maxima'or r=='Repello Inimicum'or r=='Salvio Hexia' or r=='Protego Horribilis'or r=='Protego Totalum' or r=='Protego Maxima':
                    de=sd.get(r,0)
                    print(de)
                    yhp+=de
                    print(k)
                    p()
                if energy<=0:
                    print('Ohh No You lose energy.')
                    exit()
                    break
                if dr<=0:
                    print('Its looks good.')
                    break
                elif yhp<=0:
                    print("You lose.")
                    exit()
                    break
            yhp=120                
            lm=90
            print(f'At fourth stage you have to duel with Lucius Malfoy.{sd}(Hp 80) ')
            while lm>0:
                lmc = choice(list(ensl['Lucius Malfoy'].keys()))
                print(lmc)
                r=input('Spell:')
                if lmc=="Protego Totalum":
                    da=sd.get(r,0)+70
                    lm+=da
                    print(f"Enemy HP: {lm}")
                    p()
                    energy+=da
                else:
                    da=sd.get(r,0)
                    lm+=da
                    yhp+= sd.get(lmc, 0)  
                    print(f'Enemy HP: {lm}')
                    p()
                if r=='Protego'or r=='Protego Duo' or r=='Protego Horribilis'or r=='Protego Totalum' or r=='Protego Maxima'or r=='Repello Inimicum'or r=='Salvio Hexia' or r=='Protego Horribilis'or r=='Protego Totalum' or r=='Protego Maxima':
                    de=sd.get(r,0)
                    print(de)
                    yhp+=de
                    print(lm)
                    p()
                if energy<=0:
                    print('Ohh No You lose energy.')
                    exit()
                    break             
                if da>=90:
                    print('You are ready for danger.')
                    break
                if yhp<=0:
                    print("You lose.")
                    exit()
                    break
            yhp=120
            BL=100
            while BL>0:
                bln = choice(list(ensl['Bellatrix Lestrange'].keys()))
                print(bln)
                r=input('Spell:')
                if bln=="Protego Horribilis":
                    da=sd.get(r,0)+70
                    BL+=da
                    energy+=da
                    print(f"Enemy HP: {BL}") 
                    p()
                else:     
                    da=sd.get(r,0)
                    energy+=da
                    BL+=da
                    yhp+= sd.get(bln, 0)   
                if r=='Protego'or r=='Protego Duo' or r=='Protego Horribilis'or r=='Protego Totalum' or r=='Protego Maxima'or r=='Repello Inimicum'or r=='Salvio Hexia' or r=='Protego Horribilis'or r=='Protego Totalum' or r=='Protego Maxima':
                    de=sd.get(r,0)
                    print(de)
                    yhp+=de
                    print(BL)
                    p()           
                if energy<=0:
                    print('Ohh No You lose energy.')
                    exit()
                    break            
                if BL<=0:
                    print('Ohh You are a porfessinal doweler...')
                    break
                if yhp<=0:
                    print("You lose.")
                    exit()
                    break
            Sv=120
            yhp=120
            print(f'At The 6 stage You see The real danger Severus Snape.')
            while Sv>0:
                Svn=choice(list(ensl["Severus Snape"].keys()))
                print(Svn)
                r=input('Spell:')
                if Svn=="Protego Totalum":
                    da=sd.get(r,0)+sdupdate.get(r,0)+70
                    energy+=da
                    print(f"Enemy HP: {Sv}")
                    p()
                elif Svn=="Salvio Hexia": 
                    da=sd.get(r,0)+sdupdate.get(r,0)+90
                    Sv+=da  
                    print(f"Enemy HP: {Sv}")
                    p()
                else:
                    da=sd.get(r,0)+sdupdate.get(r,0)
                    energy+=da
                    Sv+=da
                    yhp+= sd.get(Svn, 0)  
                    print(f"Enemy HP: {Sv}")
                    p()
                if r=='Protego'or r=='Protego Duo' or r=='Protego Horribilis'or r=='Protego Totalum' or r=='Protego Maxima'or r=='Repello Inimicum'or r=='Salvio Hexia' or r=='Protego Horribilis'or r=='Protego Totalum' or r=='Protego Maxima':
                    de=sd.get(r,0)
                    print(de)
                    yhp+=de
                    print(Sv)
                    p()
                if energy<=0:
                    print('Ohh No You lose energy.')
                    exit()
                    break               
                if Sv<=0:
                    print('You show you mare ready for danger')
                    break
                if yhp<=0:
                    print("You lose.")
                    exit()
                    break
            yhp=120
            D=120
            print(f'At The Seventh stage you have to Dowle with Delfhi.')
            print(f'Now you can use nabakhshodani spells.{n}')
            while D>0:
                Dn = choice(list(ensl["Delphi Riddle"].keys()))
                print(Dn)
                r=input('Spell:')
                if Dn=="Protego Maxima":
                    da = sd.get(r, 0) + n.get(r, 0)+sdupdate.get(r,0)+90
                    D+=da
                    print(f"Enemy HP: {D}")
                    p()
                    energy+=da
                else:
                    da = sd.get(r, 0) + n.get(r, 0)+sdupdate.get(r,0)
                    D+=da
                    yhp+= sd.get(Dn, 0)  
                    energy+=da
                    print(f"Enemy HP: {D}")
                    p()
                if r=='Protego'or r=='Protego Duo' or r=='Protego Horribilis'or r=='Protego Totalum' or r=='Protego Maxima'or r=='Repello Inimicum'or r=='Salvio Hexia' or r=='Protego Horribilis'or r=='Protego Totalum' or r=='Protego Maxima':
                    de=sd.get(r,0)
                    print(de)
                    yhp+=de
                    print(D)
                    p()
                if energy<=0:
                    print('Ohh No You lose energy.')
                    exit()
                    break
                if D<=0:
                    print('You might be a great witch or wizard.')
                    break
                if yhp<=0:
                    print("You lose.")
                    exit()
                    break
            TMR=120
            yhp=120
            print(f'At the last stage you have to dowel with the .... Voldemort')
            while TMR>0:
                TC = choice(list(ensl["Tom Riddle (Voldemort)"].keys()))
                print(TC)    
                r=input('Spell:')
                if TC=="Protego Maxima":
                    da = sd.get(r, 0) + ensl["Tom Riddle (Voldemort)"].get(TC, 0)+sdupdate.get(r,0)
                    TMR += da
                else:
                    da = sd.get(r, 0) + ensl["Tom Riddle (Voldemort)"].get(TC, 0)+sdupdate.get(r,0)
                    yhp+= sd.get(TC, 0) 
                    TMR+=da
                    print(f"Enemy HP: {TMR}")
                    yhp+= sd.get(TC, 0)
                if r=='Protego'or r=='Protego Duo' or r=='Protego Horribilis'or r=='Protego Totalum' or r=='Protego Maxima'or r=='Repello Inimicum'or r=='Salvio Hexia' or r=='Protego Horribilis'or r=='Protego Totalum' or r=='Protego Maxima':
                    de=sd.get(r,0)
                    print(de)
                    yhp+=de
                    print(TMR)
                    p()
                if TMR<=0:
                    print('You Are a great wizerd you, you help the wizard world to be alive. ')
                    break
                if yhp<=0:
                    print("You lose.")
                    exit()
                    break
def Two_by_Two():
    player_1_hp=120
    player_2_hp=120
    sd= {
                "Protego": 40,              
                "Protego Duo": 50,           
                "Protego Horribilis": 60,    
                "Protego Totalum": 70,       
                "Protego Maxima": 90,        
                "Repello Inimicum": 65,      
                "Salvio Hexia": 90,              
                "Petrificus Totalus": -20,
                "Incarcerous": -15,
                "Impedimenta": -10,
                "Locomotor Mortis": -10,
                "Rictusempra": -5,
                "Tarantallegra": -5,
                "Silencio": -10,
                "Langlock": -5,
                "Mimblewimble": -5,
                "Oppugno": -15,
                "Serpensortia": -20,
                "Avis": -10,
                "Expelliarmus": -25,
                "Stupefy": -30,
                "Expulso": -40,
                "Reducto": -45,
                "Bombarda": -50,
                "Diffindo": -35,
                "Depulso": -30,
                "Relashio": -25,
                "Incendio": -40,
                "Everte Statum": -30,
                "Confringo": -50,
                "Bombarda Maxima": -80,
                "Sectumsempra": -90,
            }
    r=[ "Protego",            
        "Protego Duo" ,    
        "Protego Horribilis",
        "Protego Totalum",       
        "Protego Maxima",       
        "Repello Inimicum",      
        "Salvio Hexia"] 
    while True:
        iw=input(f'The first player enter your magic {sd}')
        aq=sd.get(iw,0)
        if iw in r :
            player_1_hp+=aq
        else:
            player_2_hp+=aq
        ia=input('Now second player enter your magic.')
        aq2=sd.get(ia,0)
        if ia in r :
            player_2_hp+=aq2
        else:
            player_1_hp+=aq2
        print(player_1_hp)
        print(player_2_hp)
        if player_1_hp<=0:
            print('Player one is winer')
            break
        elif player_2_hp<=0:
            print('Player Two is winer')
            break
        else:
            print('Draw') 
            break       
if choice_play==1:
    Two_by_Two()
elif choice_play==2:
    game()
else:
    print('Please enter valied input')