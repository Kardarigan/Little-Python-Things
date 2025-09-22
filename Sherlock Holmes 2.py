from random import*
import os
sh=0
rw=0
score=rw+sh
from time import*
def print_slow(str):
    for letter in str:
        print(letter, end='', flush=True)
        sleep(0.0000000001)
print_slow('''Title: The Inheritance of Lies'\
'After many quiet years, Sherlock Holmes is called back to London.'\
'A secret government file has appeared—full of old reports, hidden letters, and maps linked to past events.'\
'These papers show secrets from people Holmes once trusted, and connect to parts of his own life that he thought were long forgotten.'\
'As Sherlock investigates, he starts to see signs of a clever and dangerous mind.'
'The style and logic in the clues remind him of someone very familiar—Professor james Moriarty, a name never spoken before, but now impossible to ignore.'\
'The deeper Sherlock goes, the more he questions what is true. He must face facts that could change how he sees his past, his work, and the people around him.' \
''')
sleep(2)
os.system('cls')
def rown():
    global sh,rw,score
    print_slow('As the same time that they want you to slove the crimes,They want another man for the job...')
    print_slow('Rowan Hale is a young and smart detective. He solves cases using logic, psychology, and careful analysis.'\
    'While Sherlock trusts his instincts and experience, Rowan works with data and facts.'\
    'He respects Sherlock but isn’t afraid to challenge him. Their teamwork has a friendly tension—both want to be right, and both want to win.'\
    'Rowan rarely makes mistakes and is fast at spotting clues.'
    'As a player, you’ll feel that you’re not just helping Sherlock—you’re proving yourself against Rowan too.' \
    'You have chalenge with him and if you win the  challenge you win 1000 dollers')
    print_slow('Rowan Hale is 28 years old. He studied criminal psychology and artificial intelligence, combining human behavior with machine-based logic.'\
          'During his time at university, Rowan developed tools to analyze crime scenes using pattern recognition, predictive modeling, and emotional profiling powered by AI.'\
          'His tech-based methods allow him to solve cases faster and with fewer mistakes—making him a valuable partner, and sometimes a quiet rival, to Sherlock Holmes.')
    sleep(2)
    os.system('cls')
    print_slow('''🕵️‍♂️ Case One: The Silent Signature\
A respected university professor is found dead in his office.\
At first, doctors say it was a heart attack. There are no signs of violence, no forced entry, no strange fingerprints.\
But Sherlock notices something strange—a folded note in the professor’s pocket, filled with symbols and numbers.\
The professor’s laptop was wiped clean just minutes before his death. There’s only one hidden file left, with a strange digital mark—like a signature that someone tried to erase.\
The police are unsure what to do. That’s when Sherlock is called in.\
🔍 Main Clues:\
- A coded note in the victim’s pocket\
- A deleted signature on his laptop\
- No sign of physical attack\
- The victim had canceled all meetings that day\
you can:\
1- Question the professor’s assistant about the victim’s final day\
Sherlock suspects someone close may know something hidden.\
2- Analyze the deleted file on the victim’s laptop to track a malicious code\
Sherlock uses decoding tools to uncover a hidden digital link to the medical device.\
3- Send the drink on the desk for toxin analysis\
Sherlock believes the half-full glass may hold the answer.\
Enter the number of the thing that you thing will help you to can slove the main crime.''')
    sleep(2)
    os.system('cls')
    x=int(input())
    if x==1:
        print_slow('❌ Leads to false clues and no useful results.' \
        'Rown find the answer its: Number 2 (✅ Reveals the real method and identity of the killer.)' \
        'and he say to you ' \
        'I think that you are more inteligent.')
        sleep(2)
        os.system('cls')
        print_slow(f'Sherlocks score: {sh}')
        print_slow(f'Rown score: {rw} ')
        os.system('cls')
        rw+=1
        SC()
    if x==2:
        print_slow('✅ Reveals the real method and identity of the killer.' \
        'You say to rown that cant find the answer:' \
        'The new ways arent alwasy correct! ')
        sleep(2)
        os.system('cls')
        sh+=1
        print_slow(f'Sherlocks score: {sh}')
        print_slow(f'Rown score: {rw} ')
        os.system('cls')
        SC()
    if x==3:
        print_slow('❌ Test results are negative, and the theory doesn’t match the crime.' \
                'Rown find the answer its: Number 2 (✅ Reveals the real method and identity of the killer.)' \
                'and he say to you ' \
                'I i expeted more from my pattern')
        sleep(2)
        os.system('cls')
        print_slow(f'Sherlocks score: {sh}')
        print_slow(f'Rown score: {rw} ')
        rw+=1
        SC()
