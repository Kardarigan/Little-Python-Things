Coins = 50
Soldier = 10
Block = 100
Mine_in_The_cave = 0
Gold = 0
Miner = 0
worker = 0
Building = []
Cmds = 0


Map = ["Small Town","Average Town","Big Town"]


Menu_Of_All_Town = ["Attack","go shopping","Travel to establish government","cancel"]


Shopping = ["food store","Sale of materials","Sale of military animals","Selling working animals","gun shop","municipality","Buying people"]


Food_Store = ["Fruit","Drinks","Wheat","Rice","Water","Tea","Canned food"]


Sale_Of_Materials = ["Cement","Gypsum","Brick","Soil","Sand","Shovel","Pickaxe","Bucket","Axe","Trident","Wood","Straw","Metal"]


Sale_Of_Military_Animals = ["Horse","Camel","Dog","Wolf","Donkey"]


Selling_Working_Animals = ["Horse","Cow","Camel","Deer","Donkey","Dog","Goat"]


Gun_Shop = ["Spear","Sword","Axe","Bullet","Cartridge","Pickaxe","Bat","Gunpowder","Fence Guard"]


Municipality = ["Buy land","Buy building permit","Buy certificate","Get permit","Buy territory"]


Buying_People = ["Worker","Miner","Soldier","Warrior","Servant","Fisherman","Postman","Police","Farmer","Rascalist"]

def sep():
    print("_"*90)    
