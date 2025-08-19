import random
def shoroo():
    print("""\nSaLaM :)
    Shoma dar yek khaneh ghadimi matrooke hastid.
    Bad az miyan darz-haye panjare mivazad...""")
    entekhab_marhale_1()
def entekhab_marhale_1():
    j1='''
1) Be tabaghe bala beravid
2) Be zirzamin beravid'''
    j2='''
1) Dar ra barresi konid
2) Az panjare birun ra negah konid'''
    w=[j1,j2]
    et=random.choice(w)
    print(et)
    a=int(input())
    if et==j1:
        if a==1:
            ma21()
        else:
            ma22()
    elif et==j2:
        if a==1:
            ma23()
        else:
            ma24()
    else:
        print('incorrect input :(')
        entekhab_marhale_1()
# Marhale 2 functions
def ma21():
    print("""\nShoma be tabaghe bala mirid...
    Sedaye jirjirak-ha ghat mishavad.""")
    
    j1 ='''
1) Dar samte chap ra baz konid
2) Dar samte rast ra baz konid'''
    
    j2 ='''
1) Be zire pelleha panah begirid
2) Baz gardid va be tabaghe paein bargardid'''
    w=[j1,j2]
    et=random.choice(w)
    print(et)
    a=int(input())
    if et==j1:
        if a==1:
            ma31()
        else:
            ma32()
    elif et==j2:
        if a==1:
            ma33()
        else:
            ma34()
    else:
        print('incorrect input :(')
        ma21()
def ma22():
    print("""\nShoma be zirzamin mirid...
    Hava sardtar mishavad.""")
    
    j1 = '''
1) Jabeh ghadimi ra barresi konid
2) Be saye-i dar goshe khire shavid'''
    
    j2 = '''
1) Dar zirzamin gerdahi konid
2) Shame ra roshan konid'''
    w=[j1,j2]
    et=random.choice(w)
    print(et)
    a=int(input())
    if et==j1:
        if a==1:
            ma35()
        else:
            ma36()
    elif et==j2:
        if a==1:
            ma37()
        else:
            ma38()
    else:
        print('incorrect input :(')
        ma22()
def ma23():
    print("""\nShoma dar ra barresi mikonid...
    Ghoff ast amma kelidi kenar an gharar darad.""")
    
    j1 = '''
1) Kelid ra bardarid
2) Kelid ra nadideh begirid'''
    
    j2 = '''
1) Dar ra ba zoof bezanid
2) Az dar dur shavid'''
    w=[j1,j2]
    et=random.choice(w)
    print(et)
    a=int(input())
    if et==j1:
        if a==1:
            ma39()
        else:
            ma310()
    elif et==j2:
        if a==1:
            ma311()
        else:
            ma312()
    else:
        print('incorrect input :(')
        ma23()
def ma24():
    print("""\nShoma az panjare birun ra negah mikonid...
    Hayat por az barg-haye khoshk ast.""")
    j1 = '''
1) Faryad bezanid
2) Sari az panjare dur shavid'''
    
    j2 = '''
3) Barg-ha ra barresi konid
4) Panjare ra komelan baz konid'''
    w=[j1,j2]
    et=random.choice(w)
    print(et)
    a=int(input())
    if et==j1:
        if a==1:
            ma313()
        else:
            ma314()
    elif et==j2:
        if a==1:
            ma315()
        else:
            ma316()
    else:
        print('incorrect input :(')
        ma24()
# Marhale 3 functions 
def ma31():
    print("""\nDar samte chap ra baz mikonid...
    Otaghi por az aroosak-haye shekaste mibinid.""")
    
    j = '''
1) Be aroosak-ha nazdik shavid"
2) Dar ra bastid va az otagh firar konid'''
    print(j)
    a=int(input())
    if a==1:
        ma41()
    elif a==2:
        ma42()
    else:
        print('incorrect input :(')
        ma31()
def ma32():
    print("""\nDar samte rast ra baz mikonid...
    Otaghi khali ast amma aineh bozorgi dar moghabel-e shoma ast.""")
    j = '''
1) Be aineh nazdik shavid
2) Aineh ra shekanid'''
    print(j)
    a=int(input())
    if a==1:
        ma43()
    elif a==2:
        ma44()
    else:
        print('incorrect input :(')
        ma32()
