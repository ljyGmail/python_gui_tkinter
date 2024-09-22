from tkinter import *

root = Tk()
root.title("Justify")
label = Label(
    root,
    text="abcdefghijklmnopqrstuvwxyz",
    fg="blue",
    bg="lightyellow",
    wraplength=80,
    # justify="left",
    justify="right",
)
label.pack()

root.mainloop()
