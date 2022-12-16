import turtle

t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor('cyan')
t.speed(0)


for i in range(17):
    t.color('white')
    t.begin_fill()
    t.circle(190-i,90)
    t.left(98)
    t.end_fill()
    t.color('pink')
    t.begin_fill()
    t.circle(190-i,90)
    t.left(18)
    t.end_fill()

t.penup()
t.goto(-270,250)
t.pendown()
t.color('black')
t.write('kali ini bentuknya lebih bunga kan hehe -dhamski', font = ('Verdana',15,'bold'))

s.exitonclick()