def ma33():
    print("""\nShoma be zire pelleha panah mibarid...
    Dar hamin hal, pelleha shoroo be larzidan mikonand!""")
    
    j= '''
1) Sari az zire pelleha birun biaid
2) Dar zire pelleha bemanid'''
    print(j)
    a=int(input())
    if a==1:
        ma45()
    elif a==2:
        ma46()
    else:
        print('incorrect input :(')
        ma33()
def ma34():
    print("""\nShoma baz gardid va be tabaghe paein raftid...
    Amma dar rah, pay-e shoma az ruye pellah mished!""")
    
    j = '''
1) Be donbale rah-e farar begardid
2) Az pellah-ha gerefte shavid'''
    print(j)
    a=int(input())
    if a==1:
        ma47()
    elif a==2:
        ma48()
    else:
        print('incorrect input :(')
        ma34()
def ma35():
    print("""\nJabeh ghadimi ra baz mikonid...
    Dakhel an name-i zard shode ast.""")
    
    j= '''
1) Name ra bekhanid
2) Name ra part konid'''
    print(j)
    a=int(input())
    if a==1:
        ma49()
    elif a==2:
        ma410()
    else:
        print('incorrect input :(')
        ma35()
def ma36():
    print("""\nBe saye khire mishavid...
    Saye shoroo be roshd mikonad!""")
    
    j = '''
1) Az saye dur shavid
2) Be saye negah konid'''
    print(j)
    a=int(input())
    if a==1:
        ma411()
    elif a==2:
        ma412()
    else:
        print('incorrect input :(')
        ma36()
def ma37():
    print("""\nShoma dar zirzamin gerdahi mikonid...
    Dar yek goshe, chizi shoma ra seda mizanad!""")
    
    j = '''
1) Be seda nazdik shavi
2) Az an ja firar konid'''
    print(j)
    a=int(input())
    if a==1:
        ma413()
    elif a==2:
        ma414()
    else:
        print('incorrect input :(')
        ma37()
def ma38():
    print("""\nShoma shame ra roshan mikonid...
    Dar noor-e shame, sayeh-ha shoroo be harekat mikonand!""")
    j = '''
1) Shame ra khamosh konid
2) Be donbale sayeh-ha begardid'''
    print(j)
    a=int(input())
    if a==1:
        ma415()
    elif a==2:
        ma416()
    else:
        print('incorrect input :(')
        ma38()
def ma39():
    print("""\nKelid ra barmidarid...
    Nagahan dar az posht baz mishavad!""")
    
    j = '''
1) Kelid ra estefade konid
2) Kelid ra part konid'''
    print(j)
    a=int(input())
    if a==1:
        ma417()
    elif a==2:
        ma418()
    else:
        print('incorrect input :(')
        ma39()
def ma310():
    print("""\nKelid ra nadideh migirid...
    Sedaye zarbe-i az posht dar miayad.""")
    j= '''
1) Az dar dur shavid
2) Dar ra baz konid'''
    print(j)
    a=int(input())
    if a==1:
        ma419()
    elif a==2:
        ma420()
    else:
        print('incorrect input :(')
        ma310()
def ma311():
    print("""\nShoma dar ra ba zoof mizanid...
    Dar pasokh, sedaye zan-i az posht-e dar mishenavid!""")
    
    j = '''
1) Dar ra baz konid
2) Az dar firar konid'''
    print(j)
    a=int(input())
    if a==1:
        ma421()
    elif a==2:
        ma422()
    else:
        print('incorrect input :(')
        ma311()
def ma312():
    print("""\nShoma az dar dur mishavid...
    Amma dar hamin hal, dar khod-ba-khod baz mishavad!""")
    
    j = '''
1) Be dar nazdik shavid
2) Be tabaghe bala bargardid'''
    print(j)
    a=int(input())
    if a==1:
        ma423()
    elif a==2:
        ma424()
    else:
        print('incorrect input :(')
        ma312()
