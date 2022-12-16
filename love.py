import turtle

t = turtle.Turtle()
s = turtle.Screen()

s.bgcolor('black')
t.hideturtle()
t.goto(0,-10)

t.pensize()
t.color('red')
t.begin_fill()
t.left(140)
t.forward(180)
t.circle(-90,200)
t.setheading(60)
t.circle(-90,200)
t.forward(178)
t.end_fill()

# if you don't get it, you could change the write string and goto function parameters
t.penup()
t.goto(-150,130)
t.pendown()
t.color('white')
t.write('bentuknya love dulu yaa -dhamski', font = ('Verdana',12,'bold'))

turtle.done()
