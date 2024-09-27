S = True

def start():
    print('''\t\t\t\t\t hello and welcome!
          you\'re lyin on your bed being bored when suddenly a portal opens and drags you in it...
          after some minutes of beig in a black hole
          you find yourself sitting on a couch near the fire place, having a book on your lap, the book\'s title \" Restricted Spells\"
          \t\t\t\t-welcome to Harry Potter\'s world,, you\'re in Slytherin Commonroom
          
          you hear a sound from your back...''')
    choice_1()

def choice_1():
    s = int(input('1) standing up and following the sound \n2) sit there and continiue to read'))
    if s == 1:
        standing()
    if s == 2:
        sitting()

def standing():
    print('''you stand up, and start to follow the sound
          you walk out of the common room, and make your step in the dark hallway..''')
    w = int(input('1) take your wond out and cast\"Lumos\" \nor \n2) take back inside and grab a flash ligh'))
    if w == 1:
        wond()
    if w == 2:
        back()

def sitting():
    print('as you continiue to read your book you sence that sth is on your back')
    r = int(input('1) turn around and face it\n\t\t or\n2) stand and start to run'))
    if r == 1:
        face()
    if r == 2:
        run()

def wond():
    print('''you take your wond wond and cast the spell, now is much better. at least you can see.
          you look up and see a dead, bloody corpse, tangled upp from the roof
          there\'s a massage next to him written with blood that says\"The Chamber of Secret has been opened... Enemies of the heir be Awar\"
          it has one meaning==> Tom Riddle is back...''')
    t = int(input('1) you can scream and make MR Filch to find you \n2) or you walk to take him down'))  
    if t == 1:
        found()
    if t == 2:
        saving()


def back():
    print('''you get back inside, and grab a flash light from the desk
          as you turn to get back you see a enormous spider....
          but no that is not a spider that\'s \"Aragog\"
          P.S: they eat meat... human\'s meat''')
    q = int(input('1) you take your wond and start a fight \n2) run==>'))
    if q == 1:
        fight()
    if q == 2:
        run2()

def face():
    print('''you see it the giant snack that crawls...
          you take your wound''')
    o = int(input('1) you cast the first spell and start to run out of the common room \n2) you cast the spell and start the fight'))
    if o == 1:
        run3()
    if o == 2:
        fight2()

def run():
    print('''you just stand up and start to run without even looking, you run out of the commonroom, you face the a dead body lying on ground covered in blood.
          you continiue to run until you hide behind a wall. as you look in front of you, you see a cat being tangled up from the roof
          there\'s no blood the cat has been froze...''')
    q = int(input('1) you find out what creature was in the commonroom \n2) you don\'t know'))
    if q == 1:
        discovery()
    if q == 2:
        cat()


def found():
    print('''Good Job!
          MR Filch found you... good Lock with detention 😎''')
    end()
    
def saving():
    print('''you walk toward the guy in rush. you open the rope, you take him down but his dead
          you find a twisted piece of paper in his hand. you open it \"follow the sound to to Second_floor''')
    y = int(input('1) you listen to the paper \n2) you ignore it and continiue your own path'))
    if y == 1:
        secondfloor()
    if y == 2:
        myway()

def fight():
    print('''the sspider attacks to you, dogde and start to cast spells toward the Aragog''')
    e = int(input('1) do you want to kill it? \n2) you want it to pass put?==>'))
    if e == 1:
        dead()
    if e == 2:
        passout()

def run2():
    print('''you start to run out of the commonroom with the flash light,
          as you run out you see a bloody corpse tangled up on the wall in front of you tend to scream but the spider has folowed you out
          the spider grabs your foot, so you fall on the ground...''')
    u = int(input('1) you take your wond out and you kill it \n2) you give up!'))
    if u == 1:
        kill()
    if u == 2:
        giveup()

def run3():
    print('''you cast the first spell successfully and run out of the commonroom. you run and hide behinde a wall.
          but you still can hear the snack\'s crowlling...''')
    p = int(input('1) you come out and cast a spell on snake and fight with it \n2) stay hidden and let the snake leave==>'))
    if p == 1:
        fight3()
    if p ==2:
        print('game over! snakes still alive')
        end()

def fight2():
    print('''you cast the first spell and start to run around the room. and you cast more spells toward it''')
    n = int(input('1) kill it \n\t\t orrr \n2) pass it out'))
    if n == 1:
        print('Good job, you did it!')
        end()
    if n == 2:
        teachers()

def discovery():
    print('''you think with yourself \" i heard snake\'s sound from my back and a corpe. and this cat is froze
          it means that... that is a \"Basilisk\" the most dangerous snake in the world''')
    z = int(input('1) you go back to see if you\'re right \n2) you stay in you\'re place'))
    if z == 1:
        turning()
    if z == 2:
        print('cowered, you lose!')
        end()

