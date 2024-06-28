import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

guessed_states = []

data = pandas.read_csv("./50_states.csv")
state_list = data["state"].to_list()

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"Correct: {len(guessed_states)}/50",
                                    prompt="Name another State?").title()
    # Using a list comprehension
    if answer_state == "Exit":
        missing_states = [state for state in state_list if state not in guessed_states]
        df = pandas.DataFrame(missing_states)
        df.to_csv("missing_states.csv")
        break
        
    # Using a for loop
    # if answer_state == "Exit":
    #     missing_states = []
    #     for state in data["state"]:
    #         if state not in guessed_states:
    #             missing_states.append(state)
    #     df = pandas.DataFrame(missing_states)
    #     df.to_csv("missing_states.csv")
    #     break

    if answer_state in state_list:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)

screen.exitonclick()

# Use onscreenclick to populate coordinates of each State.
# def get_mouse_clicker_coor(x, y):
#     print(x, y)
# turtle.onscreenclick(get_mouse_clicker_coor)
# turtle.mainloop()
