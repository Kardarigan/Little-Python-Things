import turtle as t
import random

persianColors = ['#00a693', '#1c39bb', '#0067ab', '#32127a', '#fe28a2', '#f77fbe', '#c81d11', '#d99058', '#701c1c']

t.speed(10)

def pixel():
    R = random.choice(persianColors)
    t.speed(0)
    t.pendown()
    t.color(R)
    t.begin_fill()
    for i in range(4):
        t.fd(10)
        t.left(90)
    t.end_fill()
    t.penup()

def logo_A():
    t.speed(0)
    t.pendown()
    pixel()
    t.bk(10)
    t.lt(90)
    t.fd(10)
    t.rt(90)
    pixel()
    t.rt(90)
    t.fd(10)
    t.lt(90)
    pixel()
    t.bk(10)
    pixel()
    t.fd(10)
    t.rt(90)
    t.fd(10)
    t.lt(90)
    pixel()
    t.fd(10)
    pixel()
    t.rt(90)
    t.fd(10)
    t.lt(90)
    pixel()
    t.fd(10)
    t.lt(90)
    t.fd(10)
    t.rt(90)
    pixel()
    t.lt(90)
    t.fd(10)
    t.rt(90)
    pixel()
    t.fd(10)
    pixel()
    t.bk(10)
    t.lt(90)
    t.fd(10)
    t.rt(90)
    pixel()
    t.bk(10)
    pixel()
    t.lt(90)
    t.fd(10)
    t.rt(90)
    pixel()
    t.penup()

def logo_B():
    for n in range(100):
        t.speed(0)
        logo_A()
        t.lt(90)
        t.fd(30)
        t.rt(90)
        logo_A()
        t.lt(90)
        t.fd(30)
        t.rt(90)
        logo_A()
        t.rt(90)
        t.fd(70)
        t.lt(90)
        t.bk(50)
        logo_A()
        t.rt(90)
        t.fd(20)
        t.lt(90)
        t.fd(100)
        logo_A()
        t.rt(90)
        t.fd(70)
        t.lt(90)
        logo_A()
        t.rt(90)
        t.fd(20)
        t.lt(90)
        t.fd(50)
        logo_A()
        t.rt(90)
        t.fd(20)
        t.lt(90)
        t.bk(150)
        logo_A()
        t.rt(90)
        t.fd(20)
        t.lt(90)
        t.bk(50)
        logo_A()
        t.rt(90)
        t.fd(20)
        t.lt(90)
        t.fd(100)
        t.rt(90)
        t.fd(50)
        t.lt(90)
        logo_A()
        t.rt(90)
        t.fd(20)
        t.lt(90)
        t.bk(50)
        logo_A()
        t.rt(90)
        t.fd(20)
        t.lt(90)
        t.fd(100)
        logo_A()
        t.rt(90)
        t.fd(20)
        t.lt(90)
        t.bk(50)
        t.rt(90)
        t.fd(50)
        t.lt(90)
        logo_A()
        t.lt(90)
        t.fd(80)
        t.rt(90)

E = input('A or B ? ').upper()

if E == 'A' :
    logo_A()

if E == 'B' :
    logo_B()

input()