def cat():
    print('''you\'re looking at the cat when you hear snake\'s sound down the hallway''')
    x = int(input('1) you stay hidden \n2) you take a look'))
    if x == 1:
        print('little chicky')
        end()
    if x == 2:
        takelook()

def secondfloor():
    print('''you listen and make your way through the halls till you get to stairs
          you go up the moving_stairs, you follow the sound in the girl\'s restroom.
          you open the door and get in, suddenly you see the ghost of Martel''')
    c = int(input('1) stay and get information from martel\n2) followin the voice'))
    if c == 1:
        talking()
    if c == 2:
        following()

def myway():
    print('''you think it\'s a trape and you go on your way''')
    v = int(input('1) you get lost \n2) you find the way==>'))
    if v == 1:
        print('loser...')
        end()
    if v == 2:
        way()

def dead():
    print('''you cast the Avracadabra spell and you kill the spider
          you walk out of the room and you see a dead body on the ground
          he\'s dead''')
    b = int(input('1) continiue \n2) take care of the dead body'))
    if b == 1:
        continiue()
    if b == 2:
        end()

def passout():
    print('''you cast the spell Stopefight on the spider, and the spider pass out. 
          you walk out following the sound you follow the sound to second floor. you get in girl\'s restrom. you see a snake in front of you...
          that\'s not a regulre snake it\'s an Basilisk... the most dangrous creature on earth''')
    m = int(int('1) you fight with it \n2) you close the door and run away'))
    if m == 1:
        fight4()
    if m == 2:
        print('cowerd')
        end()

def kill():
    print('''you take you\'re wond and cast a spell that kills the spider
          you get up; with your leg hurted
          again you hear the sound''')
    a = int(input('1) you scared and you don\'t go for it \n2) you follow it'))
    if a == 1:
        print('idiot')
        end()
    if a == 2:
        following2()

def giveup():
    print('''the Aragog starts to eat you alive and only think you can do is to yell''')
    end()

def fight3():
    print('''you put yourself together together and jump out
          you start to fight with the snack... you cast spells and run around''')
    k = int(input('1) you kill the snack \n2) snake kills you'))
    if k  == 1:
        print('Good job')
        end()
    if k == 2:
        print('you did your best, but you lost')
        end()

def teachers():
    print('''as soon as the snake is passed out you go to proffesor Snape for help and he come\'s and take the snake away..
          good job''')
    end()

def turning():
    print('''the fear has too over you\'re body, but you know you have to this
          if that\'s a snake it means everyone\'s in danger.... you walk in the commonroom in silence''')
    j = int(input('1) the snack is there \n2) it\'s gone'))
    if j == 1:
        there()
    if j == 2:
        print('that snake is not on your consern anymore')
        end()

def takelook():
    print('''you look and see snake down the hallway
         and on that moment you remember the picture in your book, that\'s a Basilisk 
         the most dangerous creature on earth''')
    h = int(input('1) staying there and doing nothing\n2) kill it'))
    if h == 1:
        print('chicky!')
        end()
    if h == 2:
        killit()

def talking():
    print('''you start a conversation with Martel \"this sound that you\'re looking for is down there\" she points at a wall
          then she tells you that there\'s a hidden door there.and she tells you that there\'s a Basilisk there''')
    g = int(input('1) you open the door \n2) you back off and leave the room'))
    if g == 1:
        secretdoor()
    if g == 2:
        print('loser')
        end()

def following():
    print('''you get lost because you couldn't find the Chamber
          you lose''')
    end()    

def way():
    print('''you find the way to second floor and you find the Chamber of secret
          as you walk through the Chamber you find a Basilik it attacks you''')
    f = int(input('1) you fight with it and kill it \n2) you die'))
    if f== 1:
        print('you killed it, you won')
        end()
    if f == 2:
        print('stpid')
        end()

def continiue():
    print('''you continiued your way...
          you find the way to second floor and you find the Chamber of secret
          as you walk through the Chamber you find a Basilik it attacks you''')
    f = int(input('1) you fight with it and kill it \n2) you die'))
    if f== 1:
        print('you killed it, you won')
        end()
    if f == 2:
        print('stpid')
        end()

def fight4():
    print('''you start to fight and you kill it
          congratulation''')
    end()

def following2():
    print('''you go throgh the hallway and find the snake
          you recognize it. it\'s a Basilisk... you fight with it and you kill it
          you won''')
    end()

def there():
    print('''you see the snake... you were right.
          but now you must fight to survive
          you start to fight and manage to kill it''')
    end()

def killit():
    print('''you jum out of nowhere and suprise the snake and that suprise gives you time
          to cast the spell and kill it''')
    end()

def secretdoor():
    print('''you get in and you walk and walk
        till you see it, Martel was right... you attck and kill that creatre
          Good job''')
    end()

def end():
    print('''there\'s 595 ways of playing this game
          i hope you liked it''')
    
while S:
    start()
    if end():
        S = False