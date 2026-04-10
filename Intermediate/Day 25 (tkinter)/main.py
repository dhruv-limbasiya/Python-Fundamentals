import tkinter as tkt
from tkinter import Entry

window = tkt.Tk()
window.title("GUI program")
window.minsize(width=500, height=300)

# lable
my_label = tkt.Label(text="It's label", font=("Arial", 24, "bold"))
my_label.pack()

#second way to create a label
my_label["text"] = "New Text"

#another way to create label
my_label.config(text="new textt")


#button

def button_clicked():
    print("I got clicked")
    new_text = input.get()
    my_label.config(text=new_text)

button = tkt.Button(text = "Clik me", command=button_clicked)
button.pack()


#Entry
input = Entry(width = 18)
input.pack()
print(input.get())

window.mainloop()
