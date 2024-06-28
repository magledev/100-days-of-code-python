from tkinter import *
import time
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Roboto"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    global reps
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer")
    check_mark_label.config(text="")
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    # If it is the 8th rep
    if reps % 8 == 0:
        count_down(long_break_sec)
        title_label.config(text="Break", fg=RED)
    # If it is the 2nd/4th/6th rep
    elif reps % 2 == 0:
        count_down(short_break_sec)
        title_label.config(text="Break", fg=PINK)
    # If it is the 1st/3rd/5th/7th rep
    else:
        title_label.config(text="Work", fg=GREEN)
        count_down(work_sec)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✔"
        check_mark_label.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro Break Timer")
window.config(padx=100, pady=50, bg=YELLOW)

checkmark = "✔"

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_image)
timer_text = canvas.create_text(
    100, 134, text="00:00", fill="white", font=(FONT_NAME, 26, "bold"))
canvas.grid(column=1, row=1)

# Labels
title_label = Label(text="Timer", bg=YELLOW, fg=GREEN,
                    font=(FONT_NAME, 36, "bold"))
title_label.grid(column=1, row=0)

check_mark_label = Label(text="", fg=GREEN, bg=YELLOW,
                         font=(FONT_NAME, 24, "bold"))
check_mark_label.grid(column=1, row=3)

# Buttons
start_button = Button(text="Start", command=start_timer, bg="white",
                      highlightthickness=0, font=(FONT_NAME, 14, "bold"))
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", command=reset_timer, bg="white",
                      highlightthickness=0, font=(FONT_NAME, 14, "bold"))
reset_button.grid(column=2, row=2)

window.mainloop()
