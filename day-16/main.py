# from turtle import Screen, Turtle
#
# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("red", "green")
# timmy.turtlesize(2, 2)
# timmy.position()
# timmy.forward(100)
#
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable
table = PrettyTable()

table.add_column("Pokemon Name", ["Pikachu",
                 "Squirtle", "Charmander"], "l", "m")
table.add_column("Type", ["Electric", "Water", "Fire"], "l", "m")

print(table)
