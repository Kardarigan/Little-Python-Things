import turtle

turtle.speed(0)

def rec(w = 100):
  turtle.pendown()
  turtle.color('azure')
  turtle.begin_fill()
  for i in range(2):
    turtle.forward(w)
    turtle.left(90)
    turtle.forward(30)
    turtle.left(90)
    
  turtle.end_fill()
  turtle.penup()
  
turtle.color('#000080')
turtle.begin_fill()
for i in range(6):
  turtle.forward(100)
  turtle.left(60)
turtle.end_fill()  

turtle.penup()

turtle.goto(0, 120)
rec()

turtle.goto(-20, 90)
turtle.right(60)
rec(80)

turtle.goto(95, 105)
turtle.right(60)
rec(80)



turtle.goto(20, 105)
turtle.left(120)

turtle.color('azure')
turtle.begin_fill()

for i in range(3):
  turtle.forward(60)
  turtle.right(120)
  
turtle.end_fill()

turtle.mainloop()