while True:
    sep()
    print("Day",Cmds//16)
    sep()
    print("Coins :",Coins)
    print("Soldier :",Soldier)   
    print("Block Zone :",Block)
    print("pure_gold :",Mine_in_The_cave)
    print("Miner :",Miner)
    sep()
    x = input("What do you want ? :")
    Cmds += 1
    if x == "Buy Soldier":
        a = int(input("How many soldiers do you want to buy for yourself ? : "))
        if a*2 <= Coins:
            Coins -= a*2
            Soldier += a
        else:
            print("We are out of Coins !")

    if x == "Mine_in_The_cave":
        y = int(input("How many soldiers do you want for mine? : "))
        if y <= Soldier:
            Soldier -= y
            Miner += y
        else:
            print("Your number of soldiers is not enough to turn into a Chi mine !") 


            
    if x == "Exchange":
        c = input("Enter the item you want to exchange ! :")
        if c == "Soldier":
            d = input("Do you want to turn a soldier into a worker or Miner ? :")
            if d == "Worker":
                e = int(input("How many soldiers do you want for Worker ? :"))
                if e <= Soldier:
                    Soldier -= e
                    worker += e
        
            elif d == "Miner":
                e = int(input("How many soldiers do you want for Miner ? :"))
                if e <= Soldier:
                    Soldier -= e
                    Miner += e
        elif c == "Worker":
            d = input("Do you want to turn a Worker into a Soldier or a miner ? :")
            if d == "Soldier":
                e = int(input("How many Worker do you want for Soldier ? :"))
                if e <= Worker:
                    Soldier += e
                    worker -= e
        
            elif d == "Miner":
                e = int(input("How many Worker do you want for Worker ? :"))
                if e <= Worker:
                    Miner += e
                    worker -= e
        elif c == "Miner":
            d = input("Do you want to turn a Miner into a Soldier or a Worker ? :")
            if d == "Soldier":
                e = int(input("How many Miner do you want for Soldier ? :"))
                if e <= Miner:
                    Soldier += e
                    Miner -= e
        
            elif d == "Worker":
                e = int(input("How many Miner do you want for Soldier ? :"))
                if e <= Miner:
                    Miner += e
                    Worker -= e
        else:
            print("Your request is invalid. You do not have the required item for exchange !")

    Mine_in_The_cave += Miner*2


    if x == "Map":
        print(Map)
    if x == "Small Town":
        choice_Menu_Town = input(print(Menu_Of_All_Town))
        if x == "Attack":
            if Soldier >= 100 :
                print("The attack was carried out ! (:")
            elif Soldier <= 100 :
                print("You don't have enough soldiers to attack this Town ! ")
    

    if x == "Shopping":
        choice_Menu_Shopping = input(print(Shopping))
        if x == Food_Store:
            print(Food_Store)


    if x == "Shopping":
        choice_Menu_Shopping = input(print(Shopping))
        if x == Sale_Of_Materials:
            print(Sale_Of_Materials)


    if x == "Shopping":
        choice_Menu_Shopping = input(print(Shopping))
        if x == Sale_Of_Military_Animals:
            print(Sale_Of_Military_Animals)



    if x == "Shopping":
        choice_Menu_Shopping = input(print(Shopping))
        if x == Selling_Working_Animals:
            print(Selling_Working_Animals)



    if x == "Shopping":
        choice_Menu_Shopping = input(print(Shopping))
        if x == Gun_Shop:
            print(Gun_Shop)



    if x == "Shopping":
        choice_Menu_Shopping = input(print(Shopping))
        if x == Municipality:
            print(Municipality)



    if x == "Shopping":
        choice_Menu_Shopping = input(print(Shopping))
        if x == Buying_People:
            print(Buying_People)


    if x == "Map":
        print(Map)
    if x == "Average Town":
        choice_Menu_Town = input(print(Menu_Of_All_Town))
        if x == "Attack":
            if Soldier >= 200 :
                print("The attack was carried out ! (:")
            elif Soldier <= 200 :
                print("You don't have enough soldiers to attack this Town ! ")


    if x == "Shopping":
        choice_Menu_Shopping = input(print(Shopping))
        if x == Food_Store:
            print(Food_Store)


    if x == "Shopping":
        choice_Menu_Shopping = input(print(Shopping))
        if x == Sale_Of_Materials:
            print(Sale_Of_Materials)


    if x == "Shopping":
        choice_Menu_Shopping = input(print(Shopping))
        if x == Sale_Of_Military_Animals:
            print(Sale_Of_Military_Animals)



    if x == "Shopping":
        choice_Menu_Shopping = input(print(Shopping))
        if x == Selling_Working_Animals:
            print(Selling_Working_Animals)



    if x == "Shopping":
        choice_Menu_Shopping = input(print(Shopping))
        if x == Gun_Shop:
            print(Gun_Shop)



    if x == "Shopping":
        choice_Menu_Shopping = input(print(Shopping))
        if x == Municipality:
            print(Municipality)



    if x == "Shopping":
        choice_Menu_Shopping = input(print(Shopping))
        if x == Buying_People:
            print(Buying_People)



    if x == "Map":
        print(Map)
    if x == "Big Town":
        choice_Menu_Town = input(print(Menu_Of_All_Town))
        if x == "Attack":
            if Soldier >= 500 :
                print("The attack was carried out ! (:")
            elif Soldier <= 500 :
                print("You don't have enough soldiers to attack this Town ! ")



    if x == "Shopping":
        choice_Menu_Shopping = input(print(Shopping))
        if x == Food_Store:
            print(Food_Store)


    if x == "Shopping":
        choice_Menu_Shopping = input(print(Shopping))
        if x == Sale_Of_Materials:
            print(Sale_Of_Materials)


    if x == "Shopping":
        choice_Menu_Shopping = input(print(Shopping))
        if x == Sale_Of_Military_Animals:
            print(Sale_Of_Military_Animals)



    if x == "Shopping":
        choice_Menu_Shopping = input(print(Shopping))
        if x == Selling_Working_Animals:
            print(Selling_Working_Animals)



    if x == "Shopping":
        choice_Menu_Shopping = input(print(Shopping))
        if x == Gun_Shop:
            print(Gun_Shop)



    if x == "Shopping":
        choice_Menu_Shopping = input(print(Shopping))
        if x == Municipality:
            print(Municipality)



    if x == "Shopping":
        choice_Menu_Shopping = input(print(Shopping))
        if x == Buying_People:
            print(Buying_People)

