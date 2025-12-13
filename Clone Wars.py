# Our Army
clones = 100
jedi = 5
atte = 10
credit = 200

# Enemy Army
droid = 700
aat = 50

report_title = ['clones', 'jedi', 'atte', 'credit', 'droid', 'aat']
commands = ['buy', 'sell', 'attack']
buy_options = ['clone', 'atte']

while True:
    report = [clones, jedi, atte, credit, droid, aat]
    for i in range(len(report)):
        print(report_title[i] + ':\t' + str(report[i]))
    print('-' * 30)
    for i in commands:
        print('- ' + i)

    command = input('Whats your command sir? ')
    print('Sir yes sir!')

    if command == 'buy':
        for i in buy_options:
            print('- ' + i)
        unit_to_buy = input('Wich unit you wanna buy? ')
        amount_to_buy = int(input('How many items? '))
        total_cost = 0
        if unit_to_buy == 'clone':
            total_cost = amount_to_buy * 2
        elif unit_to_buy == 'atte':
            total_cost = amount_to_buy * 20
        else:
            print('invalid')

        if total_cost > credit:
            print('Were out of budget sir...')
            continue

        if unit_to_buy == 'clone':
            clones += amount_to_buy
            credit -= amount_to_buy * 2
        elif unit_to_buy == 'atte':
            atte += amount_to_buy
            credit -= amount_to_buy * 20

    elif command == 'attack':
        for i in range(3):
            print('-' + report_title[i])
        invader_unit = input('Choose your units: ')
        damage = 0

        if invader_unit == 'clones':
            invader_unit = clones
            damage = 2
        elif invader_unit == 'atte':
            invader_unit = atte
            damage = 20
        elif invader_unit == 'jedi':
            invader_unit = jedi
            damage = 80

        damage = invader_unit * damage

        enemy_units = input('Whats your target sir? ')
        enemy_damage = 0
        
        if enemy_units == 'droid':
            enemy_units = droid
            enemy_damage = 1
        elif enemy_units == 'aat':
            enemy_units = aat
            enemy_damage = 20
        
        enemy_damage = enemy_units * enemy_damage

        if enemy_damage > damage:
            invader_unit -= invader_unit // 0.1
        elif enemy_damage < damage:
            enemy_units -= enemy_units // 0.1
        else:
            invader_unit -= invader_unit // 0.05
            enemy_units -= enemy_units // 0.05
        