def SC():
    global sh,rw,score
    print_slow('''🕵️ Case Title: The Chessboard Cipher
Late one stormy evening, Richard Sterling, a renowned mathematics professor, is found dead in his study. On his desk:\
an unfinished chessboard showing a “checkmate in three moves” scenario.\
On the blackboard behind him: a mysterious equation resembling modern cryptography. No fingerprints. No witnesses. Only silence... and calculation.\
Sherlock Holmes and Rowan Hale suspect this isn't just a murder—it's a mental duel orchestrated by someone frighteningly intelligent.
For the first time, a name echoes in whispers: Professor James Moriarty.\
The player must decide how to proceed:\
1️⃣ Interrogate Miles Ketting – Sterling’s former student

2️⃣ Decrypt the equation using software analysis

3️⃣ Analyze the victim’s journal and the symbols in his unfinished story''')
    z=int(input())
    sleep(2)
    os.system('cls')
    if z==1:
        print('Sherlock interviews Miles, who had prior links to Moriarty. His answers are emotional yet inconsistent.\
- ❌ Misleading path: Miles breaks under pressure, but his intel is fake. The real killer remains hidden.')
        os.system('cls')
        print('Rown find the killer its about Moriaty:' \
        'He say to you:' \
        'I Find your old enemy')
        sleep(2)
        rw+=1
        n2()
    if z==2:
        w=input('The player applies advanced cryptographic tools to solve the blackboard formula.\
- It looks a trap laid by Moriarty: The equation leads to a  location,but you dont no its true or false'
'If you think that place that it will have murder in it enter Yes if not enter No').lower()
        if w=='yes':
            ksh()
        if w=='no':
            print('It was a place thet they plan for your death its better to dont go.')
            n2()
    if z==3:
        print('Hidden within Sterling’s fictional writing are veiled references to real-life patterns and psychological triggers.\
- ✅ True path: The metaphors match with prior evidence. The player decodes Moriarty’s mental framework.' \
'Now, only you have to go on tome for find moriaty and kiling a presen')
        n2()
    sleep(2)
Ssc=0
def ksh():
    global sh,rw,Ssc,score
    print_slow('When you go to the place that you think is the place of a new murder,suddenly you see a play machine,A writing is on it:' \
    'LifE iS GAme.WHITE gameing Some TruTHes will be realivED.' \
    'if you want to play the game:' \
    'enter 1' \
    'if you dont want to play ' \
    'enter 2')
    sleep(2)
    a=int(input())
    if a==1:
        hand=['rock','paper','scirors']
        for i in range(0,5):
            x=input('Rock,paper or scirors?').lower()
            pc=choice(hand)
            print('pcs choice:', pc)
            if x==pc:
                print('draw')
            elif x=='rock':
                if pc=="paper":
                    print('you lose')
                else:
                    print('you win')
            elif x=='paper':
                if pc=="scirors":
                    print('you lose')
                else:
                    print('you win')
                    Ssc+=1
            elif x=='scirors':
                if pc=="rock":
                    print('you lose')
                else:
                    print('you win')
        print_slow(f'''After This game, you dont got any thing but you hear a sound You see moriaty with his men He say to you:' \
        'Hi, old enemy.I know that you will listen to that math quistion.' \
        'it had lots of risk you can find me but i can find you to.' \
        'you play with that game and with your score you have time to defence yourself {Ssc} is your score.
        you cant do anyting and at last second rown enter with his mens. Moriarty now that he cant kill all of them and ran away.
Sherlock an Rown  are chasing him when the moriraty enter a door and close it with a special lock.''')
        w=int(input('''You see this word in the lock.' \
        'sh.w.i.y.s.c.i.t.r.p.c.' \
        'You dont now what is it mean but rown asked you:' \
        'what do you see in that room and you say him about thq minigame and he say what is you is your score enter it.'''))
        if w==Ssc or Z==Ssc:
            print('The lock open and you go to the next room')
        else:
            print('Rown said: Its incorrect.if you dont now it we have to come back.')
            Z=int(input('Enter your score again'))
            sleep(2)
            os.access('sls')
            n2()
