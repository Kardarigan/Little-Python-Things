import random

you = {
    'soldier': 300,
    'people': 750,
    'coin': 3000
}


cpu = {
    'soldier': 800,
    'people': 50,
    'coin': 2000
}


war = bool(you['soldier'] > 0 and cpu['soldier'] > 0)

print('''grearings sire. we are under attack

for freedome''')

def attack(us, enemy):
    damage = random.randint(10, 20)
    our_damge = random.randint(1, damage//2)
    us['coin'] -= 100
    us['soldier'] -= our_damge
    enemy['soldier'] -= damage
    
    return us, enemy

def defence(us, enemy):
    damage = random.randint(0, 15)
    our_damge = random.randint(1, damage//2)
    us['coin'] -= 30
    us['soldier'] -= our_damge
    us['people'] -= our_damge
    enemy['soldier'] -= damage
    
    return us, enemy

def hire(us, faction):
    amount = random.randint(1, us['coin'])    
    if faction == 'human':
        amount = int(input('how many units you wanna hire? '))
    
    
    if us['coin'] < amount * 3 or us['people'] < amount:
        print('we dont have enought coins/people!')
    
    else:
        cost = amount * 3
        us['coin'] -= cost
        us['people'] -= amount
        us['soldier'] += amount
        
    return us

def order(ord, faction):
    if faction == 'human':
        if ord == 'attack':
            return attack(you, cpu)
                
        elif ord == 'defence':
            return defence(you, cpu)

        elif ord == 'hire':
            return hire(you, faction), cpu
    
    else:
        if ord == 'attack':
            return attack(cpu, you)
                
        elif ord == 'defence':
            return defence(cpu, you)

        elif ord == 'hire':
            return hire(cpu, faction), you
            

commands = ['attack', 'defence', 'hire']


while war:
    print(you)
    print(cpu)
    
    you_cmd = input('whats your command sire? ')
    cpu_cmd = random.choice(commands)
    print('enemy chose ' + cpu_cmd)
    
    cmd = [(you_cmd, 'human'), (cpu_cmd, 'machine')]
    
    for c, f in cmd:
        result = order(c, f)
        if f == 'human':
            you = result[0]
            cpu = result[1]
        else:
            cpu = result[0]
            you = result[1]
                    
        
        