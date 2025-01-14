import random

money = 5
oil = 6000
soldier = 240
allied_soldier = 1300 + 1228 + 200 + 240 + 300
allied_countries = ["Russia", "China", "North korea", "Turkey", "Japan"]
rocket = 11
tank = 10
spy = 0
battle = False


enemy = 0
allied_enemy_soldier = 0
enemy_rocket = 0


confirm = False
while not confirm:
    war = input("Enter your command(Example:Attack America) :").split()
    if war[0].capitalize() == "Attack":
        battle = True
        if war[1].capitalize() == "America" or "Usa" or "United states of america":
            attack = input("USA is a superpower are you sure you want to attack it?").capitalize()
            if attack == "Yes":
                confirm = True
                enemy = 1400
                allied_enemy_soldier = 3200
                rocket_power = 3
            elif attack == "No":
                continue
        elif war[1].capitalize() == "Russia":
            attack = input("Russia is a superpower are you sure you want to attack it?").capitalize()
            if attack == "Yes":
                confirm = True
                enemy = 1300
                rocket_power = 2.5
            elif attack == "No":
                continue
        elif war[1].capitalize() == "China":
            attack = input("China is a superpower are you sure you want to attack it?").capitalize()
            if attack == "Yes":
                confirm = True
                enemy = 1228
                rocket_power = 4
            elif attack == "No":
                continue
        elif war[1].capitalize() == "France":
            attack = input("France is a member of european union are you sure you want to attack it?").capitalize()
            if attack == "Yes":
                confirm = True
                enemy = 1600
                rocket_power = 2.5
            elif attack == "No":
                continue
        elif war[1].capitalize() == "Uk" or "Britain" or "United kingdom":
            attack = input("Britain is a member of european union are you sure you want to attack it?").capitalize()
            if attack == "Yes":
                confirm = True
                enemy = 1600
                rocket_power = 2.5
            elif attack == "No":
                continue
        elif war[1].capitalize() == "Germany":
            attack = input("Germany is a member of european union are you sure you want to attack it?").capitalize()
            if attack == "Yes":
                confirm = True
                enemy = 1600
                rocket_power = 2.5
            elif attack == "No":
                continue
        elif war[1].capitalize() == "austria":
            attack = input("austria is a member of european union are you sure you want to attack it?").capitalize()
            if attack == "Yes":
                confirm = True
                enemy = 1600
                rocket_power = 2.5
            elif attack == "No":
                continue
        elif war[1].capitalize() == "Switzerland":
            attack = input("Switzerland is a member of european union are you sure you want to attack it?").capitalize()
            if attack == "Yes":
                confirm = True
                enemy = 1600
                rocket_power = 2.5
            elif attack == "No":
                continue
        elif war[1].capitalize() == "Spain":
            attack = input("Spain is a member of european union are you sure you want to attack it?").capitalize()
            if attack == "Yes":
                confirm = True
                enemy = 1600
                rocket_power = 2.5
            elif attack == "No":
                continue
        elif war[1].capitalize() == "Italy":
            attack = input("Italy is a member of european union are you sure you want to attack it?").capitalize()
            if attack == "Yes":
                confirm = True
                enemy = 1600
                rocket_power = 2.5
            elif attack == "No":
                continue
        elif war[1].capitalize() == "Finland":
            attack = input("Finland is a member of european union are you sure you want to attack it?").capitalize()
            if attack == "Yes":
                confirm = True
                enemy = 1600
                rocket_power = 2.5
            elif attack == "No":
                continue
        elif war[1].capitalize() == "Netherlands":
            attack = input("Netherlands is a member of european union are you sure you want to attack it?").capitalize()
            if attack == "Yes":
                confirm = True
                enemy = 1600
                rocket_power = 2.5
            elif attack == "No":
                continue
        elif war[1].capitalize() == "Poland":
            attack = input("Poland is a member of european union are you sure you want to attack it?").capitalize()
            if attack == "Yes":
                confirm = True
                enemy = 1600
                rocket_power = 2.5
            elif attack == "No":
                continue
        elif war[1].capitalize() == "Belgium":
            attack = input("Belgium is a member of european union are you sure you want to attack it?").capitalize()
            if attack == "Yes":
                confirm = True
                enemy = 1600
                rocket_power = 2.5
            elif attack == "No":
                continue
        elif war[1].capitalize() == "Bulgaria":
            attack = input("Bulgaria is a member of european union are you sure you want to attack it?").capitalize()
            if attack == "Yes":
                confirm = True
                enemy = 1600
                rocket_power = 2.5
            elif attack == "No":
                continue
        elif war[1].capitalize() == "Croatia":
            attack = input("Croatia is a member of european union are you sure you want to attack it?").capitalize()
            if attack == "Yes":
                confirm = True
                enemy = 1600
                rocket_power = 2.5
            elif attack == "No":
                continue
        elif war[1].capitalize() == "Republic of cyprus" or "Cyprus":
            attack = input("Republic of Cyprus is a member of european union are you sure you want to attack it?").capitalize()
            if attack == "Yes":
                confirm = True
                enemy = 1600
                rocket_power = 2.5
            elif attack == "No":
                continue
        elif war[1].capitalize() == "Czech republic" or "Czech":
            attack = input("Netherlands is a member of european union are you sure you want to attack it?").capitalize()
            if attack == "Yes":
                confirm = True
                enemy = 1600
                rocket_power = 2.5
            elif attack == "No":
                continue
        elif war[1].capitalize() == "Denmark":
            attack = input("Denmark is a member of european union are you sure you want to attack it?").capitalize()
            if attack == "Yes":
                confirm = True
                enemy = 1600
                rocket_power = 2.5
            elif attack == "No":
                continue
        elif war[1].capitalize() == "Estonia":
            attack = input("Estonia is a member of european union are you sure you want to attack it?").capitalize()
            if attack == "Yes":
                confirm = True
                enemy = 1600
                rocket_power = 2.5
            elif attack == "No":
                continue
        elif war[1].capitalize() == "Greece":
            attack = input("Greece is a member of european union are you sure you want to attack it?").capitalize()
            if attack == "Yes":
                confirm = True
                enemy = 1600
                rocket_power = 2.5
            elif attack == "No":
                continue
        elif war[1].capitalize() == "Hungary":
            attack = input("Hungary is a member of european union are you sure you want to attack it?").capitalize()
            if attack == "Yes":
                confirm = True
                enemy = 1600
                rocket_power = 2.5
            elif attack == "No":
                continue
        elif war[1].capitalize() == "Ireland":
            attack = input("Ireland is a member of european union are you sure you want to attack it?").capitalize()
            if attack == "Yes":
                confirm = True
                enemy = 1600
                rocket_power = 2.5
            elif attack == "No":
                continue
        elif war[1].capitalize() == "Latvia":
            attack = input("Latvia is a member of european union are you sure you want to attack it?").capitalize()
            if attack == "Yes":
                confirm = True
                enemy = 1600
                rocket_power = 2.5
            elif attack == "No":
                continue
        elif war[1].capitalize() == "Lithuania":
            attack = input("Lithuania is a member of european union are you sure you want to attack it?").capitalize()
            if attack == "Yes":
                confirm = True
                enemy = 1600
                rocket_power = 2.5
            elif attack == "No":
                continue
        elif war[1].capitalize() == "Luxembourg":
            attack = input("Luxembourg is a member of european union are you sure you want to attack it?").capitalize()
            if attack == "Yes":
                confirm = True
                enemy = 1600
                rocket_power = 2.5
            elif attack == "No":
                continue
        elif war[1].capitalize() == "Malta":
            attack = input("Malta is a member of european union are you sure you want to attack it?").capitalize()
            if attack == "Yes":
                confirm = True
                enemy = 1600
                rocket_power = 2.5
            elif attack == "No":
                continue
        elif war[1].capitalize() == "Portugal":
            attack = input("Portugal is a member of european union are you sure you want to attack it?").capitalize()
            if attack == "Yes":
                confirm = True
                enemy = 1600
                rocket_power = 2.5
            elif attack == "No":
                continue
        elif war[1].capitalize() == "Romania":
            attack = input("Romania is a member of european union are you sure you want to attack it?").capitalize()
            if attack == "Yes":
                confirm = True
                enemy = 1600
                rocket_power = 2.5
            elif attack == "No":
                continue
        elif war[1].capitalize() == "Slovakia":
            attack = input("Slovakia is a member of european union are you sure you want to attack it?").capitalize()
            if attack == "Yes":
                confirm = True
                enemy = 1600
                rocket_power = 2.5
            elif attack == "No":
                continue
        elif war[1].capitalize() == "Slovenia":
            attack = input("Slovenia is a member of european union are you sure you want to attack it?").capitalize()
            if attack == "Yes":
                confirm = True
                enemy = 1600
                rocket_power = 2.5
            elif attack == "No":
                continue
        elif war[1].capitalize() == "Sweden":
            attack = input("Sweden is a member of european union are you sure you want to attack it?").capitalize()
            if attack == "Yes":
                confirm = True
                enemy = 1600
                rocket_power = 2.5
            elif attack == "No":
                continue
        elif war[1].capitalize() == "Japan":
            enemy = 300
            a = False
        elif war[1].capitalize() == "India":
            enemy = 600
            a = False
        elif war[1].capitalize() == "South korea":
            enemy = 200
            a = False
        elif war[1].capitalize() == "Turkey":
            enemy = 240
            a = False
        elif war[1].capitalize() == "Republic of korea" or "South korea":
            enemy = 100
            a = False
        elif war[1].capitalize() == "Vietnam":
            enemy = 105
            a = False
        elif war[1].capitalize() == "Taiwan":
            enemy = 110
            a = False
        elif war[1].capitalize() == "United arab emirates" or "Emirates":
            enemy = 120
            a = False
        elif war[1].capitalize() == "Thailand":
            enemy = 130
            a = False
        elif war[1].capitalize() == "Indonesia":
            enemy = 150
            a = False
        elif war[1].capitalize() == "Pakistan":
            enemy = 160
            a = False
        elif war[1].capitalize() == "Saudi arabia":
            enemy = 200
            a = False
        elif war[1].capitalize() == "Israel":
            enemy = 200
            a = False
        elif war[1].capitalize() == "Jordan":
            enemy = 200
            a = False
        elif war[1].capitalize() == "Oman":
            enemy = 220
            a = False
        elif war[1].capitalize() == "Iraq":
            enemy = 230
            a = False
        elif war[1].capitalize() == "Kuwait":
            enemy = 230
            a = False
        elif war[1].capitalize() == "Egypt":
            enemy = 240
            a = False
        elif war[1].capitalize() == "Qatar":
            enemy = 240
            a = False
        elif war[1].capitalize() == "Brazil":
            enemy = 220
            a = False
        elif war[1].capitalize() == "Mexico":
            enemy = 200
            a = False
        elif war[1].capitalize() == "Canada":
            enemy = 380
            a = False
        elif war[1].capitalize() == "Argentina":
            enemy = 180
            a = False
        elif war[1].capitalize() == "Morocco":
            enemy = 80
            a = False
        elif war[1].capitalize() == "Azerbaijan":
            enemy = 50
            a = False
        elif war[1].capitalize() == "Kazakhstan":
            enemy = 40
            a = False
        elif war[1].capitalize() == "Morocco":
            enemy = 80
            a = False
        elif war[1].capitalize() == "lebanon":
            enemy = 30
            a = False


