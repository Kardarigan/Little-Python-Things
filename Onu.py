
import random

card = ['red,0', 'red,1', 'red,2', 'red,3', 'red,4', 'red,5', 'red,6', 'red,7', 'red,8', 'red,9',
'blue,0', 'blue,1', 'blue,2', 'blue,3', 'blue,4', 'blue,5', 'blue,6', 'blue,7', 'blue,8', 'blue,9',
'yellow,0', 'yellow,1', 'yellow,2', 'yellow,3', 'yellow,4', 'yellow,5', 'yellow,6', 'yellow,7', 'yellow,8', 'yellow,9',
'green,0', 'green,1', 'green,2', 'green,3', 'green,4', 'green,5', 'green,6', 'green,7', 'green,8', 'green,9']

cpu_card = []
person_card = []

for i in range(7):
    a = random.choice(card)
    cpu_card.append(a)
    card.remove(a)
    b = random.choice(card)
    person_card.append(b)
    card.remove(b)

Asly = random.choice(card)
card.remove(Asly)

def check_cards(rang):
    for c in person_card:
        the_card = c.split(',')
        if rang == the_card[0]:
            return False
    return True
        
        

while cpu_card and person_card:
    print('cart haye shoma: ', *person_card, sep='|')
    print('carte roye zamin: ', Asly)

    person_choice = input('che carty ro mazary??(age mikhay cart jadid var dary 1 ro vared kon)')
    if person_choice == '1':
        if card:
            person_choice = random.choice(card)
            person_card.append(person_choice)
        else:
            print('cart ha tamom shode ast')
            continue
    
    n = Asly.split(',')
    n2 = person_choice.split(',')
    no_card = bool(person_choice in card and check_cards(n[0]))
    
    if n[0] == n2[0] or n[1] == n2[1]:
        if person_choice in person_card or no_card:
            person_card.remove(person_choice)
            Asly = person_choice
        else:
            print('cart namotabar ast')
    else:
        print('cart namotabar ast...')
    if not person_card:
        print('shoma barande shodid')
        break


    valid_move = False
    for i in range(len(cpu_card)):
        n1 = Asly.split(',')
        n2 = cpu_card[i].split(',')
        if n1[0] == n2[0] or n1[1] == n2[1]:
            valid_move = True
            Asly = cpu_card[i]
            cpu_card.remove(cpu_card[i])
            break

    if not valid_move:
        if card:
            new_card = random.choice(card)
            cpu_card.append(new_card)
        else:
            print('cart ha tamom shode ast')

    if not cpu_card:
        print('computer is winner')