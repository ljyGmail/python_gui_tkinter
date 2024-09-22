from tkinter import *

root = Tk()
root.title("WrapLength")
label = Label(
    root,
    text="I like tkinter",
    fg="blue",
    bg="yellow",
    height=3,
    width=15,
    anchor="nw",
    wraplength=40,
)
label.pack()

root.mainloop()