def buy(item):
    global money, soldier, rocket, tank, spy
    if item == "soldier" and money >= 1:
        soldier += 100
        money -= 1
    elif item == "rocket" and money >= 1:
        rocket += 1
        money -= 1
    elif item == "tank" and money >= 2:
        tank += 1
        money -= 2
    elif item == "spy" and money >= 1:
        spy += 1
        money -= 1
    else:
        print("Not enough money")


def sell(item):
    global money, soldier, rocket, tank, spy, oil
    if item == "soldier" and soldier >= 100:
        soldier -= 100
        money += 1
    elif item == "rocket" and rocket >= 1:
        rocket -= 1
        money += 1
    elif item == "tank" and tank >= 1:
        tank -= 1
        money += 2
    elif item == "spy" and spy >= 1:
        spy -= 1
        money += 1
    elif item == "oil" and oil >= 1000:
        oil -= 1000
        money += 5
    else:
        print("Not enough items")


def use(item, weapon=None):
    global enemy, rocket, soldier, spy, tank, allied_soldier, allied_enemy_soldier
    if item == "rocket" and rocket >= 1:
        rocket -= 1
        enemy -= 20
    elif item == "soldier" and soldier >= 10:
        soldier -= 10
        if weapon == "kalashnikov":
            enemy -= 20
        elif weapon == "shotgun":
            enemy -= 22
        elif weapon == "smg":
            enemy -= 18
        elif weapon == "rpg":
            enemy -= 40
        else:
            enemy -= 15
    elif item == "allied_soldier" and allied_soldier >= 30:
        allied_soldier -= 30
        if allied_enemy_soldier <= 90:
            allied_soldier -= 30
            if weapon == "kalashnikov":
                enemy -= 50
            elif weapon == "shotgun":
                enemy -= 58
            elif weapon == "smg":
                enemy -= 52
            elif weapon == "rpg":
                enemy -= 90
            else:
                enemy -= 40
        elif allied_enemy_soldier > 90:
            if weapon == "kalashnikov":
                allied_enemy_soldier -= 50
            elif weapon == "shotgun":
                allied_enemy_soldier -= 58
            elif weapon == "smg":
                allied_enemy_soldier -= 52
            elif weapon == "rpg":
                allied_enemy_soldier -= 90
            else:
                allied_enemy_soldier -= 40

    elif item == "spy" and spy >= 1:
        spy -= 1
        print(f"Enemy has {enemy_rocket} rockets.")
    if item == "tank" and tank >= 1:
        tank -= 1
        enemy -= 40
    else:
        print("Not enough items")


