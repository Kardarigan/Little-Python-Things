
s=True
LashcarMa=100
LashcarDoshman=100
coin=10
g=25
p=10
a=20

while LashcarMa and LashcarDoshman and s:
    LashcarDoshman+=15
    print(LashcarDoshman)
    print(LashcarMa)
    print(coin)
    w=input('choose one[attack] [deffnce] [white flag] [nuke] [buy sarbaz 10] [sent jets]')
    if w =='attack':
            print('u choosed attack')
            LashcarMa-=15
            LashcarDoshman-=20
            coin+=10
    elif w =='deffnce':
        print('u choosed deffnce')
        LashcarMa-=5
        LashcarDoshman-=10
        coin+=5
    elif w =='white flag':
        if LashcarMa>=LashcarDoshman:
            print('shoma solh cardid bazi tamam shod')
            s=False
    elif w =='nuke':
        if coin>=g:
            LashcarMa+=10
            LashcarDoshman-=40
            coin-=25
            print('shoma az nuke estfade cardid')
    elif w =='buy sarbaz 10':
        if coin>=p:
            LashcarMa+=10
            coin-=10
            print('shoma sarbaz kharidid')
    elif w =='sent jets':
        if coin>=a:
            LashcarDoshman-=25
            LashcarMa-=6
            coin-=20
            print('moshak ha frestade shodand')
    

    if LashcarDoshman <= 0:
        print('shoma bazi ra bordid')
        s=False
    elif LashcarMa <= 0:
        print('shoma bazi ra bakhtid')
        s=False
    

    

            
