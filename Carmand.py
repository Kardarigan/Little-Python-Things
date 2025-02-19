num = 1
pol = 100000
crm = 30
cmd = ['carmand','skip']
while True:
    print('                   Daily report')
    print('__________________________________________________')
    print()
    print('Day = '+str(num))
    print('Money = '+str(pol)+'$')
    print('Carmand = '+str(crm))
    print('__________________________________________________')
    print()
    print(cmd)
    x = input('Farman--> ')
    if x == 'carmand':
        k = input('Chanta(1carmand=100$)')
        pol -= int(k)
        crm += int(k)
    elif x == 'skip':
        r = int(input('Chanta?(skip=100$)'))
        pol -= r*100
        num += r
        continue
    else:
        print('Eror')
        continue
    pol += int(crm)*100
    num+=1