import turtle
import random
import sys


rminlength = 1
rmaxlength = 15
gminlength = 1
gmaxlength = 30
bminlength = 1
bmaxlength = 45

rminangle = 45
rmaxangle = 45
gminangle = 90
gmaxangle = 90
bminangle = 135
bmaxangle = 135

drawspeed = 10000

r = turtle.Turtle()
r.color('red')
r.pensize(3)
r.shape('circle')
r.speed(drawspeed)
r.hideturtle()

g = turtle.Turtle()
g.color('green')
g.pensize(3)
g.shape('circle')
g.speed(drawspeed)
g.hideturtle()

b = turtle.Turtle()
b.color('blue')
b.pensize(3)
b.shape('circle')
b.speed(drawspeed)
b.hideturtle()

#Movement

def rmove():
    if(random.randint(1,2) == 1):
        r.left(random.randint(rminangle,rmaxangle))
        if(random.randint(1,2) == 1):
            r.forward(random.randint(rminlength,rmaxlength))
        else:
            r.backward(random.randint(rminlength,rmaxlength))
    else:
        r.right(random.randint(rminangle,rmaxangle))
        if(random.randint(1,2) == 1):
            r.forward(random.randint(rminlength,rmaxlength))
        else:
            r.backward(random.randint(rminlength,rmaxlength))

def gmove():
    if(random.randint(1,2) == 1):
        g.left(random.randint(gminangle,gmaxangle))
        if(random.randint(1,2) == 1):
            g.forward(random.randint(gminlength,gmaxlength))
        else:
            g.backward(random.randint(gminlength,gmaxlength))
    else:
        g.right(random.randint(gminangle,gmaxangle))
        if(random.randint(1,2) == 1):
            g.forward(random.randint(gminlength,gmaxlength))
        else:
            g.backward(random.randint(gminlength,gmaxlength))

def bmove():
    if(random.randint(1,2) == 1):
        b.left(random.randint(bminangle,bmaxangle))
        if(random.randint(1,2) == 1):
            b.forward(random.randint(bminlength,bmaxlength))
        else:
            b.backward(random.randint(bminlength,bmaxlength))
    else:
        b.right(random.randint(bminangle,bmaxangle))
        if(random.randint(1,2) == 1):
            b.forward(random.randint(bminlength,bmaxlength))
        else:
            b.backward(random.randint(bminlength,bmaxlength))

while 1: # loop infinitely
    rmove()
    gmove()
    bmove()


import turtle
from random import choice
from random import randint


class Turtle:
    def __init__(
        self, color, min_len, max_len, angle, speed=10, pensize=3
    ):
        self.min_len = min_len
        self.max_len = max_len
        self.angle = angle
        self.turt = turtle.Turtle()
        self.turt.color(color)
        self.turt.pensize(pensize)
        self.turt.speed(speed)
        self.turt.hideturtle()

    def move(self):
        choice((self.turt.left, self.turt.right))(self.angle)
        dir_func = choice((self.turt.forward, self.turt.backward))
        dir_func(randint(self.min_len, self.max_len))


if __name__ == "__main__":
    turtles = [
        Turtle("red", 1, 15, 45),
        Turtle("green", 1, 30, 90),
        Turtle("blue", 1, 45, 135)
    ]

    while True:
        for turt in turtles:
            turt.move()
