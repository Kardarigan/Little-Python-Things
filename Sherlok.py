import random
m=5500
danger=0
Morality=50
Reputation=50
clues = 0  

print ('You are Sherlock holmes and you have 3 servents and you have to slove the crimes that they want you to slove.but...')
def fc ():
    p=int(input('One day a rich man come to you and asked for helped for kidnaping of her son and have red line mark  but when you go to the home to sayed it to the watson ' \
    'you find out that he was kidnapped to and see a letter in the floor that say to you:DONT SLOVE THE CRIMES THAT HAVE A RED LINE MARK ON IT IF YOU NOT WANT TO FIND WATSON IN DEAD. ' \
    '1-You dont attention at this letter and go to slove the crime(price of that crime 100)' \
    '2-You dont slove it and look for a remedy to find watson' \
    ' (if your mony ended you lose)(when your clues go to 7 you will we winner)'))
    print('mony:'+str(m))
    print('danger:'+str(danger))
    print('Morality:'+str(Morality))
    print('Reputation:'+str(Reputation))
    print('clues:'+str(clues))
    if p==1:
        h()
    elif p==2:
        d()
    else:
        print('enter corecct input please.')
def d():
    global m
    d=int(input('One of your servents were kidnaped too A woman came to your house as a servent but she say that she is your dather you want to let him to go  out but that rich man that was kidnapped come back and the woman Amilia,see him twice' \
    '1-You pay the dather to work for you.(she is very clever.)(her salary:90 per mouth)' \
    '2-You let him to go out.'))
    m-=10
    print('mony:'+str(m))
    print('danger:'+str(danger))
    print('Morality:'+str(Morality))
    print('Reputation:'+str(Reputation))
    print('clues:'+str(clues))
    if d==1:
        m-=90
        cd()
    elif d==2:
       m-=10
       cd()
    else:   
       print('enter corecct input please.')
def h():
    global m
    oo=int(input('One of your servents id kidnapped too. You go to the rich man house and want to think one day and say the answer. At the home you see the lettr again that write ' \
    'DONT LET US TO KILL THEM WITH SLOVE THE CRIMES' \
    'FROM RED LINE'
    '1-YOU dont attention at it again ' \
    '2- You say to the rich man that you cant slove it  '))
    m-=10
    print('mony:'+str(m))
    print('danger:'+str(danger))
    print('Morality:'+str(Morality))
    print('Reputation:'+str(Reputation))
    print('clues:'+str(clues))
    if oo==1:
        r()
    elif oo==2:
        d()
    else:
        print('enter corecct input please.')
def r():
    global m
    t=int(input('You have another letter.' \
    'WE WARING TO YOU FOR THE LAST TIME' \
    'RED LINE GROUP' \
    '1-You sayed it at the police' \
    '2- You say to the rich man that you cant slove it '))
    print('mony:'+str(m))
    print('danger:'+str(danger))
    print('Morality:'+str(Morality))
    print('Reputation:'+str(Reputation))
    print('clues:'+str(clues))
    m-=10
    if t==1:
        po()
    elif t==2:
        d()
    else:
        print('enter corecct input please.')
def po():
    global m
    A=int(input('You go to the police Station but when you sayed it to the police none of the polices attention  at it because...' \
    'The red line has member in the police!' \
    'When you back home you Dont now why You cant have the help of the police...' \
    'letter:YOU THINK THAT YOU CAN FIGHT WITH US WITH POLICE?WE HAVE MEMBER THERE TOO.IF YOU WANT WATSON AND YOUR SERVENT YOUR ONLY WAY' \
    'IS LISTENING TO US. PAY 5000 MONY AND PROMISE TO DONT SLOVE THE CRIMSE OF US THEN YOU HAVE YOUR WATSON AND YOUR SERVENT.' \
    'FROM RED LINE GROUP'
    '1-You accept and pay the mony.'
    '2-You dont accept the offer.'))
    
    print('mony:'+str(m))
    print('danger:'+str(danger))
    print('Morality:'+str(Morality))
    print('Reputation:'+str(Reputation))
    print('clues:'+str(clues))
    end_game()
