from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
Q_FONT = ("Arial", 16, "italic")
S_FONT = ("Arial", 12)


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        # Window elements
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        # Canvas elements
        self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.question_text = self.canvas.create_text(
            150,
            125,
            text="Question text goes here...",
            width=280,
            fill=THEME_COLOR,
            font=Q_FONT
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        # Label elements
        self.score_label = Label(text="Score: 0", bg=THEME_COLOR, fg="white", font=S_FONT)
        self.score_label.grid(row=0, column=1)

        # Button elements
        true_button_image = PhotoImage(file="images/true.png")
        self.true_button = Button(
            image=true_button_image,
            command=self.true_click,
            highlightthickness=0,
            borderwidth=0
        )
        self.true_button.grid(row=2, column=1)

        false_button_image = PhotoImage(file="images/false.png")
        self.false_button = Button(
            image=false_button_image,
            command=self.false_click,
            highlightthickness=0,
            borderwidth=0
        )
        self.false_button.grid(row=2, column=0)

        # Retrieve next question
        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text,
                                   text=f"You have completed the quiz.\n"
                                        f"Your final score was: {self.quiz.score}/{self.quiz.question_number}")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_click(self):
        self.question_feedback(self.quiz.check_answer("True"))

    def false_click(self):
        self.question_feedback(self.quiz.check_answer("False"))

    def question_feedback(self, is_correct):
        if is_correct:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
