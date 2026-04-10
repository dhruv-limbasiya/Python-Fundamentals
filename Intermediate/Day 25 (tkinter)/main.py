import tkinter as tkt
from tkinter import Entry, Button

window = tkt.Tk()
window.title("GUI program")
window.minsize(width=500, height=300)
window.config(padx=100, pady=200)
# lable
my_label = tkt.Label(text="It's label", font=("Arial", 24, "bold"))
my_label.pack()


# second way to create a label
my_label["text"] = "New Text"

# another way to create label
my_label.config(text="new textt")

# place
# my_label.place(x=100, y=200)

# Grid
my_label.grid(column=0, row=0)


# button
def button_clicked():
    print("I got clicked")
    new_text = input.get()
    my_label.config(text=new_text)


button = tkt.Button(text="Clik me", command=button_clicked)
button.grid(column=1, row=1)

new_button = Button(text="new Button")
new_button.grid(column=2,row=0)

# Entry
input = Entry(width=18)
input.grid(column=3,row=2)
print(input.get())

window.mainloop()
