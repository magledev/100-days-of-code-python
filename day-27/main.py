from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)


my_label = Label(text="I Am a Label", font=("Arial", 24, "bold"))
my_label.pack(side="left")

my_label["text"] = "New Text"
print(my_label)
my_label.config(text="Newer Text")
print(my_label)


def button_clicker():
    my_label.config(text=input.get())


button = Button(text="Click Me", command=button_clicker)
button.pack()

input = Entry(width=10)
input.pack()
print(input.get())

window.mainloop()
