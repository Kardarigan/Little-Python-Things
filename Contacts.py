contacts = {
    'elena': 112,
    'ordak': 888,
    'elon': 689,
    'googoosh': 122
}


while True:
    cmd = input('whats you command: ').split()
    result = ''
    
    if cmd[0] == 'get':
        result = contacts[cmd[1]]
    
    elif cmd[0] == 'add':
        if cmd[1] in contacts:
            cmd_1 = input('this contact is already in your phonebook. do you wanna change its number? ')
            if cmd_1 == 'no':
                continue
            
        contacts[cmd[1]] = int(cmd[2])
        result = f'this guy {cmd[1]} added to your contacts!'
        
    print(result)