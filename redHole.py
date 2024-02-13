from turtle import *

bgcolor('black')
speed(0)
hideturtle()

for i in range(144):
    color('#AA0000')
    circle(i)
    color('#BA0021')
    circle(i*1.2)
    right(6)
    forward(6)
done()