def ma313():
    print("""\nFaryad mizanid...
    Sokoot-e sangini hame ja ra far migirad.""")
    
    j= '''
1) Dobare faryad bezanid
2) Sokoot konid'''
    print(j)
    a=int(input())
    if a==1:
        ma425()
    elif a==2:
        ma426()
    else:
        print('incorrect input :(')
        ma313()
def ma314():
    print("""\nAz panjare dur mishavid...
    Amma panjare khod-ba-khod baz mishavad!""")
    
    j = '''
1) Panjare ra bastid
2) Az otagh firar konid'''
    print(j)
    a=int(input())
    if a==1:
        ma427()
    elif a==2:
        ma428()
    else:
        print('incorrect input :(')
        ma314()
def ma315():
    print("""\nShoma barg-ha ra barresi mikonid...
    Barg-ha shoroo be harekat mikonand va shakl-e chehreh-ha ra be khod migirand!""")
    
    j = '''
1) Barg-ha ra part konid
2) Az barg-ha dur shavid'''
    print(j)
    a=int(input())
    if a==1:
        ma429()
    elif a==2:
        ma430()
    else:
        print('incorrect input :(')
        ma315()
def ma316():
    print("""\nShoma panjare ra komelan baz mikonid...
    Nagahan, yek bade garm az birun vared mishavad!""")
    
    j = '''
1) Panjare ra bastid
2) Az panjare birun parid'''
    print(j)
    a=int(input())
    if a==1:
        ma431()
    elif a==2:
        ma432()
    else:
        print('incorrect input :(')
        ma316()
# Marhale 4 functions
def ma41():
    print("""\nBe aroosak-ha nazdik mishavid...
    Aroosak-ha cheshm-hashan ra baz mikonand!""")
    payan()
    print("Aroosak-ha shoma ra dar bar migirand va hame ja tarik mishavad!")
def ma42():
    print("""\nDar ra bastid va az otagh farar mikonid...
    Amma dar rah, pelleha shekaste mishavand!""")
    payan()
    print("Shoma be zamin mikhorid va hich gah az khab-e zire khak bidar nemishavid!")
def ma43():
    print("""\nBe aineh nazdik mishavid...
    Tasvir-e shoma dar aineh az shoma joda mishavad!""")
    payan()
    print("Tasvir-e shoma az aineh birun miayad va shoma ra jaygozin mikonad!")
def ma44():
    print("""\nAineh ra mishkanid...
    Az shekast-e aineh, khoon miayad!""")
    payan()
    print("Shekast-ha shoma ra boride boride mikonand va hame ja ra khoon migirad!")
def ma45():
    print("""\nAz zire pelleha birun miaid...
    Amma pelleha shekaste mishavand!""")
    payan()
    print("Yek tike pelleh be gardan-e shoma mikhorad va hame chiz siyah mishavad!")
def ma46():
    print("""\nDar zire pelleha mimanid...
    Pelleha kamelan shekaste mishavand!""")
    payan()
    print("Shoma zir-e khare pile-ye pelleha mandeid va kasi shoma ra nemibinad!")
def ma47():
    print("""\nBe donbale rah-e farar migardid...
    Amma hame dar-ha ghofl hastand!""")
    payan()
    print("Shoma dar ghoff-e khaneh gharar migirid va aheste aheste havash ra az dast midahid!")
def ma48():
    print("""\nAz pellah-ha gerefte mishavid...
    Nagahan pellah-ha shoroo be larzidan mikonand!""")
    payan()
    print("Pellah-ha shekaste mishavand va shoma be zamin mikhorid!")
def ma49():
    print("""\nName ra mikhani...
    Matn-e name be zabane gharibe ast!""")
    payan()
    print("Name shoma ra tabdil be yek aroosak mikonad!")
def ma410():
    print("""\nName ra part mikonid...
    Name atash migirad!""")
    payan()
    print("Atash-e name hame otagh ra far migirad!")
def ma411():
    print("""\nAz saye dur mishavid...
    Amma saye shoma ra raha nemikonad!""")
    payan()
    print("Saye shoma ra mighirad va dar khod mikhanad!")
def ma412():
    print("""\nBe saye negah mikonid...
    Saye cheshm-hai darad!""")
    payan()
    print("Cheshm-ha-ye saye shoma ra majboor mikonand be an negah konid!")