def n2():
    global Ssc,score
    print('when you go to the place you see that minigame')
    for i in range(0,5):
            x=input('Rock,paper or scirors?').lower()
            hand=['rock','paper','scirors']
            pc=choice(hand)
            print('pcs choice:', pc)
            if x==pc:
                print('draw')
            elif x=='rock':
                if pc=="paper":
                    print('you lose')
                else:
                    print('you win')
            elif x=='paper':
                if pc=="scirors":
                    print('you lose')
                else:
                    print('you win')
                    Ssc+=1
            elif x=='scirors':
                if pc=="rock":
                    print('you lose')
                else:
                    print('you win')
    print('After that, you see moriarty and you dont let him to kill that ppreson and then moriarty try to escaped but rown dont let him and he ' \
    'ran away under groun and you see a lock..... ')
    print('''You see this word in the lock.' \
        'sh.w.i.y.s.c.i.t.r.p.c.' \
        'You dont now what is it mean but rown asked you:' \
        'what do you see in that room and you say him about the minigame and he say what is you is your score enter it.''')
    while True:
        Zi=int(input('Enter your score.'))
        if Zi==Ssc:
            print('The lock open and you go to the next room')
            score+=1
            break
        else:
            print('Rown said: Its incorrect.if you dont now it we have to come back.')
    g=input('in the second room you se another lock:' \
        'What is The name of porfesser Moriaty?').lower()
    if g=='james':
        print('Correct! and you go to the next room.')
        score+=1
    else:
        print('it isnt correct!It is a very easy qustion.')
        g=input('Write his name.')
    print_slow('''🧠 Stage Four: The Hall of Illusions

You enter a room with walls made of mirrors. But these mirrors don’t show your reflection — they show versions of you.

In one mirror, you are defeated, broken, and alone.  
In another, you are holding a weapon, standing over a body.  
In the third, you see Moriarty — but with your face.

Suddenly, a voice echoes through the room:
"Moriarty isn’t your enemy. He’s the version of you that dared to think differently."

In the center of the room, a strange machine lights up. It asks you three questions. Your answers will shape your path.

1 - If saving one life means sacrificing ten, would you do it?
2 - Is truth always better than a comforting lie?
3 - Can you trust someone who once betrayed you?

Choose your mindset:
1 - Answer with logic
2 - Answer with emotion''')

    choices = int(input('Enter your choice: '))
    if choices == 1:
        print_slow('''✅ You answer with logic.
    The mirrors shift and reveal a hidden panel.
    Inside, you find a coded message:
    "The final move is hidden in the mind, not the board."
    You gain a clue for the final stage.''')
        score+=1
    elif choices == 2:
        print_slow('''🧠 You answer with emotion.
    The mirrors crack and a memory appears — your childhood, your fear of being wrong.
    You feel something change inside.
    You gain insight, but no clue.''')
    print_slow('''⚖️ Stage Five: The Moral Choice

    You and Rowan enter a chamber with two steel doors.

    Behind Door One: A child, innocent and afraid.  
    Behind Door Two: A secret agent with vital information about Moriarty.

    Moriarty’s voice echoes:
    "Only one can be saved. The other will be forgotten.
    Choose wisely, Sherlock. Your future depends on it."

    You must decide:
    1 - Save the child
    2 - Save the agent
    3 - Try to save both (risky)''')

    choices = int(input('Enter your choice: '))
    if choices == 1:
        print_slow('''❤️ You save the child.
    The agent is lost, and Moriarty’s plan continues.
    Rowan looks at you: "You chose humanity. But we lost the lead."''')
        ending()
    elif choices == 2:
        print_slow('''🧠 You save the agent.
    He gives you key intel about Moriarty’s next move.
    But the child is gone.
    Rowan says: "We did what we had to. But it hurts."''')
        ending()
    elif choices == 3:
        Z=randint(1,2)
        print_slow('🎲 You try to save both.')
        print_slow('But you dont succfull')
        ending()
        if Z==1:
            print('''     
            You disable the traps and unlock both doors.
            ✅ Success! You save them both.
            Rowan smiles: "That was brilliant, Sherlock."
            You gain full trust — and a bonus clue for the final stage.''')
            ending()
    score+=1
def ending():
    global score
    score= sh+rw
    print(f"\n🧮 Final Investigation Score: {score}")
    print("🔚 Ending:")
    print('For your good team work your scores + to each other.')
    if score >= 6:
        print("🎉 Sherlock triumphs. Moriarty is defeated. London breathes again.")
        print("🧠 Final Case Solved:")
        print("The coded journal, the poisoned drink, the chessboard cipher — all point to one mind.")
        print("Sherlock presents the evidence to the government. Rowan confirms the psychological patterns.")
        print("The truth is undeniable: Moriarty orchestrated everything.")
        print("His network collapses. His name is no longer a whisper — it's a warning.")
        print("Sherlock closes the file: 'The inheritance of lies ends here.'")
    elif 3 <= score < 6:
        print("⚖️ Partial victory. Moriarty escapes, but his plans are delayed.")
        print("The clues were close, but not enough to convict him.")
        print("Rowan says: 'We’ll get him next time. He’s not invincible.'")
    elif 0 <= score < 3:
        print("😶 Sherlock survives, but doubts linger. The game continues.")
        print("Moriarty’s trail fades. The city sleeps uneasy.")
    else:
        print("💀 Sherlock falls. Moriarty vanishes into the shadows.")
        print("His legacy grows darker. The lies live on.")
    input()
rown()