import tkinter as tkt

window = tkt.Tk()
window.title("GUI program")
window.minsize(width=500, height=300)

# lable
my_label = tkt.Label(text="It's label", font=("Arial", 24, "bold"))
my_label.pack(side="right")

#second way to create a label
my_label["text"] = "New Text"

#another way to create label
my_label.config(text="new textt")


#button

window.mainloop()