def cd():
    global m
    sa=int(input('A wealthy man visits Sherlock Holmes, pale and shaken.' \
    'He claims that after drinking tea last night, he became violently ill. He believes someone tried to poison him.' \
    'Only three people had access to the tea:'
    '- Alice – the loyal maid who usually prepares the tea.'
    '- James – the gardener, who entered the kitchen briefly to bring flowers.'
    '- Maria – a mysterious guest who claims she never entered the kitchen.' \
    'In the kitchen, a small bottle labeled “Bloodroot” (a rare plant-based poison) is found.' \
    'Alice says: “I left the kitchen for a moment. When I returned, the cups had been rearranged.”' \
    'James says: “I just dropped off the flowers and left.”' \
    'Maria says: “I never went near the kitchen.”' 
    '1️⃣ Interrogate James again' \
    '2️⃣ Examine the flowers for traces of poison' \
    '3️⃣ Ignore the case (it has no Red Line mark)'))
    if sa==1:
        print('“They threatened me... the Red Line. I slipped the poison into the tea using the flowers.”' \
        'You gain a valuable clue about the Red Line’s hideout.' \
        'Outcome: You uncover a connection to the Red Line. No money lost.' \
        'Bonus: +1 clue toward Watson’s rescue')
        
    if sa==2:
        print('You carefully inspect the bouquet James brought.'\
        'Traces of Bloodroot are found on the petals—clear evidence of tampering.'\
        'The client is saved, and James is arrested.'\
        'Outcome: Case solved.'\
        'Reward: +200 money')
        m+=190
        
    if sa==3:
        print('You decide not to get involved.' \
        'The next day, the client dies from poisoning.' \
        'A note arrives: “Indifference has a price.”'\
         'Outcome: You lose public trust.')
        m-=10
    print('mony:'+str(m))
    print('danger:'+str(danger))
    print('Morality:'+str(Morality))
    print('Reputation:'+str(Reputation))
    print('clues:'+str(clues))
    sd=random.randint(1,3)
    if sd==1:
        ck()
    elif sd==2:
        li()
    elif sd==3:
        ry()
def ck():
    global Morality 
    global clues
    global m
    global Reputation
    Ca=int(input('''Location: Rooftop of the London Postal Tower'\
    'Scenario:'/
    'One morning, a pigeon lands on Sherlock Holmes’ windowsill. It carries a message tied to its leg—just a single cryptic note:'\
    '“T+4 @ R.L.”'/

    'Holmes quickly deduces this pigeon was part of a covert communication network. It could be linked to the Red Line group.'
    'Choices for the player:'\
    ' 1️⃣ Decode the message using Holmes’ cipher journal'\
    ' 2️⃣ Trace the pigeon’s origin using flight patterns and postal tower access records'\
    ' 3️⃣ Send a fake reply through the same pigeon to lure out the sende'''))
    if Ca==1:
        print('You decipher the message using Holmes' 
        'cipher journal.'\
        'It reveals: Meeting in 4 days at Red Lines hideout near Thames River.'\
        'Outcome: You have unlocked a new lead.'\
        'Clue +1 | Morality +10')
        Morality+=10
        clues+=1

    elif Ca==2:
        print('You investigate the pigeon’s flight path.'\
            'It leads to a hidden window on the 4th floor of the London Postal Tower.'\
            'You discover a mail handler secretly working for the Red Line group.'\
            'Outcome: Strong evidence uncovered.'\
            'Reputation +10 | Money -20')
        m-=20
        Reputation+=10
    elif Ca==3 :
        print('You send a fake message back: Ready for Drop at Thames.'\
            'The Red Line intercepts it and realizes you are deceiving them.'\
            'Later that night, you receive a new threat letter:WE KNOW YOU ARE PLAYING GAMES MR HOLMES WATSON WILL PAY THE PRICE '\
            'Outcome: You’ve put Watson at greater risk.'
            'Morality -5 | Money -10|danger+10')
        Morality-=5
        M-=10
    print('mony:'+str(m))
    print('danger:'+str(danger))
    print('Morality:'+str(Morality))
    print('Reputation:'+str(Reputation))
    print('clues:'+str(clues))
    li()
