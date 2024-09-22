from tkinter import *

root = Tk()
root.title("Anchor")
# label=Label(root,text="I like tkinter",fg="blue",bg="yellow",height=3,width=15,anchor="nw")
# label=Label(root,text="I like tkinter",fg="blue",bg="yellow",height=3,width=15,anchor="se")
label = Label(
    root, text="I like tkinter", fg="blue", bg="yellow", height=3, width=15, anchor=SE
)
label.pack()

root.mainloop()
