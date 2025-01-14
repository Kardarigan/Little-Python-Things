team = [
    {'name' : 'eddie','hastan': True , 'age' : 40 , 'why' : 'eddie : for he was killed a police .'} , 
    {'name' : 'barms','hastan': True , 'age' : 100 , 'why' : "barms : for he was haidra\'s spy ."} ,
    {'name' : 'starck','hastan': False , 'age' : 45 , 'why' : ""} ,
    {'name' : 'ragers','hastan': False , 'age' : 100 , 'why' : ""} ,
    {'name' : 'cent' , 'hastan' : False , 'age' : 40  , 'why' : ""} ,
    {'name' : 'bruce' , 'hastan' : True , 'age' : 40  , 'why' : "bruce : for he was killed falcone ."} ,
    {'name' : 'arthur' , 'hastan' : True , 'age' : 36 , 'why' : "arthur : for he was killed mayka ."} ,
    {'name' : 'duch' , 'hastan' : False , 'age' : 50 , 'why' : ""} ,
    {'name' : 'cj' , 'hastan' : True , 'age' : 100 , 'why' : "cj : for he was robed bigest city\'s bank ."} ,
    {'name' : 'sherek' , 'hastan' : True , 'age' : 100 , 'why' : "sherek : for he was killed his donkey ."} ,
    {'name' : 'parker' , 'hastan' : False , 'age' : 20 , 'why' : ""} ,
    {'name' : 'mamad_gholi' , 'hastan' : False , 'age' : 10000000000000000000000000000000000000000000000000000000000000000 , 'why' : ""} ,
    {'name' : 'potter' , 'hastan' : True , 'age' : 45 , 'why' : "potter : for he was braked timeline ."} ,
    {'name' : 'voldemord' , 'hastan' : True , 'age' : 100 , 'why' : "voldemord : for he was killed lots of people"} 
    
]

def find(name):
    for i in team :
        if i['name'] == name :
            return i 
        
while True :
    cmd = input('enter your command : ').split()
    if cmd[0] == 'report' :
        for i in team :
            if i['hastan'] :
                print(i['name'])
    elif cmd[0] == 'out' :
        person = find(cmd[1])
        person['hastan'] = False
        print('You got this person out of jail .')
        person['why'] = ''

    elif cmd[0] == 'put' :
        if cmd[1] not in team :
            print(cmd[1] + 'not in jail ! ')
            continue
        person = find(cmd[1])
        person['hastan'] = True
        find(cmd[1])['why']
        print('You put this person in jail .')
        B = input('why ? ')
        (cmd[1])['why'] = B

    elif cmd[0] == 'age' : 
        for i in team :
            if i[''] >= int(cmd[1]) :
                print(i['name'])

    elif cmd[0] == 'why' :
        for i in team :
            if i['why'] :
                print(i['why'])
