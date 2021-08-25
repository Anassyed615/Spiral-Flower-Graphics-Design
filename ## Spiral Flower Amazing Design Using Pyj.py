## Spiral Flower Amazing Design Using Python turtle

## Python Graphics

import turtle

t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor('black')
col = ('pink','yellow','red','blue')
t.speed(0)

for i in range(170):
    t.pencolor(col[i%4])
    t.setheading(i*95)

    for b in range(4):
        t.forward(i*1)
        t.right(300)