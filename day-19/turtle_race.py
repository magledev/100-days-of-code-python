from turtle import Turtle, Screen, textinput
from random import randint

screen = Screen()
screen.setup(width=1000, height=400)

is_race_on = False
turtle_list = []

wager = textinput(title="Place your bet",
                  prompt="Place your bets! Which Turtle will be the winner?"
                  "\n(Pick a color:)").lower()
print(wager)

colors = ["red", "green", "blue", "orange", "indigo", "yellow", "violet", "pink", "turquoise"]
turtle_y_pos = [-160, -120, -80, - 40, 0, 40, 80, 120, 160]

for turtle_index in range(0, 9):
    new_turtle = Turtle(shape="turtle")
    new_turtle.speed(0)
    new_turtle.turtlesize(2)
    turtle_list.append(new_turtle)
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-450, y=turtle_y_pos[turtle_index])

if wager:
    is_race_on = True

while is_race_on:
    for turtle in turtle_list:
        if turtle.xcor() > 470:
            is_race_on = False
            winning_turtle = turtle.pencolor()
            if winning_turtle == wager:
                print(f"You win! The {winning_turtle} Turtle is the winner!")
            else:
                print(f"You lose! The {winning_turtle} Turtle is the winner!")

        rand_distance = randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()
