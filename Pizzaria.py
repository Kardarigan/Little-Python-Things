import turtle as t
import random as r
t.speed(0)
def p1():
    v = input('''be restorane Haji Rashad khosh omadin. chi meil darin?
          1_ pizza
          2_ cake
          3_ breng''')
    if v == '1':
        pizza()
    elif v == '2':
        cake()
    elif v == '3':
        bre()
    else:
        b = input('fela hamina ro darim.mi khay bekha nemikhay nakha')
        if b == 'mikham':
            p1()

def felfel():
    t.color('green')
    t.pensize(3)
    x = r.randint(30,290)
    y = r.randint(30,290)
    t.up()
    t.goto(x,y)
    t.down()
    t.begin_fill()
    t.circle(15,180)
    t.lt(170)
    t.circle(-15,165)
    t.end_fill()

def jarch():
    x = r.randint(30,290)
    y = r.randint(30,290)
    t.up()
    t.goto(x,y)
    t.down()
    t.color('gray')
    t.begin_fill()
    t.rt(90)
    t.fd(20)
    t.lt(90)
    t.fd(5)
    t.lt(90)
    t.fd(20)
    t.circle(-5,180)
    t.lt(180)
    t.circle(13,180)
    t.lt(180)
    t.circle(-5,180)
    t.end_fill()

def goje():
    t.color('red')
    t.begin_fill()
    x = r.randint(40,275)
    y = r.randint(40,275)
    t.up()
    t.goto(x,y)
    t.down()
    t.circle(15)
    t.end_fill()

def pizza():
    t.color('#6e4713')
    t.pensize(3)
    for i in range(4):
        t.fd(320)
        t.lt(90)
    t.pensize(1)
    t.up()
    t.goto(160,10)
    t.down()
    t.color('#fabe6d','#f5dd96')
    t.begin_fill()
    t.circle(150)
    t.end_fill()
    t.lt(90)
    for i in range(5):
        t.fd(150)
        t.lt(60)
        t.bk(150)
    for i in range(10):
        goje()
    for i in range(10):
        felfel()
    for i in range(10):
        jarch()
  
def cake():
    t.color('#715024')
    t.begin_fill()
    t.circle(115)
    t.end_fill()
    t.up()
    t.goto(-50,55)
    t.down()
    t.color('#ebcfa9')
    t.begin_fill()
    for i in range(4):
        t.fd(100)
        t.circle(5,90)
    t.end_fill()
       
def bre():
    t.bgcolor('white')
    t.color('black')
    t.begin_fill()
    for i in range(4):
        t.fd(200)
        t.circle(10,90)
    t.end_fill()
    for i in range(300):
        ch = r.randint(1,360)
        t.lt(ch)
        bre1()

def bre1():
    t.color('white')
    x = r.randint(5,200)
    y = r.randint(5,200)
    t.up()
    t.goto(x,y)
    t.down()
    for i in range(2):
        t.fd(6)
        t.circle(0.5,180)

p1()
t.mainloop()