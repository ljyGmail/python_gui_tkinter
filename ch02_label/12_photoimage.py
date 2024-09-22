from tkinter import *

root = Tk()
root.title("PhotoImage")

image = PhotoImage(file="ch01_basics/images/mygithub.png")
label = Label(root, image=image)
label.pack()

root.mainloop()