def peace():
    global battle
    peace_confirmation = random.randint(1, 2)
    if peace_confirmation == 1:
        print("Enemy accepted our peace contract.")
        battle = False
    else:
        print("Enemy refused our peace contract.")


def resign():
    global battle, soldier, oil
    soldier_give = random.randint(9, soldier)
    oil_give = random.randint(999, oil)
    __resign__ = input(f"""If you resign you will give {soldier_give} soldiers and {oil_give} oil.
                       Are you sure you want to resign?""").capitalize()
    if __resign__ == "Yes":
        soldier -= soldier_give
        oil -= oil_give
        print("You resigned.\nYou're nothing except a pussy :|")
        battle = False
    elif __resign__ == "No":
        print("Good job ^_+")


while battle:
    if soldier == 0:
        print("""Enemy captured our homeland
        Khak bar sare farmandeh""")
        battle = False
    elif enemy == 0:
        print("""A country added to our homeland
        Merci farmandeh""")
        battle = False
    print("\n")
    print("Salam farmandeh.")
    print(f"Enemy has {enemy} soldiers and their allied countries soldiers are ")
    print(f"You have {money} coins, {soldier} soldiers, {rocket} rockets, {spy} spies  and your allied countries are {allied_countries} that they have {allied_soldier} soldiers totally")
    print("""Functions:
        buy soldier, buy rocket, buy spy, buy tank, use spy, use rocket, use soldier
        use tank, peace, sell rocket, sell soldier, sell spy, sell tank, sell oil, resign""")
    command = input("Enter a command: ").split()
    if command[0] == "buy":
        buy(command[1])
    elif command[0] == "use":
        if len(command) == 3:
            use(command[1], command[2])
        else:
            use(command[1])
    elif command[0] == "sell":
        sell(command[1])
    elif command[0] == "peace":
        peace()
    elif command[0] == "resign":
        resign()
    else:
        print("Invalid command")
