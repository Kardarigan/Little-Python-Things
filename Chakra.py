chakra = 1500
shuricen = 100
kunai = 55
teki= 140
nakama= 140
experience=0
payment=0
print('hint:fist try to train and gain chakra')
jutsu=['RANK A JUTSU','RANK B JUTSU','RANK C JUTSU','RANK D JUTSU']
orders =['attack','support','get back','buy kunai','buy shuricen','increase chakra','train','throw shuricen','rasengan','throw kunai','pay','increase experience','sell kunai and shuricen']
go = True
while teki and nakama and go:
    print(orders)
    print(jutsu)
    move = input('what should we do boss?:')
  
    if move == 'sell kunai and shuricen':
        payment+=25
        shuricen-=10
        kunai-=5
    if move == 'buy shuricen'and payment > 0:
         
         shuricen += 10
         payment-=5
    if move == 'buy shuricen' and payment == 0:
        print(' not enough money')
    if move == 'buy kunai' and payment > 0:
         kunai += 5
         payment-=5
    if   move == 'buy kunai' and payment == 0:
        print('not enough money')
    if move == 'train':
        for i in range(4):
            u=input('how much time do you need for training?:')
            if u == '2 days':
                   chakra+=100
                   experience+=50
            if u == ' 1 day ' :
                   chakra+=50
                   experience+=25
            if u==' 12 hours ':
                   chakra+=25
                   experience=12
            if u == ' less than 12 hours':
                   chakra+=12
              

    if move == 'increase chakra' :
        
       print('you can gain more chakra by fightinh')
    if experience == 0:
         print(' you have to train or go to war')
    if experience > 0 :
            chakra += 140




    if move == 'attack' :
        if nakama==teki :
            teki -= 5
            nakama -= 5
        if nakama < teki :
            teki -= 2
            nakama -= 5
        if nakama > teki :
            teki -= 20
            nakama -= 10
   
    if move == 'support' :
        nakama+=20
    if move=='throw shuricen':
        shuricen-=5
        teki-=2

    if move == 'throw kunai':
        kunai-=5
        teki-=3
    if move == 'RANK A JUTSU':
        chakra-=100
    if move == 'RANK B JUTSU':
        chakra-=75
    if move == 'RANK C JUTSU':
        chakra -=50
    if move == 'RANK D JUTSU':
        chakra -=25
    if chakra <=1:
        print('you can not use jutsu if your chakra runs out you may die!!!!')
    if teki<= 0 and chakra>0:
        print('yoshaaa')
        payment+=5555
        experience+=600
    elif nakama<=0 and chakra<=0:
        print('yadaaaaa')
        go = False

    print('teki')
    print(teki)
    print('nakama')
    print(nakama)
    print('kunai')
    print(kunai)
    print('shuricen')
    print(shuricen)
    print('experience')
    print(experience)
    print('payment')
    print(payment)
    print('chakra')
    print(chakra)


















    
