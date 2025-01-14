team = [
    {
        "name": "john",
        "role": "developer",
        "is_working": True
    },
    {
        "name": "dora",
        "role": "abdarchi",
        "is_working": True
    },
    {
        "name": "donald",
        "role": "boss",
        "is_working": True 
    },
    {
        "name": "jess",
        "role": "developer",
        "is_working": False
    },
    {
        "name": "dani",
        "role": "developer",
        "is_working": False
    },
    {
        "name": "duck",
        "role": "devops",
        "is_working": True
    },
    {
        "name": "descartes",
        "role": "estakhrtamizkon",
        "is_working": False 
    },
    {
        "name": "daisy",
        "role": "devops",
        "is_working": True
    },
]


def find(name):
    for i in team:
        if i['name'] == name:
            return i



while True:
    print('-'*80)
    cmd = input('what\'s you command sire? ').split()
    
    if cmd[0] == 'report':
        for i in team:
            if i['is_working']:
                print(f'{i['name']} now is working.')
                
    elif cmd[0] == 'rreport':
        for i in team:
            if not i['is_working']:
                print(f'{i['name']} is not in the office.')
                
    elif cmd[0] == 'close':
        for i in team:
            i['is_working'] = False
        print('get the hell out of here')
    
    elif cmd[0] == 'arrived':
        person = find(cmd[1])
        if person['is_working']:
            print('this guy is already in the office')
        else:
            person['is_working'] = True
            print(f'{person['name']} now is working')
    
    elif cmd[0] == 'left':
        person = find(cmd[1])
        if not person['is_working']:
            print('this guy is already out of the office')
        else:
            person['is_working'] = False
            print(f'{person['name']} left her/his work')
    