from tkinter import *


# Define button actions
def miles_to_km():
    km = round(float(entry.get()) * 1.609347088, 2)
    label_km.config(text=f"{km}")


# Create window and base config
window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=250, height=150)
window.config(padx=20, pady=20)

# Buttons
# Calls calculate when pressed
button = Button(text="Calculate", command=miles_to_km)
button.grid(column=1, row=2)

# Create labels
label_1 = Label(text="Miles")
label_1.grid(column=2, row=0)
label_2 = Label(text="is equal to")
label_2.grid(column=0, row=1)
label_3 = Label(text="Km")
label_3.grid(column=2, row=1)
label_km = Label(text="0")
label_km.grid(column=1, row=1)

# Entry box for miles
entry = Entry(width=10, highlightcolor="blue")
print(entry.get())
entry.grid(column=1, row=0)

window.mainloop()
