from tkinter import *

root = Tk()
root.title("Font")
label = Label(
    root,
    text="I like tkinter",
    fg="blue",
    bg="yellow",
    height=3,
    width=15,
    # font="Helvetic 20 bold",
    font=("Helvetic", 20, "bold"),
)
label.pack()

root.mainloop()
