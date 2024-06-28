import colorgram
import turtle as t
from random import choice

tim = t.Turtle()
tim.shape("circle")
tim.turtlesize(1)
tim.pensize(20)
screen = t.Screen()
t.colormode(255)
screen.screensize(650, 650)


rgb_colors = []
colors = colorgram.extract('spot_image.webp', 100)
print(colors)
print(len(colors))

for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_colors.append(new_color)

print(rgb_colors)


for _ in range(10):
    tim.pencolor(rgb_colors[0 + _])
    tim.dot(20)
    tim.pendown()
    tim.penup()
    tim.forward(50)
print(tim.setpos(0, 70))
print(type(tim.pos()))



screen.exitonclick()