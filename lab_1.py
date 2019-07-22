import turtle

# first ^
turtle.penup()
turtle.goto(-175,100)
turtle.pendown()
turtle.left(45)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)

# second ^
turtle.penup()
turtle.left(90)
turtle.goto(175,100)
turtle.pendown()
turtle.forward(100)
turtle.right(90)
turtle.forward(100)

#  ( 
turtle.penup()
turtle.goto(-150,0)
turtle.pendown()
turtle.forward(100)
turtle.left(22.5)
turtle.forward(75)
turtle.left(22.5)
turtle.forward(150)
turtle.left(22.5)
turtle.forward(75)
turtle.left(22.5)
turtle.forward(100)

# |
turtle.penup()
turtle.goto(-150,0)
turtle.pendown()
turtle.right(45)
turtle.forward(450)

turtle.mainloop()
