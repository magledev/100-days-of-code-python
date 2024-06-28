import turtle as t
from random import randint

tim = t.Turtle()
tim.turtlesize(2)
tim.speed(0)
screen = t.Screen()
t.colormode(255)


def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    rand_color = (r, g, b)
    return rand_color


circle_gap = int(input("What size gap between circles?: "))
circle_size = int(input("What size cirlce do you want to draw?: "))


def draw_spirograph(gap_size):
    for _ in range(int(360 / gap_size)):
        tim.pencolor(random_color())
        tim.circle(circle_size)
        tim.setheading(tim.heading() + gap_size)

draw_spirograph(circle_gap)

screen.exitonclick()