def ma413():
    print("""\nBe seda nazdik mishavid...
    Sedaa az yek aks-e ghadimi miayad!""")
    payan()
    print("Aks shoma ra be dakhel-e khod mikashad!")
def ma414():
    print("""\nAz an ja firar mikonid...
    Amma dar-ha hame ghoff hastand!""")
    payan()
    print("Shoma dar zirzamin gharar migirid va havash dar miravad!")
def ma415():
    print("""\nAz an ja firar mikonid...
    Amma dar-ha hame ghoff hastand!""")
    payan()
    print("Shoma dar zirzamin gharar migirid va havash dar miravad!")
def ma416():
    print("""\nBe donbale soyeh-ha migardid...
    Soyeh-ha shoma ra be yek otagh-e digar mibarand!""")
    payan()
    print("Shoma dar otagh-e aroosak-ha gharar migirid!")
def ma417():
    print("""\nKelid ra estefade mikonid...
    Dar baz mishavad!""")
    payan()
    print("Posht-e dar, yek donya-ye digar ast va shoma dar an gom mishavid!")
def ma418():
    print("""\nKelid ra part mikonid...
    Kelid az dast-e shoma parvaz mikonad!""")
    payan()
    print("Kelid be gardan-e shoma mikhorad va shoma mimirid!")
def ma419():
    print("""\nAz dar dur mishavid...
    Amma dar shoma ra mikhahad!""")
    payan()
    print("Dar shoma ra be dakhel mikashad!")
def ma420():
    print("""\nDar ra baz mikonid...
    Posht-e dar heychi nist!""")
    payan()
    print("Shoma be yek abysh-e siyah meoftid!")
def ma421():
    print("""\nDar ra baz mikonid...
    Zan-e pir heychi nemiguyad!""")
    payan()
    print("Zan-e pir shoma ra be ghalb-e khod mikhorad!")
def ma422():
    print("""\nAz dar firar mikonid...
    Amma dar-ha hame ghoff hastand!""")
    payan()
    print("Shoma dar ghoff-e khaneh gharar migirid!")
def ma423():
    print("""\nBe dar nazdik mishavid...
    Dar khod-ba-khod baz mishavad!""")
    payan()
    print("Dast-hai az dar birun miayand va shoma ra mikashand!")
def ma424():
    print("""\nBe tabaghe bala bargardid...
    Amma pelleha shekaste mishavand!""")
    payan()
    print("Shoma be zamin mikhorid va gardan-e shoma shekaste mishavad!")
def ma425():
    print("""\nDobare faryad mizanid...
    Pasokh-e faryad az hame ja miayad!""")
    payan()
    print("Seda-ha shoma ra majboor mikonand be zamin bekhorid!")
def ma426():
    print("""\nSokoot mikonid...
    Sokoot harasnak tar mishavad!""")
    payan()
    print("Shoma his mikonid ke nafas-e kasi ru-ye gardan-e shoma ast!")
def ma427():
    print("""\nPanjare ra bastid...
    Amma panjare dobare baz mishavad!""")
    payan()
    print("Dast-hei az panjare birun miayand va shoma ra mikashand!")
def ma428():
    print("""\nAz otagh firar mikonid...
    Amma dar-ha hame ghoff hastand!""")
    payan()
    print("Shoma dar ghoff-e khaneh gharar migirid!")
def ma429():
    print("""\nBarg-ha ra part mikonid...
    Barg-ha khoon miazarand!""")
    payan()
    print("Khoon-e barg-ha shoma ra ghargh mikonad!")
def ma430():
    print("""\nAz barg-ha dur mishavid...
    Amma barg-ha shoma ra mikhahand!""")
    payan()
    print("Barg-ha shoma ra mighirand va dar khod mikhanand!")
def ma431():
    print("""\nPanjare ra bastid...
    Amma bade garm dar dakhel mahdood mishavad!""")
    payan()
    print("Hava garm shoma ra mikhoshk mikonad!")
def ma432():
    print("""\nAz panjare birun miparid...
    Amma zamin az shoma dur mishavad!""")
    payan()
    print("Shoma dar havaye siyah gom mishavid!")
# Marhale payani funktion
def payan():
    print("Payan-e dastan :)")
shoroo()