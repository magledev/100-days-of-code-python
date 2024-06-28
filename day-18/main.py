import turtle as t
from random import choice


tim = t.Turtle()
tim.turtlesize(2)
screen = t.Screen()
screen.colormode(255)
screen.screensize(400, 400)


def draw_shape(num_sides):
    tim.pencolor(choice(range(0, 255)), choice(range(0, 255)), choice(range(0, 255)))
    for _ in range(num_sides):
        tim.forward(100)
        tim.right(360/num_sides)
        tim.forward(10)


t_angle = 360 / int(input("How many shapes do you want to draw?: "))
for _ in range(int(360 / t_angle)):
    tim.right(t_angle)
    for _ in range(3, 10):
        draw_shape(_)


screen.exitonclick()