def li():
    global m, danger, Morality ,Reputation ,clues
    ex=int(input('Location: A noblemans private library in London'\
                'Scenario:'\
                'Late at night, a maid finds a note written in invisible ink—only visible under candlelight. The message reads:'\
                'He who reads in silence, watches in shadow. Trust not the quiet.'\

                'The suspects in the manor are:'\
                '- Henry – a quiet, book-obsessed gentleman who often stays late in the library.'\
                '- Eliza – a newly hired maid who admits being afraid of the dark and keeps candles lit.'\
                '- Victor – the garden keeper who often says, “Silent men are the most trustworthy.”'\
                '1️⃣ Interrogate Henry about his nightly routines'\
                '2️⃣ Inspect the candle stands for fingerprints'\
                '3️⃣ Surveil Victor with a hidden camera'\
                'Each path leads to a different outcome—only one reveals a full clue connected to Red Line and Watson’s location.'))
    if ex==1:
        print('1️⃣ Interrogate Henry'\
    'Henry remains composed and avoids your questions.'\
    'His responses are vague, and though you sense something is off, no direct evidence is found.'\
    'Outcome: No actionable clue. Time wasted.'\
    'Morality -5 | Reputation -5')
    Morality-=5
    Reputation-=5
    if ex==2:
        print('Fingerprint analysis confirms Eliza touched the candle stand recently.'\
                'She bursts into tears and confesses:'\
                'I found the message... I think Victor is involved. I saw him sneaking in last night.'\
                'Outcome: Partial suspicion toward Victor, but no proof.'\
                'Morality +5 | Reputation +0')
        Morality+=5
        Reputation+=0

    if ex==3:
        print ('The footage reveals Victor entering the library at 2 AM.'\
                'He pulls out a book titled The Silent Watcher and reveals a hidden scroll inside.'
                'The scroll contains: map coordinates, coded orders from the Red Line group, and a direct mention of Watson’s location.'\
                'Outcome: Major breakthrough — you’ve uncovered a critical clue.'\
                'Clue +6 | Morality +10 | Reputation +10')
        clues+=6
        Morality+=10 
        Reputation+=10
    print('mony:'+str(m))
    print('danger:'+str(danger))
    print('Morality:'+str(Morality))
    print('Reputation:'+str(Reputation))
    print('clues:'+str(clues))
    ry() 
def ry():
    global Morality, Reputation, clues
    print("Case: Poison at the Wedding")
    print("During a lavish wedding ceremony, the bride collapses. The cause: a rare toxic plant — Digitalis.")
    print("You must choose how to investigate:")
    print("1. Investigate the guest list")
    print("2. Interrogate the groom’s sister")
    print("3. Analyze the delivered flowers")
    
    choice = input("Enter your choice (1-3): ")
    
    if choice == "1":
        morality += 5
        reputation -= 5
        print("You cross-check the guest list and discover a former Red Line associate near the bride.")
        print("He left before the incident. Suspicious, but no direct clue.")
        print("Morality +5 | Reputation -5 | Clue +0")
        
    elif choice == "2":
        Morality += 10
        Reputation += 10
        clues += 1
        print("She reveals an anonymous threat: 'Give her the poison, or lose your brother.'")
        print("You’ve found a direct connection to Red Line and the toxin source.")
        print("Morality +10 | Reputation +10 | Clue +1")
        end_game()
    elif choice == "3":
        print("No traces of poison found in the flowers.")
        print("Courier says the order came from someone not on the guest list.")
        print("Outcome: Raises suspicion but no concrete lead.")
        print("Morality +0 | Reputation +0 | Clue +0")
        
    else:
        print("Invalid choice. Please enter a number between 1 and 3.")
def final_outcome():
    print("\n🔎 Final Case Review:")
    print(f"Clues gathered: {clues}")
    print(f"Morality score: {Morality}")
    print(f"Reputation score: {Reputation}")
    
    if clues >= 8 and Morality >= 60 and Reputation >= 70:
        print("\n🏆 Ending: True Detective")
        print("You've uncovered the Red Line's headquarters and saved Watson.")
        print("Holmes is celebrated as a hero, but he knows deeper threats still remain...")
    
    elif clues >= 7 and Morality >= 40 and Reputation >= 40:
        print("\n🕯️ Ending: Bittersweet Justice")
        print("You disrupted part of Red Line's plan, but their leader escaped.")
        print("Watson is saved, but public trust in Holmes wavers. A new mystery looms.")

    else:
        print("\n🕳️ Ending: Shattered Case")
        print("Insufficient clues. Red Line vanished into the shadows. Watson's fate remains unknown.")
        print("Holmes sits alone, surrounded by unsolved files... The case haunts him.")
def end_game():
        print("🕵️‍♂️ Reviewing your entire investigation...")
        final_outcome()
fc()