from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()
tim.speed(0)


def move_forwards():
    tim.forward(2)


def move_backwards():
    tim.backward(2)


def move_clockwise():
    tim.right(2)


def move_counter_clockwise():
    tim.left(2)


def clear_drawing():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="d", fun=move_clockwise)
screen.onkey(key="a", fun=move_counter_clockwise)
screen.onkey(key="c", fun=clear_drawing)
screen.exitonclick()

