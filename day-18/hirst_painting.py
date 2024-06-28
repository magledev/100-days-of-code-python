import colorgram
import turtle as t
from math import sqrt
from random import choice

# Set the turtle's starting attributes
tim = t.Turtle()
tim.hideturtle()
tim.speed(0)
tim.penup()
tim.setpos(-250, -250)

# Set the screens starting attributes
t.colormode(255)
screen = t.Screen()
screen.screensize(500, 500)

# Use colorgram to parse colors from an image
rgb_colors = []
colors = colorgram.extract('spot_image.webp', 100)

# Convert raw colorgram output to usable RGB color list
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_colors.append(new_color)

# Get inputs to determine square size to be drawn
square_size = int(input("What size square? (area): "))
side_length = int(sqrt(square_size))

# Draw the spot art square
for row in range(side_length):
    for column in range(side_length):
        tim.dot(20, choice(rgb_colors))
        tim.forward(50)
    tim.setpos(-250, (tim.ycor() + 50))

screen.exitonclick()
