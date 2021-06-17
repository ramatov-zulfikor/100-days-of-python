from tkinter import *


def calculate():
    answer = int(entry.get()) * 1.6
    answer_label.config(text=answer)


window = Tk()
window.title("Miles to km converter")
window.minsize(width=500, height=300)
window.config(padx=200, pady=100)

entry = Entry()
entry.grid(column=1, row=0)

miles_label = Label(text="miles")
miles_label.grid(column=2, row=0)
miles_label.config(padx=10, pady=10)

equal_label = Label(text="is equal to")
equal_label.grid(column=0, row=1)

answer_label = Label(text="0")
answer_label.grid(column=1, row=1)
answer_label.config(padx=10, pady=10)

km_label = Label(text="Label")
km_label.grid(column=2, row=1)

button = Button(text="Calculate", command=calculate)
button.grid(column=1, row=2)

window.mainloop()
