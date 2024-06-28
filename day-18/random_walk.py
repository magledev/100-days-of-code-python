import turtle as t
from random import choice, randint

tim = t
t.color("red", "green")
t.turtlesize(2)
t.speed(0)
t.pensize(10)

screen = t.Screen()
# screen.screensize(200, 00)
t.colormode(255)


def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    rand_color = (r, g, b)
    return rand_color


def random_walk(entity, steps):
    for _ in steps:
        entity.forward(30)
        entity.pencolor(random_color())
        entity.setheading(choice(range(0, 360, 90)))


how_many = range(int(input("How many steps?: ")))

random_walk(tim, how_many)

screen.exitonclick()
